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
  import {
    createRouter,
    createMemoryHistory, // ✅ changed
  } from 'vue-router';

  import {
    onBeforeMount,
    getCurrentInstance,
    ref,
    provide,
    readonly,
  } from 'vue';

  import Navbar from '@/components/vue/nav/Navbar.vue';
  import FixturesListView from './views/FixturesListView.vue';
  import ResultsListView from './views/ResultsListView.vue';
  import StandingsView from './views/StandingsView.vue';

  import type { Union } from '@/utils/unions';
  import type { Fixture, Standing, Club } from '@/utils/types';

  const props = defineProps<{
    union: Union;
    clubs: Record<string, Club>;
    leagues: Record<string, string>;
    standings: Record<string, Standing[]>;
    fixtures: Record<string, Fixture[]>;
  }>();

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

  // ✅ memory history (NO URL CHANGES)
  const router = createRouter({
    history: createMemoryHistory(),
    scrollBehavior: () => ({ top: 0 }),
    routes: [
      { path: '/', redirect: '/fixtures' },
      { path: '/fixtures', component: FixturesListView },
      { path: '/results', component: ResultsListView },
      { path: '/standings', component: StandingsView },
    ],
  });

  // transition direction logic stays identical
  const direction = ref<'forward' | 'back'>('forward');

  router.beforeEach((to, from, next) => {
    const mainPages = ['/fixtures', '/results', '/standings'];

    const fromIndex = mainPages.findIndex((p) => from.path.startsWith(p));
    const toIndex = mainPages.findIndex((p) => to.path.startsWith(p));

    if (fromIndex !== -1 && toIndex !== -1) {
      direction.value = toIndex > fromIndex ? 'forward' : 'back';
    } else {
      direction.value = 'forward';
    }

    next();
  });

  // install router
  onBeforeMount(() => {
    const app = getCurrentInstance()?.appContext.app;
    if (app && !app._installedPlugins?.has(router)) {
      app.use(router);
    }
  });
</script>
