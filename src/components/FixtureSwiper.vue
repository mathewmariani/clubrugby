<template>
  <DateSwiper
    :items="fixtures"
    :clubs="clubs"
    :leagues="leagues"
    :itemComponent="FixtureCarousel"
    itemProp="fixtures"
  />
</template>

<script setup>
  import DateSwiper from './vue/DateSwiper.vue';
  import FixtureCarousel from './FixtureCarousel.vue';

  const props = defineProps({
    fixtures: { type: Array, required: true },
    leagues: { type: Object, required: true },
    clubs: { type: Object, required: true },
  });
</script>
