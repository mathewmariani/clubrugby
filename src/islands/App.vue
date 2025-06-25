<template>
  <Navbar :union="union" :clubs="props.clubs" :leagues="leagues" />

  <RouterView style="margin-top: 88px" />
</template>

<script setup lang="ts">
  import { createRouter, createWebHashHistory, RouterView } from 'vue-router';
  import { onBeforeMount, getCurrentInstance } from 'vue';

  import Navbar from '../components/vue/nav/Navbar.vue';
  import Fixtures from './views/Fixtures.vue';
  import Results from './views/Results.vue';
  import Standings from './views/Standings.vue';
  import EventView from './views/Event.vue';

  import TeamScheduleView from './views/TeamSchedule.vue';
  import TeamStatsView from './views/TeamStats.vue';

  import TeamLayout from '../components/vue/layouts/TeamLayout.vue';

  import { type Union } from '../utils/unions';
  import type { Club, League, Fixture, Result, Standing } from '../utils/types';

  const props = defineProps<{
    union: Union;
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
    fixtures: Record<string, Record<string, Fixture[]>>;
    results: Record<string, Record<string, Result[]>>;
    standings: Record<string, Standing[]>;
  }>();

  const router = createRouter({
    history: createWebHashHistory(),
    scrollBehavior(to, from, savedPosition) {
      return { top: 0 };
    },
    routes: [
      { path: '/', redirect: '/fixtures' },

      {
        path: '/fixtures',
        component: Fixtures,
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
          results: props.results,
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
        path: '/event/:event_id',
        component: EventView,
        props: (route) => ({
          event_id: route.params.event_id,
          fixtures: props.fixtures,
          results: props.results,
          clubs: props.clubs,
          leagues: props.leagues,
          standings: props.standings,
        }),
      },
      {
        path: '/team/:club_id',
        component: TeamLayout,
        props: {
          clubs: props.clubs,
          leagues: props.leagues,
        },
        children: [
          {
            path: 'schedule',
            component: TeamScheduleView,
            props: (route) => ({
              club_id: route.params.club_id,
              fixtures: props.fixtures,
              results: props.results,
              clubs: props.clubs,
              leagues: props.leagues,
            }),
          },
          {
            path: 'stats',
            component: TeamStatsView,
            props: (route) => ({
              club_id: route.params.club_id,
              standings: props.standings,
              clubs: props.clubs,
              leagues: props.leagues,
            }),
          },
          {
            path: '',
            redirect: (to) => `/team/${to.params.club_id}/schedule`,
          },
        ],
      },
    ],
  });

  // Manually install router when app is ready
  onBeforeMount(() => {
    const app = getCurrentInstance()?.appContext.app;
    if (app && !app._installedPlugins?.has(router)) {
      app.use(router);
    }
  });
</script>
