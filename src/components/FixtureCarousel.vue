<template>
  <CardCarousel
    :matches="fixtures"
    :clubs="clubs"
    :leagues="leagues"
    :cardComponent="FixtureCard"
    sortOrder="asc"
  />
</template>

<script setup>
  import CardCarousel from './vue/CardCarousel.vue';
  import FixtureCard from './FixtureCard.vue';

  const props = defineProps({
    clubs: { type: Object, required: true },
    leagues: { type: Object, required: true },
    fixtures: { type: Array, required: true },
  });
</script>
