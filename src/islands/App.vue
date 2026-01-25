<template>
  <Navbar :union="props.union" :clubs="props.clubs" :leagues="props.leagues" />

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

  // Setup router
  const router = createRouter({
    history: createWebHashHistory(),
    scrollBehavior() {
      return { top: 0 };
    },
    routes: [
      { path: '/', redirect: '/schedule' },
      {
        path: '/schedule',
        component: Schedule,
        props: {
          union: props.union,
          fixtures: props.fixtures,
          clubs: props.clubs,
          leagues: props.leagues,
        },
      },
      {
        path: '/results',
        component: Results,
        props: {
          union: props.union,
          fixtures: props.fixtures,
          clubs: props.clubs,
          leagues: props.leagues,
        },
      },
      {
        path: '/standings',
        component: Standings,
        props: {
          union: props.union,
          standings: props.standings,
          clubs: props.clubs,
          leagues: props.leagues,
        },
      },
      {
        path: '/fixture/:fixture_id',
        component: FixtureView,
        props: (route) => ({
          fixture_id: route.params.fixture_id,
          fixtures: props.fixtures,
          clubs: props.clubs,
          leagues: props.leagues,
          standings: props.standings,
        }),
      },
      {
        path: '/club/:club_id',
        component: TeamLayout,
        props: {
          clubs: props.clubs,
          leagues: props.leagues,
        },
        children: [
          {
            path: 'schedule',
            component: ClubFixtures,
            props: (route) => ({
              club_id: route.params.club_id,
              fixtures: props.fixtures,
              clubs: props.clubs,
              leagues: props.leagues,
            }),
          },
          {
            path: 'stats',
            component: ClubStats,
            props: (route) => ({
              club_id: route.params.club_id,
              standings: props.standings,
              clubs: props.clubs,
              leagues: props.leagues,
            }),
          },
          {
            path: '',
            redirect: (to) => `/club/${to.params.club_id}/schedule`,
          },
        ],
      },
    ],
  });

  // Navigation direction tracking logic
  const direction = ref<'forward' | 'back'>('forward');

  router.beforeEach((to, from, next) => {
    const mainPages = ['/schedule', '/results', '/standings'];

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

<style>
  /* Shared transition styles */
  .slide-forward-enter-active,
  .slide-forward-leave-active,
  .slide-back-enter-active,
  .slide-back-leave-active {
    transition:
      transform 0.25s ease,
      opacity 0.25s ease;
  }

  /* Forward navigation: new page slides in from right */
  .slide-forward-enter-from {
    transform: translateX(100%);
    opacity: 0;
  }
  .slide-forward-enter-to {
    transform: translateX(0);
    opacity: 1;
  }
  .slide-forward-leave-from {
    transform: translateX(0);
    opacity: 1;
  }
  .slide-forward-leave-to {
    transform: translateX(-30%);
    opacity: 0;
  }

  /* Back navigation: new page slides in from left */
  .slide-back-enter-from {
    transform: translateX(-30%);
    opacity: 0;
  }
  .slide-back-enter-to {
    transform: translateX(0);
    opacity: 1;
  }
  .slide-back-leave-from {
    transform: translateX(0);
    opacity: 1;
  }
  .slide-back-leave-to {
    transform: translateX(100%);
    opacity: 0;
  }
</style>
