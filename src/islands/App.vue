<template>
  <!-- Dynamic Navbar -->
  <Navbar :title="title">
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
  import { computed, provide, readonly, ref, getCurrentInstance } from 'vue';
  import { createRouter, createWebHashHistory, useRoute } from 'vue-router';

  import Navbar from '@/components/vue/nav/Navbar.vue';
  import TabScroller from '@/components/vue/nav/TabScroller.vue';
  import FixturesList from '@/components/vue/lists/FixturesList.vue';
  import ResultsList from '@/components/vue/lists/ResultsList.vue';
  import Standings from '@/components/vue/lists/Standings.vue';
  import ClubFixturesList from '@/components/vue/lists/ClubFixturesList.vue';
  import ClubStatsList from '@/components/vue/lists/ClubStatsList.vue';
  import FixtureDetailsList from '@/components/vue/lists/FixtureDetailsList.vue';
  import FixtureStatsList from '@/components/vue/lists/FixtureStatsList.vue';

  import ShareButton from '@/components/vue/buttons/ShareButton.vue';
  import NavbarToggler from '@/components/vue/buttons/NavbarToggler.vue';
  import { SITE_TITLE } from '@/consts';

  import type {
    AppData,
    Union,
    Club,
    Standing,
    Fixture,
  } from '@/types/appData';
  import { appDataKey } from '@/types/appData';

  /* Props from Astro island */
  const props = defineProps<{
    union: Union;
    clubs: Record<string, Club>;
    leagues: Record<string, string>;
    standings: Record<string, Standing[]>;
    fixtures: Record<string, Fixture[]>;
  }>();

  /* Provide global app data */
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

  /* ------------------------
   Router setup
------------------------ */
  const router = createRouter({
    history: createWebHashHistory(),
    scrollBehavior: () => ({ top: 0 }),
    routes: [
      {
        path: '/',
        meta: {
          nav: (route: any) => ({
            title: `${SITE_TITLE.toUpperCase()} | ${props.union.slug.toUpperCase()}`,
            left: NavbarToggler,
            right: ShareButton,
            tabs: {
              titles: ['Fixtures', 'Results', 'Standings'],
              routes: [
                { name: 'fixtures' },
                { name: 'results' },
                { name: 'standings' },
              ],
            },
          }),
        },
        children: [
          { path: '', redirect: { name: 'fixtures' } },
          { path: 'fixtures', name: 'fixtures', component: FixturesList },
          { path: 'results', name: 'results', component: ResultsList },
          { path: 'standings', name: 'standings', component: Standings },
        ],
      },
      {
        path: '/fixture/:fixtureId',
        meta: {
          nav: (route: any) => ({
            title: `${SITE_TITLE.toUpperCase()} | ${props.union.slug.toUpperCase()}`,
            left: NavbarToggler,
            right: ShareButton,
            tabs: {
              titles: ['Details', 'Stats'],
              routes: [
                { name: 'fixture-details', params: route.params },
                { name: 'fixture-stats', params: route.params },
              ],
            },
          }),
        },
        children: [
          { path: '', redirect: { name: 'fixture-details' } },
          {
            path: 'details',
            name: 'fixture-details',
            component: FixtureDetailsList,
            props: true,
          },
          {
            path: 'stats',
            name: 'fixture-stats',
            component: FixtureStatsList,
            props: true,
          },
        ],
      },
      {
        path: '/club/:clubId',
        meta: {
          nav: (route: any) => ({
            left: NavbarToggler,
            right: ShareButton,
            tabs: {
              titles: ['Fixtures', 'Stats', 'Standings'],
              routes: [
                { name: 'club-fixtures', params: route.params },
                { name: 'club-stats', params: route.params },
                { name: 'club-standings', params: route.params },
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
        meta: {
          nav: (route: any) => ({
            left: NavbarToggler,
            right: ShareButton,
            tabs: {
              titles: ['Fixtures', 'Results', 'Standings'],
              routes: [
                { name: 'league-fixtures', params: route.params },
                { name: 'league-results', params: route.params },
                { name: 'league-standings', params: route.params },
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
            component: ResultsList,
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

  /* Install router */
  getCurrentInstance()!.appContext.app.use(router);

  /* ------------------------
   Navbar meta
------------------------ */
  const route = useRoute();
  const nav = computed(() => {
    const meta = route.meta.nav;
    if (!meta) return {};
    return typeof meta === 'function' ? meta(route) : meta;
  });

  const title = computed(() => {
    const { clubId, leagueId } = route.params as any;

    if (clubId && props.clubs[clubId]) {
      return props.clubs[clubId].name;
    }
    if (leagueId && props.leagues[leagueId]) {
      return props.leagues[leagueId];
    }
    // fallback.
    return nav.value?.title ?? 'Unknown';
  });

  /* ------------------------
   Slide transition direction
------------------------ */
  const direction = ref<'forward' | 'back'>('forward');
  router.beforeEach((to, from, next) => {
    const order = ['fixtures', 'standings']; // main pages order
    const fromIndex = order.indexOf(from.name as string);
    const toIndex = order.indexOf(to.name as string);
    direction.value =
      fromIndex !== -1 && toIndex !== -1 && toIndex < fromIndex
        ? 'back'
        : 'forward';
    next();
  });
</script>
