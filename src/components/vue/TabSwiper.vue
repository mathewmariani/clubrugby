<template>
  <StickyNavTabs
    :union="union"
    :titles="['Results', 'Fixtures', 'Standings']"
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
    >
      <SwiperSlide v-for="(section, index) in sections" :key="section.title">
        <component :is="section.component" v-bind="section.props" />
      </SwiperSlide>
    </Swiper>
  </div>
</template>

<script setup lang="ts">
  import { ref } from 'vue';
  import { Swiper, SwiperSlide } from 'swiper/vue';
  import 'swiper/css';

  import { type Union } from '../../unions';

  const props = defineProps({
    union: Object,
    clubs: Object,
    leagues: Object,
    standings: Object,
    fixtures: Object,
    results: Object,
  });

  import StickyNavTabs from './StickyNavTabs.vue';
  import FixturesTab from './tabs/FixturesTab.vue';
  import ResultsTab from './tabs/ResultsTab.vue';
  import StandingsTab from './tabs/StandingsTab.vue';

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
  const swiperInstance = ref(null);

  function goToSlide(index) {
    selectedIndex.value = index;
    swiperInstance.value?.slideTo(index);
  }

  function onSlideChange(swiper) {
    selectedIndex.value = swiper.activeIndex;
  }

  function onSwiper(swiper) {
    swiperInstance.value = swiper;
  }
</script>

<style scoped>
  .swiper {
    width: 100%;
  }
</style>
