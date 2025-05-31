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

<script setup>
  import { computed } from 'vue';
  import StandingsTable from './vue/StandingsTable.vue';
  import { useSavedLeagues } from '../utils/useSavedLeagues';

  const props = defineProps({
    standings: { type: Object, required: true },
    clubs: { type: Object, required: true },
    leagues: { type: Object, required: true },
  });

  const { savedLeagues } = useSavedLeagues();

  const filteredStandings = computed(() => {
    const result = {};
    for (const leagueId of Object.keys(props.standings)) {
      if (savedLeagues.value.includes(leagueId)) {
        result[leagueId] = props.standings[leagueId];
      }
    }
    return result;
  });
</script>
