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
  import { provide, readonly, ref } from 'vue';

  import Navbar from '@/components/vue/nav/Navbar.vue';
  import FixturesList from '@/components/vue/lists/FixturesList.vue';
  import Standings from '@/components/vue/lists/Standings.vue';

  import ClubFixturesList from '@/components/vue/lists/ClubFixturesList.vue';
  import ClubStatsList from '@/components/vue/lists/ClubStatsList.vue';

  import FixtureLayout from '@/layouts/vue/FixtureLayout.vue';
  import ClubLayout from '@/layouts/vue/ClubLayout.vue';
  import LeagueLayout from '@/layouts/vue/LeagueLayout.vue';
  import UnionLayout from '@/layouts/vue/UnionLayout.vue';

  import type {
    AppData,
    Union,
    Club,
    Standing,
    Fixture,
  } from '@/types/appData';
  import { appDataKey } from '@/types/appData';

  const props = defineProps<{
    union: Union;
    clubs: Record<string, Club>;
    leagues: Record<string, string>;
    standings: Record<string, Standing[]>;
    fixtures: Record<string, Fixture[]>;
  }>();

  provide(
    appDataKey,
    readonly({
      union: props.union,
      clubs: props.clubs,
      leagues: props.leagues,
      fixtures: props.fixtures,
      standings: props.standings,
    }) as AppData
  );

  // Setup router
  const router = createRouter({
    history: createWebHashHistory(),
    scrollBehavior: () => ({ top: 0 }),
    routes: [
      {
        path: '/',
        component: UnionLayout,
        children: [
          { path: '', redirect: (to) => `/` },
          {
            path: 'fixtures',
            component: FixturesList,
          },
          {
            path: 'results',
            component: FixturesList,
          },
          {
            path: 'standings',
            component: Standings,
          },
        ],
      },
      {
        path: '/fixture/:fixtureId',
        component: FixtureLayout,
        props: true,
      },
      {
        path: '/club/:clubId',
        component: ClubLayout,
        children: [
          {
            path: '',
            redirect: (to) => `/club/${to.params.clubId}/fixtures`,
          },
          {
            path: 'fixtures',
            component: ClubFixturesList,
            props: true,
          },
          {
            path: 'stats',
            component: ClubStatsList,
            props: true,
          },
          {
            path: 'standings',
            component: Standings,
            props: true,
          },
        ],
      },
      {
        path: '/league/:leagueId',
        component: LeagueLayout,
        children: [
          {
            path: '',
            redirect: (to) => `/league/${to.params.leagueId}/fixtures`,
          },
          {
            path: 'fixtures',
            component: FixturesList,
            props: true,
          },
          {
            path: 'results',
            component: FixturesList,
            props: true,
          },
          {
            path: 'standings',
            component: Standings,
            props: true,
          },
        ],
      },
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

  // install router
  onBeforeMount(() => {
    const app = getCurrentInstance()?.appContext.app;
    if (app) {
      app.use(router);
    }
  });
</script>
