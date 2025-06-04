<template>
  <div v-for="league_fixture in fixtures">
    <FixtureCard
      v-for="fixture in league_fixture"
      :match="fixture"
      :clubs="clubs"
      :leagues="leagues"
      mode="fixture"
    />
  </div>
</template>

<script setup>
  import FixtureCard from './FixtureCard.vue';
  const props = defineProps({
    clubs: Object,
    leagues: Object,
    fixtures: Object,
  });
</script>

<style scoped></style>
