<template>
  <div>
    <template v-if="hasStandings">
      <template
        v-for="leagueGroup in groupedStandings"
        :key="leagueGroup.leagueId"
      >
        <template v-if="leagueGroup.divisions">
          <template
            v-for="division in leagueGroup.divisions"
            :key="division.division"
          >
            <StandingsTable
              :title="division.division"
              :teams="division.teams"
              :clubs="clubs"
              :columns="sortableColumns"
            />
          </template>
        </template>
        <template v-else>
          <StandingsTable
            :title="leagues[leagueGroup.leagueId]?.name || leagueGroup.leagueId"
            :teams="leagueGroup.teams"
            :clubs="clubs"
            :columns="sortableColumns"
          />
        </template>
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
  import { ref, toRef } from 'vue';
  import StandingsTable from '@/components/vue/tables/StandingsTable.vue';
  import type { Club, League, Standing } from '@/utils/types';
  import { useSavedLeagues } from '@/composables/useSavedLeagues';
  import { useFilteredStandings } from '@/composables/useFilteredStandings';

  const props = defineProps<{
    standings: Record<string, Standing[]>;
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
  }>();

  const sortColumn = ref<keyof Standing>('pts');
  const sortDirection = ref<'asc' | 'desc'>('desc');

  const { savedLeagues } = useSavedLeagues();
  const { groupedStandings, hasStandings } = useFilteredStandings(
    toRef(props, 'standings'),
    savedLeagues,
    sortColumn,
    sortDirection
  );

  const sortableColumns = [
    { key: 'pld', label: 'PLD' },
    { key: 'w', label: 'W-D-L' },
    { key: 'pts', label: 'PTS' },
    { key: 'pf', label: 'PF' },
    { key: 'pa', label: 'PA' },
    { key: 'diff', label: 'PD' },
  ];
</script>
