<template>
  <!-- Loading Spinner -->
  <div
    v-if="loading"
    class="d-flex justify-content-center align-items-center"
    style="height: 50vh"
  >
    <div class="spinner-border text-primary" role="status">
      <span class="visually-hidden">Loading...</span>
    </div>
  </div>

  <template v-else>
    <Navbar
      :union="union"
      :leagues="leagues"
      :titles="titles"
      :selectedIndex="selectedIndex"
      @select="goToSlide"
    />

    <div
      v-if="loading"
      class="d-flex justify-content-center align-items-center"
      style="height: 50vh"
    >
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>

    <div v-else style="margin-top: 104px">
      <Swiper
        @swiper="onSwiper"
        @slideChange="onSlideChange"
        ref="swiperRef"
        :slides-per-view="1"
        :autoHeight="true"
        :space-between="12"
        :allowTouchMove="false"
      >
        <SwiperSlide v-for="(section, index) in sections" :key="section.title">
          <component
            :is="section.component"
            v-bind="section.props"
            v-on="section.on"
          />
        </SwiperSlide>
      </Swiper>
    </div>
  </template>
</template>

<script setup lang="ts">
  import { ref, computed, onMounted } from 'vue';
  import { Swiper, SwiperSlide } from 'swiper/vue';
  import 'swiper/css';

  import type { Union } from '../../utils/unions';

  import Navbar from './nav/Navbar.vue';
  import FixturesTab from './tabs/FixturesTab.vue';
  import ResultsTab from './tabs/ResultsTab.vue';
  import StandingsTab from './tabs/StandingsTab.vue';
  import DetailsTab from './tabs/DetailsTab.vue';
  import type {
    Club,
    League,
    Fixture,
    Result,
    Standing,
  } from '../../utils/types';

  const loading = ref(true);

  onMounted(() => {
    loading.value = false;
  });

  const props = defineProps<{
    union: Union;
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
    fixtures: Record<string, Record<string, Fixture[]>>;
    results: Record<string, Record<string, Result[]>>;
    standings: Record<string, Standing[]>;
  }>();

  const selectedMatch = ref<Fixture | null>(null);

  const titles = ['Fixtures', 'Results', 'Standings'];

  const sections = computed(() => [
    {
      title: 'Fixtures',
      component: FixturesTab,
      props: {
        clubs: props.clubs,
        leagues: props.leagues,
        fixtures: props.fixtures,
      },
      on: {
        'match-selected': onMatchSelected,
      },
    },
    {
      title: 'Results',
      component: ResultsTab,
      props: {
        clubs: props.clubs,
        leagues: props.leagues,
        results: props.results,
      },
      on: {},
    },
    {
      title: 'Standings',
      component: StandingsTab,
      props: {
        clubs: props.clubs,
        leagues: props.leagues,
        standings: props.standings,
      },
      on: {},
    },
    {
      title: 'Comparison',
      component: DetailsTab,
      props: {
        clubs: props.clubs,
        leagues: props.leagues,
        standings: props.standings,
        match: selectedMatch.value,
      },
      on: {},
    },
  ]);

  const selectedIndex = ref(0);
  const swiperInstance = ref<any>(null);

  function goToSlide(index: number) {
    window.scrollTo({ top: 0, behavior: 'auto' });
    if (!swiperInstance.value) return;
    swiperInstance.value.slideTo(index, 0);
    selectedIndex.value = index;
  }
  function onSlideChange(swiper: any) {
    selectedIndex.value = swiper.activeIndex;
  }

  function onSwiper(swiper: any) {
    swiperInstance.value = swiper;
  }

  function onMatchSelected(match: Fixture) {
    selectedMatch.value = match;
    goToSlide(3);
  }
</script>

<style scoped>
  .swiper {
    width: 100%;
  }
</style>
