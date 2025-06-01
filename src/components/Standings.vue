<template>
  <div class="mt-3" v-if="Object.keys(standings).length">
    <StandingsTable
      :standings="filteredStandings"
      :clubs="clubs"
      :leagues="leagues"
    />
  </div>
  <div v-else>
    <p>Loading standings...</p>
  </div>
</template>

<script setup lang="ts">
  import { computed } from 'vue';
  import StandingsTable from './vue/StandingsTable.vue';
  import { useSavedLeagues } from '../composables/useSavedLeagues';

  const props = defineProps({
    standings: { type: Array, required: true },
    clubs: { type: Array, required: true },
    leagues: { type: Array, required: true },
  });

  const { savedLeagues } = useSavedLeagues();

  // this can be composable
  const filteredStandings = computed(() => {
    const result: Record<string, typeof props.standings> = {};
    for (const standing of props.standings) {
      const leagueId = standing.league_id;
      if (savedLeagues.value.includes(leagueId)) {
        if (!result[leagueId]) {
          result[leagueId] = [];
        }
        result[leagueId].push(standing);
      }
    }
    return result;
  });

</script>
