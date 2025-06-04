<template>
  <div v-for="league_result in results">
    <FixtureCard
      v-for="result in league_result"
      :match="result"
      :clubs="clubs"
      :leagues="leagues"
      mode="result"
    />
  </div>
</template>

<script setup>
  import FixtureCard from './FixtureCard.vue';
  const props = defineProps({
    clubs: Object,
    leagues: Object,
    results: Object,
  });
</script>

<style scoped></style>
