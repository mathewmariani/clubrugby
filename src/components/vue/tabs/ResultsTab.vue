<template>
  <div class="list-group list-group-flush">
    <template v-for="(results, day) in dailyResults" :key="day">
      <strong class="list-group-item">{{ formatDate(day) }}</strong>
      <!-- {{  groupResultsByLeague(results)  }} -->
      <template
        v-for="(r, league) in groupResultsByLeague(results)"
        :key="league"
      >
        <strong class="list-group-item">{{ leagues[league].name }}</strong>
        <ResultListItem
          v-for="results in r"
          :match="results"
          :clubs="clubs"
          :leagues="leagues"
        />
      </template>
    </template>
  </div>
</template>

<!-- <template>
  <div class="list-group list-group-flush">
    <template v-for="(results, day) in dailyResults" :key="day">
      <strong class="list-group-item">{{ formatDate(day) }}</strong>
      <ResultListItem
        v-for="result in results"
        :match="result"
        :clubs="clubs"
        :leagues="leagues"
      />
    </template>
  </div>
</template> -->

<script setup>
  import { computed } from 'vue';
  import ResultListItem from '../ResultListItem.vue';
  import {
    groupFixturesByDay,
    groupResultsByLeague,
    formatDate,
  } from '../../../utils';
  import { useSavedLeagues } from '../../../composables/useSavedLeagues'; // adjust path as needed

  const props = defineProps({
    clubs: Object,
    leagues: Object,
    results: Object,
  });

  const { savedLeagues } = useSavedLeagues();

  const filteredResults = computed(() => {
    if (!savedLeagues.value.length) return props.results;
    return props.results.filter((r) =>
      savedLeagues.value.includes(r.league_id)
    );
  });

  const dailyResults = computed(() =>
    groupFixturesByDay(filteredResults.value)
  );
</script>

<style scoped>
  .list-group {
    border-radius: 0;
    border-radius: 0;
  }
</style>
