<template>
  <div v-if="teamId">
    <h1 class="d-flex align-items-center gap-2 mb-4">
      <img
        v-if="clubs[teamId]?.logo"
        :src="clubs[teamId].logo"
        alt="Team Logo"
        width="128"
        height="128"
        style="object-fit: contain; border-radius: 6px;"
      />
      {{ clubs[teamId]?.name || teamId }}
    </h1>

    
    <h2 class="mt-5">Standings</h2>
    <div v-for="leagueId in leaguesForTeam" :key="'standings-' + leagueId + teamId" class="mb-4">
      <h3>{{ leagues[leagueId] || leagueId }}</h3>

      <div v-if="standings[leagueId] && standings[leagueId][teamId]">
        <StandingsTable
          :standings="standings[leagueId]"
          :clubs="clubs"
          :lastModified="standings[leagueId][teamId]?.date_modified || 'N/A'"
        />
      </div>
      <div v-else>
        <p>No standings for this league.</p>
      </div>
    </div>


    <h2 class="mt-5">Upcoming Matches</h2>
    <div v-for="leagueId in leaguesForTeam" :key="'schedule-' + leagueId" class="mb-4">
      <h3>{{ leagues[leagueId] || leagueId }}</h3>

      <div v-if="scheduleByLeague[leagueId]?.length">
        <MatchCard
          v-for="match in scheduleByLeague[leagueId]"
          :key="match.date + '-' + match.home_id + '-' + match.away_id"
          :match="match"
          :clubs="clubs"
          :standings="standings[leagueId]"
        />
      </div>
      <div v-else>
        <p>No upcoming matches for this league.</p>
      </div>
    </div>

    <h2 class="mt-5">Results</h2>
    <div v-for="leagueId in leaguesForTeam" :key="'results-' + leagueId" class="mb-4">
      <h3>{{ leagues[leagueId] || leagueId }}</h3>

      <div v-if="resultsByLeague[leagueId]?.length">
        <ResultCard
          v-for="match in resultsByLeague[leagueId]"
          :key="match.date + '-' + match.home_id + '-' + match.away_id"
          :match="match"
          :clubs="clubs"
          :standings="standings[leagueId]"
        />
      </div>
      <div v-else>
        <p>No results for this league.</p>
      </div>
    </div>
  </div>

  <div v-else>
    <p>No team ID specified in URL.</p>
  </div>
</template>

<script>
import StandingsTable from './StandingsTable.vue';
import MatchCard from './MatchCard.vue';
import ResultCard from './ResultCard.vue';

export default {
  props: {
    clubs: Object,
    standings: Object,
    schedule: Array,
    results: Array,
    leagues: Object,  // <--- Add leagues prop here
  },
  components: { StandingsTable, MatchCard, ResultCard },
  data() {
    return {
      teamId: null,
    };
  },
  computed: {
    leaguesForTeam() {
      if (!this.teamId || !this.standings) return [];
      return Object.entries(this.standings)
        .filter(([leagueId, teams]) => teams.hasOwnProperty(this.teamId))
        .map(([leagueId]) => leagueId);
    },

    standingsByLeague() {
      if (!this.teamId || !this.standings) return {};
      const byLeague = {};
      for (const leagueId of this.leaguesForTeam) {
        byLeague[leagueId] = this.standings.filter(
          (m) =>
            m.league_id === leagueId && m.team_id === this.teamId
        );
      }
      return byLeague;
    },

    scheduleByLeague() {
      if (!this.teamId || !this.schedule) return {};
      const byLeague = {};
      for (const leagueId of this.leaguesForTeam) {
        byLeague[leagueId] = this.schedule.filter(
          (m) =>
            m.league_id === leagueId &&
            (m.home_id === this.teamId || m.away_id === this.teamId)
        );
      }
      return byLeague;
    },

    resultsByLeague() {
      if (!this.teamId || !this.results) return {};
      const byLeague = {};
      for (const leagueId of this.leaguesForTeam) {
        byLeague[leagueId] = this.results.filter(
          (m) =>
            m.league_id === leagueId &&
            (m.home_id === this.teamId || m.away_id === this.teamId)
        );
      }
      return byLeague;
    },
  },
  mounted() {
    const params = new URLSearchParams(window.location.search);
    this.teamId = params.get('id');
  },
};
</script>
