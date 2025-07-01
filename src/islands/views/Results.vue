<template>
  <div v-if="hasResults">
    <DayMatchGroup
      v-for="(leaguesForDay, day) in filteredResults"
      :key="day"
      :day="day"
      :leagues-for-day="leaguesForDay"
      :clubs="clubs"
      :leagues="leagues"
      match-component="ResultListItem"
    />
  </div>
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
  import DayMatchGroup from '../../components/vue/DayMatchGroup.vue';
  import ResultListItem from '../../components/vue/items/ResultListItem.vue';
  import { useSavedLeagues } from '../../composables/useSavedLeagues';
  import { useFilteredMatches } from '../../composables/useFilteredMatches';
  import type { Club, League, Result } from '../../utils/types';
  import type { Union } from '../../utils/unions';

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
  const filteredResults = useFilteredMatches(results, savedLeagues);

  const hasResults = computed(() =>
    Object.values(filteredResults.value).some(
      (leaguesForDay) => Object.values(leaguesForDay).flat().length > 0
    )
  );
</script>
