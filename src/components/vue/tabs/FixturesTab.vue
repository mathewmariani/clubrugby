<template>
  <div class="list-group list-group-flush">
    <template v-for="(fixtures, day) in dailyFixtures" :key="day">
      <strong class="list-group-item">{{ formatDate(day) }}</strong>
      <template
        v-for="(f, league) in groupFixturesByLeague(fixtures)"
        :key="league"
      >
        <strong class="list-group-item">{{ leagues[league].name }}</strong>
        <FixtureListItem
          v-for="fixture in f"
          :match="fixture"
          :clubs="clubs"
          :leagues="leagues"
        />
      </template>
    </template>
  </div>
</template>

<script setup>
  import { computed } from 'vue';
  import FixtureListItem from '../FixtureListItem.vue';
  import {
    groupFixturesByDay,
    groupFixturesByLeague,
    formatDate,
  } from '../../../utils';
  import { useSavedLeagues } from '../../../composables/useSavedLeagues';

  const props = defineProps({
    clubs: Object,
    leagues: Object,
    fixtures: Object, // should be Fixture[] ideally
  });

  const { savedLeagues } = useSavedLeagues();

  const filteredFixtures = computed(() => {
    if (!savedLeagues.value.length) return props.fixtures;
    return props.fixtures.filter((f) =>
      savedLeagues.value.includes(f.league_id)
    );
  });

  const dailyFixtures = computed(() =>
    groupFixturesByDay(filteredFixtures.value)
  );
</script>

<style scoped>
  .list-group {
    border-radius: 0;
    border-radius: 0;
  }
</style>
