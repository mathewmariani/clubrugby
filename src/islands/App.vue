<template>
  <Navbar />

  <div class="view-container">
    <router-view v-slot="{ Component }">
      <transition :name="`slide-${direction}`" mode="out-in">
        <component :is="Component" :key="$route.fullPath" />
      </transition>
    </router-view>
  </div>
</template>

<script setup lang="ts">
  import { createRouter, createWebHashHistory } from 'vue-router';
  import { onBeforeMount, getCurrentInstance } from 'vue';
  import { ref } from 'vue';

  import Navbar from '@/components/vue/nav/Navbar.vue';
  import Schedule from './views/Schedule.vue';
  import Results from './views/Results.vue';
  import Standings from './views/Standings.vue';
  import FixtureView from './views/Fixture.vue';

  import ClubFixtures from './views/club/Fixtures.vue';
  import ClubStats from './views/club/Stats.vue';

  import TeamLayout from '@/layouts/vue/TeamLayout.vue';
  import type { Union } from '@/utils/unions';
  import type { Fixture, Standing, Club } from '@/utils/types';

  const props = defineProps<{
    union: Union;
    clubs: Record<string, Club>;
    leagues: Record<string, string>;
    standings: Record<string, Standing[]>;
    fixtures: Record<string, Fixture[]>;
  }>();

  import { provide, readonly } from 'vue';
  provide(
    'appData',
    readonly({
      union: props.union,
      clubs: props.clubs,
      leagues: props.leagues,
      fixtures: props.fixtures,
      standings: props.standings,
    })
  );

  // Setup router
  const router = createRouter({
    history: createWebHashHistory(),
    scrollBehavior: () => ({ top: 0 }),
    routes: [
      { path: '/', redirect: '/fixtures' },
      { path: '/fixtures', component: Schedule },
      { path: '/results', component: Results },
      { path: '/standings', component: Standings },
      // {
      //   path: '/fixture/:fixture_id',
      //   component: FixtureView,
      //   props: (route) => ({
      //     fixture_id: route.params.fixture_id,
      //   }),
      // },
      // {
      //   path: '/club/:club_id',
      //   component: TeamLayout,
      //   props: {
      //     clubs: props.clubs,
      //     leagues: props.leagues,
      //   },
      //   children: [
      //     {
      //       path: 'schedule',
      //       component: ClubFixtures,
      //       props: (route) => ({
      //         club_id: route.params.club_id,
      //       }),
      //     },
      //     {
      //       path: 'stats',
      //       component: ClubStats,
      //       props: (route) => ({
      //         club_id: route.params.club_id,
      //       }),
      //     },
      //     {
      //       path: '',
      //       redirect: (to) => `/club/${to.params.club_id}/schedule`,
      //     },
      //   ],
      // },
    ],
  });

  // Navigation direction tracking logic
  const direction = ref<'forward' | 'back'>('forward');

  router.beforeEach((to, from, next) => {
    const mainPages = ['/fixtures', '/results', '/standings'];

    const isMainFrom = mainPages.some((p) => from.path.startsWith(p));
    const isMainTo = mainPages.some((p) => to.path.startsWith(p));
    const isDetailFrom =
      to.path.startsWith('/fixture') ||
      from.path.startsWith('/fixture') ||
      from.path.startsWith('/club') ||
      to.path.startsWith('/club');

    // 1. Handle main page linear order
    const fromIndex = mainPages.findIndex((p) => from.path.startsWith(p));
    const toIndex = mainPages.findIndex((p) => to.path.startsWith(p));

    if (fromIndex !== -1 && toIndex !== -1) {
      direction.value = toIndex > fromIndex ? 'forward' : 'back';
    }
    // 2. From main page to detail page => forward
    else if (isMainFrom && isDetailFrom) {
      direction.value = 'forward';
    }
    // 3. From detail page to main page => back
    else if (isDetailFrom && isMainTo) {
      direction.value = 'back';
    }
    // 4. Team schedule/stats for same club (detailed)
    else if (from.path.startsWith('/club/') && to.path.startsWith('/club/')) {
      const fromMatch = from.path.match(/^\/club\/([^/]+)\/(schedule|stats)$/);
      const toMatch = to.path.match(/^\/club\/([^/]+)\/(schedule|stats)$/);

      if (fromMatch && toMatch) {
        const [_, fromClub, fromSub] = fromMatch;
        const [__, toClub, toSub] = toMatch;

        if (fromClub === toClub) {
          if (fromSub === 'schedule' && toSub === 'stats') {
            direction.value = 'forward';
          } else if (fromSub === 'stats' && toSub === 'schedule') {
            direction.value = 'back';
          } else {
            direction.value = 'forward';
          }
          next();
          return;
        }
      }
      direction.value = 'forward';
    }
    // default fallback
    else {
      direction.value = 'forward';
    }

    next();
  });

  // Install router on mount
  onBeforeMount(() => {
    const app = getCurrentInstance()?.appContext.app;
    if (app && !app._installedPlugins?.has(router)) {
      app.use(router);
    }
  });
</script>
