<template>
  <template v-if="hasResults">
    <div class="list-group list-group-flush">
      <template v-for="(leaguesForDay, day) in filteredResults" :key="day">
        <div class="list-group-item bg-body-tertiary">
          <strong>{{ formatDate(day) }}</strong>
        </div>
        <template v-for="(matches, leagueId) in leaguesForDay" :key="leagueId">
          <div class="list-group-item bg-body-tertiary">
            <strong>{{ getLeagueName(leagueId, leagues) }}</strong>
          </div>
          <ResultListItem
            v-for="match in matches"
            :key="match.id"
            :match="match"
            :clubs="clubs"
            :leagues="leagues"
          />
        </template>
      </template>
    </div>
  </template>
  <template v-else>
    <div class="container-fluid text-center text-muted pt-3">
      <p>No results available.</p>
      <hr />
      <p>Ensure your preferences are set.</p>
    </div>
  </template>
</template>

<script setup lang="ts">
  import { computed, toRef } from 'vue';
  import type { Club, League, Result } from '../../../utils/types';
  import ResultListItem from '../../components/vue/items/ResultListItem.vue';
  import { formatDate } from '../../utils/data';
  import { getLeagueName } from '../../composables/utils';
  import { useSavedLeagues } from '../../composables/useSavedLeagues';
  import { useFilteredResults } from '../../composables/useFilteredResults';

  const props = defineProps<{
    union: Union;
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
    results: Record<string, Record<string, Result[]>>;
  }>();

  const clubs = toRef(props, 'clubs');
  const leagues = toRef(props, 'leagues');
  const results = toRef(props, 'results');

  const { savedLeagues } = useSavedLeagues();

  const filteredResults = useFilteredResults(results, savedLeagues);

  const hasResults = computed(() =>
    Object.values(filteredResults.value).some(
      (resultsForDay) => Object.values(resultsForDay).flat().length > 0
    )
  );
</script>

<style scoped>
  .list-group {
    border-radius: 0;
  }
</style>
