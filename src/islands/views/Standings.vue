<template>
  <div>
    <template v-if="hasStandings">
      <template v-for="(standing, leagueId) in standings" :key="leagueId">
        <div>
          <StandingsTable
            :title="getLeagueName(leagueId.toString(), leagues)"
            :standings="standing"
            :columns="sortableColumns"
          />
        </div>
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
  import { getLeagueName } from '@/composables/utils';

  import { useAppData } from '@/composables/useAppData';
  const { standings, leagues } = useAppData();

  // No more grouping or filtering needed
  const hasStandings = computed(() => Object.keys(standings).length > 0);

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
