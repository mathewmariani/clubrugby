<template>
  <Navbar :defaultTitle="nav.title">
    <!-- left slot -->
    <template #left v-if="nav.left">
      <component :is="nav.left" />
    </template>

    <!-- right slot -->
    <template #right v-if="nav.right">
      <component :is="nav.right" />
    </template>

    <!-- tabs slot -->
    <template #tabs v-if="nav.tabs">
      <TabScroller :titles="nav.tabs.titles" :routes="nav.tabs.routes" />
    </template>
  </Navbar>

  <!-- Animated routed pages -->
  <div class="view-container">
    <router-view v-slot="{ Component }">
      <transition :name="`slide-${direction}`" mode="out-in">
        <component :is="Component" :key="$route.fullPath" />
      </transition>
    </router-view>
  </div>
</template>

<script setup lang="ts">
  import { createRouter, createWebHashHistory, useRoute } from 'vue-router';
  import { computed, provide, readonly, ref, getCurrentInstance } from 'vue';

  import Navbar from '@/components/vue/nav/Navbar.vue';
  import TabScroller from '@/components/vue/nav/TabScroller.vue';

  import FixturesList from '@/components/vue/lists/FixturesList.vue';
  import Standings from '@/components/vue/lists/Standings.vue';
  import ClubFixturesList from '@/components/vue/lists/ClubFixturesList.vue';
  import ClubStatsList from '@/components/vue/lists/ClubStatsList.vue';

  import UnionLayout from '@/layouts/vue/UnionLayout.vue';
  import ClubLayout from '@/layouts/vue/ClubLayout.vue';
  import LeagueLayout from '@/layouts/vue/LeagueLayout.vue';

  import type {
    AppData,
    Union,
    Club,
    Standing,
    Fixture,
  } from '@/types/appData';
  import { appDataKey } from '@/types/appData';
  import ShareButton from '@/components/vue/buttons/ShareButton.vue';
  import NavbarToggler from '@/components/vue/buttons/NavbarToggler.vue';
  import { SITE_TITLE } from '@/consts';

  /* --------------------------------------------------
   Props from Astro island
-------------------------------------------------- */

  const props = defineProps<{
    union: Union;
    clubs: Record<string, Club>;
    leagues: Record<string, string>;
    standings: Record<string, Standing[]>;
    fixtures: Record<string, Fixture[]>;
  }>();

  /* --------------------------------------------------
   Provide app data globally
-------------------------------------------------- */

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

  /* --------------------------------------------------
   Router
-------------------------------------------------- */

  const router = createRouter({
    history: createWebHashHistory(),
    scrollBehavior: () => ({ top: 0 }),
    routes: [
      {
        path: '/',
        component: UnionLayout,
        meta: {
          nav: (route: any) => ({
            title: `${SITE_TITLE.toUpperCase()} | ${props.union.slug.toUpperCase()}`,
            left: NavbarToggler,
            tabs: {
              titles: ['Fixtures', 'Results', 'Standings'],
              routes: [`/fixtures`, `/results`, `/standings`],
            },
          }),
        },
        children: [
          { path: '', redirect: { name: 'fixtures' } },
          {
            path: 'fixtures',
            name: 'fixtures',
            component: FixturesList,
          },
          {
            path: 'results',
            name: 'results',
            component: FixturesList,
          },
          {
            path: 'standings',
            name: 'standings',
            component: Standings,
          },
        ],
      },
      {
        path: '/club/:clubId',
        component: ClubLayout,
        meta: {
          nav: (route: any) => ({
            title: `Club ${route.params.clubId}`,
            left: NavbarToggler,
            right: ShareButton,
            tabs: {
              titles: ['Fixtures', 'Stats', 'Standings'],
              routes: [
                `/club/${route.params.clubId}/fixtures`,
                `/club/${route.params.clubId}/stats`,
                `/club/${route.params.clubId}/standings`,
              ],
            },
          }),
        },
        children: [
          { path: '', redirect: { name: 'club-fixtures' } },
          {
            path: 'fixtures',
            name: 'club-fixtures',
            component: ClubFixturesList,
            props: true,
          },
          {
            path: 'stats',
            name: 'club-stats',
            component: ClubStatsList,
            props: true,
          },
          {
            path: 'standings',
            name: 'club-standings',
            component: Standings,
            props: true,
          },
        ],
      },
      {
        path: '/league/:leagueId',
        component: LeagueLayout,
        meta: {
          nav: (route: any) => ({
            title: `Club ${route.params.leagueId}`,
            left: NavbarToggler,
            right: ShareButton,
            tabs: {
              titles: ['Fixtures', 'Results', 'Standings'],
              routes: [
                `/league/${route.params.leagueId}/fixtures`,
                `/league/${route.params.leagueId}/results`,
                `/league/${route.params.leagueId}/standings`,
              ],
            },
          }),
        },
        children: [
          { path: '', redirect: { name: 'league-fixtures' } },
          {
            path: 'fixtures',
            name: 'league-fixtures',
            component: FixturesList,
            props: true,
          },
          {
            path: 'results',
            name: 'league-results',
            component: FixturesList,
            props: true,
          },
          {
            path: 'standings',
            name: 'league-standings',
            component: Standings,
            props: true,
          },
        ],
      },
    ],
  });

  /* --------------------------------------------------
   Install router
-------------------------------------------------- */

  getCurrentInstance()!.appContext.app.use(router);

  /* --------------------------------------------------
   Dynamic Navbar config
-------------------------------------------------- */

  const route = useRoute();

  const nav = computed(() => {
    const meta = route.meta.nav;

    if (!meta) return {};

    return typeof meta === 'function' ? meta(route) : meta;
  });

  /* --------------------------------------------------
   Slide transition direction
-------------------------------------------------- */

  const direction = ref<'forward' | 'back'>('forward');

  router.beforeEach((to, from, next) => {
    const order = ['fixtures', 'standings'];

    const fromIndex = order.indexOf(from.name as string);
    const toIndex = order.indexOf(to.name as string);

    if (fromIndex !== -1 && toIndex !== -1) {
      direction.value = toIndex > fromIndex ? 'forward' : 'back';
    } else {
      direction.value = 'forward';
    }

    next();
  });
</script>
