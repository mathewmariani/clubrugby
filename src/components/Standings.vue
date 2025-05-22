<template>
  <div v-if="Object.keys(standings).length">
    <div
      v-for="leagueId in sortedLeagueIds"
      :key="'standings-' + leagueId"
      class="mb-5"
    >
      <h2>{{ leagues[leagueId] || leagueId }}</h2>

      <div v-if="standings[leagueId] && Object.keys(standings[leagueId]).length">
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

<script>
import StandingsTable from './StandingsTable.vue';

export default {
  components: { StandingsTable },

  props: {
    standings: { type: Object, required: true },
    clubs: { type: Object, required: true },
    leagues: { type: Object, required: true },
  },

  computed: {
    sortedLeagueIds() {
      // Sort league IDs alphabetically by league name (if available)
      return Object.keys(this.standings).sort((a, b) => {
        const nameA = this.leagues[a] || a;
        const nameB = this.leagues[b] || b;
        return nameA.localeCompare(nameB);
      });
    },
  },

  methods: {
    lastModified(leagueId) {
      // Attempt to get the last modified date from any team in the league standings
      const leagueStandings = this.standings[leagueId];
      if (!leagueStandings) return 'N/A';

      const dates = Object.values(leagueStandings)
        .map(team => team.date_modified)
        .filter(Boolean);

      if (!dates.length) return 'N/A';

      // Return the most recent date string
      return dates.reduce((latest, date) =>
        new Date(date) > new Date(latest) ? date : latest
      );
    },
  },
};
</script>
