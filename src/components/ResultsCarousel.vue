<template>
  <CardCarousel
    :matches="results"
    :clubs="clubs"
    :leagues="leagues"
    :cardComponent="ResultCard"
    sortOrder="desc"
  />
</template>

<script setup>
  import CardCarousel from './vue/CardCarousel.vue';
  import ResultCard from './ResultCard.vue';

  const props = defineProps({
    clubs: { type: Object, required: true },
    leagues: { type: Object, required: true },
    results: { type: Array, required: true },
  });
</script>
