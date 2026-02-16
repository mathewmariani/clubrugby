<template>
  <div v-if="hasStandings && Object.keys(filteredStandings).length">
    <template v-for="(standing, leagueId) in filteredStandings" :key="leagueId">
      <StandingsTable
        :title="getLeagueName(leagueId, leagues)"
        :standings="standing"
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
  import { computed } from 'vue';
  import StandingsTable from '@/components/vue/tables/StandingsTable.vue';
  import { getLeagueName } from '@/composables/utils';
  import { useAppData } from '@/composables/useAppData';
  import { useStandingsFilters } from '@/composables/useStandingsFilters';

  const { standings, leagues } = useAppData();

  const props = defineProps<{
    leagueId?: string;
    clubId?: string;
  }>();

  const { query, hasStandings } = useStandingsFilters(standings);

  const filteredStandings = computed(() =>
    query({
      leagueId: props.leagueId,
      clubId: props.clubId,
    })
  );
</script>
