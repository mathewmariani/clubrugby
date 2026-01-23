<template>
  <div>
    <template v-if="hasStandings">
      <template v-for="(teams, leagueId) in standings" :key="leagueId">
        <StandingsTable
          :title="leagues[leagueId]?.name || leagueId"
          :teams="teams"
          :clubs="clubs"
          :columns="sortableColumns"
        />
      </template>
    </template>

    <template v-else>
      <div class="container-fluid text-center text-muted pt-3">
        <p>No standings available.</p>
        <hr />
        <p>Ensure your preferences are set.</p>
      </div>
    </template>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import StandingsTable from '@/components/vue/tables/StandingsTable.vue';
import type { Club, League, Standing } from '@/utils/types';

const props = defineProps<{
  standings: Record<string, Standing[]>; // already sorted by league & rank
  clubs: Record<string, Club>;
  leagues: Record<string, League>;
}>();

// No more grouping or filtering needed
const hasStandings = computed(() => Object.keys(props.standings).length > 0);

// Columns to display in the table
const sortableColumns = [
  { key: 'played', label: 'PLD' },
  { key: 'w-d-l', label: 'W-D-L' },
  { key: 'points', label: 'PTS' },
  { key: 'pointsFor', label: 'PF' },
  { key: 'pointsAgainst', label: 'PA' },
  { key: 'pointsDifference', label: 'PD' },
];
</script>
