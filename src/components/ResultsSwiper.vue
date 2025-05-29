<template>
  <DateSwiper
    :items="results"
    :clubs="clubs"
    :leagues="leagues"
    :itemComponent="ResultsCarousel"
    itemProp="results"
  />
</template>

<script setup>
  import DateSwiper from './vue/DateSwiper.vue';
  import ResultsCarousel from './ResultsCarousel.vue';

  const props = defineProps({
    results: { type: Array, required: true },
    leagues: { type: Object, required: true },
    clubs: { type: Object, required: true },
  });
</script>
