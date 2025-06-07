<template>
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

<script setup lang="ts">
  import ResultListItem from '../items/ResultListItem.vue';
  import { type Club, type League, type Result } from '../../../utils/types';
  import { formatDate } from '../../../utils/data';

  const props = defineProps<{
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
    results: Record<string, Record<string, Result[]>>;
  }>();

  import { toRef } from 'vue';
  import { useFilteredResults } from '../../../composables/useFilteredResults';

  const filteredResults = useFilteredResults(toRef(props, 'results'));
</script>

<style scoped>
  .list-group {
    border-radius: 0;
  }
</style>
