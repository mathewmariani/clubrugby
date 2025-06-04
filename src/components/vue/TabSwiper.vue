<!-- InfoSwiper.vue -->
<template>
  <TabHeaders
    :titles="sections.map((s) => s.title)"
    :selected-index="selectedIndex"
    @select="goToSlide"
  />

  <Swiper ref="swiperRef" :slides-per-view="1" @slideChange="onSlideChange">
    <SwiperSlide v-for="(section, index) in sections" :key="section.title">
      <component :is="section.component" v-bind="section.props" />
    </SwiperSlide>
  </Swiper>
</template>

<script setup lang="ts">
  import { ref } from 'vue';
  import { Swiper, SwiperSlide } from 'swiper/vue';
  import 'swiper/css';

  const props = defineProps({
    clubs: Object,
    leagues: Object,
    standings: Object,
    fixtures: Object,
    results: Object,
  });

  import TabHeaders from './TabHeaders.vue';
  import FixturesTab from './FixturesTab.vue';
  import ResultsTab from './ResultsTab.vue';
  import StandingsTab from './StandingsTab.vue';

  const sections = [
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
  ];

  const selectedIndex = ref(0);
  const swiperRef = ref<any>(null);

  function goToSlide(index: number) {
    selectedIndex.value = index;
    swiperRef.value?.swiper?.slideTo(index);
  }

  function onSlideChange(swiper: any) {
    selectedIndex.value = swiper.activeIndex;
  }
</script>

<style scoped>
  .swiper {
    width: 100%;
  }
</style>
