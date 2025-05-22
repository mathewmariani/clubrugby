<template>
  <div v-if="Object.keys(standings).length">
    <div
      v-for="leagueId in sortedFilteredLeagueIds"
      :key="'standings-' + leagueId"
      class="mb-5"
    >
      <h2>{{ leagues[leagueId] || leagueId }}</h2>

      <div
        v-if="standings[leagueId] && Object.keys(standings[leagueId]).length"
      >
        <StandingsTable
          :standings="standings[leagueId]"
          :clubs="clubs"
          :lastModified="lastModified(leagueId)"
        />
      </div>
      <div v-else>
        <p>No standings for this league.</p>
      </div>
    </div>
  </div>
  <div v-else>
    <p>Loading standings...</p>
  </div>
</template>

<script setup>
  import { computed } from 'vue';
  import StandingsTable from './StandingsTable.vue';
  import { useSavedLeagues } from '../utils/useSavedLeagues';

  const props = defineProps({
    standings: { type: Object, required: true },
    clubs: { type: Object, required: true },
    leagues: { type: Object, required: true },
  });

  const { savedLeagues } = useSavedLeagues();

  // Filter league IDs in standings by saved leagues, then sort alphabetically by league name
  const sortedFilteredLeagueIds = computed(() => {
    const filtered = Object.keys(props.standings).filter((leagueId) =>
      savedLeagues.value.includes(leagueId)
    );

    return filtered.sort((a, b) => {
      const nameA = props.leagues[a] || a;
      const nameB = props.leagues[b] || b;
      return nameA.localeCompare(nameB);
    });
  });

  function lastModified(leagueId) {
    const leagueStandings = props.standings[leagueId];
    if (!leagueStandings) return 'N/A';

    const dates = Object.values(leagueStandings)
      .map((team) => team.date_modified)
      .filter(Boolean);

    if (!dates.length) return 'N/A';

    return dates.reduce((latest, date) =>
      new Date(date) > new Date(latest) ? date : latest
    );
  }
</script>
