<template>
  <template v-if="hasResults">
    <div>
      <template v-for="(leaguesForDay, day) in filteredResults" :key="day">
        <!-- Day wrapper -->
        <div class="list-group list-group-flush">
          <!-- Sticky Date Header -->
          <div class="list-group-item bg-body-tertiary sticky-date">
            <strong>{{ formatDate(day) }}</strong>
          </div>

          <!-- League blocks inside day -->
          <template
            v-for="(matches, leagueId) in leaguesForDay"
            :key="leagueId"
          >
            <div class="list-group list-group-flush">
              <!-- Sticky League Header -->
              <div class="list-group-item bg-body-tertiary sticky-league">
                <strong>{{ getLeagueName(leagueId, leagues) }}</strong>
              </div>

              <!-- Results -->
              <ResultListItem
                v-for="match in matches"
                :key="match.id"
                :match="match"
                :clubs="clubs"
                :leagues="leagues"
              />
            </div>
          </template>
        </div>
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
  .sticky-date {
    position: sticky;
    top: 88px; /* navbar height */
    z-index: 10;
  }

  .sticky-league {
    position: sticky;
    top: calc(88px + 2.5rem); /* navbar height + date header height */
    z-index: 9;
  }
</style>
