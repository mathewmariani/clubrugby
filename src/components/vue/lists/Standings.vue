<template>
  <div v-if="hasStandings">
    <template v-for="(standing, leagueId) in standings" :key="leagueId">
      <StandingsTable
        :title="getLeagueName(leagueId, leagues)"
        :standings="standing"
        :columns="sortableColumns"
      />
    </template>
  </div>

  <div v-else class="container-fluid text-center text-muted pt-3">
    <p>No standings available.</p>
    <hr />
    <p>Ensure your preferences are set.</p>
  </div>
</template>

<script setup lang="ts">
  import StandingsTable from '@/components/vue/tables/StandingsTable.vue';
  import { getLeagueName } from '@/composables/utils';
  import { useAppData } from '@/composables/useAppData';
  import { useStandingsFilters } from '@/composables/useStandingsFilters';

  const { standings: allStandings, leagues } = useAppData();

  const props = defineProps<{
    leagueId?: string;
  }>();

  const { standings, hasStandings } = useStandingsFilters(allStandings, {
    leagueId: props.leagueId,
  });

  const sortableColumns = [
    { key: 'played', label: 'PLD' },
    { key: 'w-d-l', label: 'W-D-L' },
    { key: 'points', label: 'PTS' },
    { key: 'pointsFor', label: 'PF' },
    { key: 'pointsAgainst', label: 'PA' },
    { key: 'pointsDifference', label: 'PD' },
  ];
</script>
