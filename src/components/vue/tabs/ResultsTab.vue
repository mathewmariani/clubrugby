<template>
  <template v-if="hasResults">
    <div class="list-group list-group-flush">
      <template v-for="(leaguesForDay, day) in filteredResults" :key="day">
        <strong class="list-group-item">{{ formatDate(day) }}</strong>
        <template v-for="(matches, leagueId) in leaguesForDay" :key="leagueId">
          <strong class="list-group-item">{{
            leagues[leagueId]?.name || 'Unknown League'
          }}</strong>
          <ResultListItem
            v-for="match in matches"
            :match="match"
            :clubs="clubs"
            :leagues="leagues"
          />
        </template>
      </template>
    </div>
  </template>
  <!-- No results fallback -->
  <template v-else>
    <div class="container mt-3 text-center text-muted">
      <p>No results available.</p>
      <p>Ensure your preferences are set.</p>
    </div>
  </template>
</template>

<script setup lang="ts">
  import { computed } from 'vue';
  import ResultListItem from '../items/ResultListItem.vue';
  import type { Club, League, Result } from '../../../utils/types';
  import { formatDate } from '../../../utils/data';

  const props = defineProps<{
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
    results: Record<string, Record<string, Result[]>>;
  }>();

  import { toRef } from 'vue';
  import { useSavedLeagues } from '../../../composables/useSavedLeagues';
  import { useFilteredResults } from '../../../composables/useFilteredResults';

  const { savedLeagues } = useSavedLeagues();
  const filteredResults = useFilteredResults(
    toRef(props, 'results'),
    savedLeagues
  );

  const hasResults = computed(() => {
    return Object.values(filteredResults.value).some(
      (resultsForDay) => Object.values(resultsForDay).flat().length > 0
    );
  });
</script>

<style scoped>
  .list-group {
    border-radius: 0;
  }
</style>
