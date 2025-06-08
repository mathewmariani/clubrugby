<template>
  <Navbar
    client:only="vue"
    :union="union"
    :leagues="leagues"
    :titles="titles"
    :selectedIndex="selectedIndex"
    @select="goToSlide"
  />

  <div style="margin-top: 104px">
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
        <component :is="section.component" v-bind="section.props" />
      </SwiperSlide>
    </Swiper>
  </div>
</template>

<script setup lang="ts">
  import { ref, computed } from 'vue';
  import { Swiper, SwiperSlide } from 'swiper/vue';
  import 'swiper/css';

  import type { Union } from '../../utils/unions';

  import Navbar from './nav/Navbar.vue';
  import FixturesTab from './tabs/FixturesTab.vue';
  import ResultsTab from './tabs/ResultsTab.vue';
  import StandingsTab from './tabs/StandingsTab.vue';
  import {
    type Club,
    type League,
    type Fixture,
    type Result,
  } from '../../utils/types';

  const props = defineProps<{
    union: Union;
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
    fixtures: Record<string, Record<string, Fixture[]>>;
    results: Record<string, Record<string, Result[]>>;
    standings: Record<string, any[]>;
  }>();

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
    },
    {
      title: 'Results',
      component: ResultsTab,
      props: {
        clubs: props.clubs,
        leagues: props.leagues,
        results: props.results,
      },
    },
    {
      title: 'Standings',
      component: StandingsTab,
      props: {
        clubs: props.clubs,
        leagues: props.leagues,
        standings: props.standings,
      },
    },
  ]);

  const selectedIndex = ref(0);
  const swiperInstance = ref<any>(null);

  function goToSlide(index: number) {
    selectedIndex.value = index;
    swiperInstance.value?.slideTo(index);
  }

  function onSlideChange(swiper: any) {
    selectedIndex.value = swiper.activeIndex;
  }

  function onSwiper(swiper: any) {
    swiperInstance.value = swiper;
  }
</script>

<style scoped>
  .swiper {
    width: 100%;
  }
</style>
