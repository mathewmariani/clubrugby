<template>
  <div v-if="teamId">
    <div class="card">
      <div class="card-body d-flex align-items-center">
        <img
          v-if="clubs[teamId]?.logo"
          :src="clubs[teamId].logo"
          alt="Team Logo"
          width="128"
          height="128"
        />
        <h5 class="card-title">{{ clubs[teamId]?.name || teamId }}</h5>
      </div>
      <div class="card-footer">
        <a :href="info[teamId]?.url" class="card-link">Website</a>
        <a :href="'mailto:' + info[teamId]?.email" class="card-link">Email</a>
      </div>
    </div>

    <h2 class="mt-5">Standings</h2>
    <div
      v-for="leagueId in filteredLeaguesForTeam"
      :key="'standings-' + leagueId + teamId"
      class="mb-4"
    >
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
  </div>

  <!-- <h2 class="mt-5">Upcoming Matches</h2>
    <div
      v-for="leagueId in filteredLeaguesForTeam"
      :key="'schedule-' + leagueId"
      class="mb-4"
    >
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
    <div
      v-for="leagueId in filteredLeaguesForTeam"
      :key="'results-' + leagueId"
      class="mb-4"
    >
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
  </div> -->
</template>

<script setup>
  import { ref, computed, onMounted } from 'vue';
  import StandingsTable from './vue/StandingsTable.vue';
  import { useSavedLeagues } from '../utils/useSavedLeagues';

  const props = defineProps({
    standings: { type: Object, required: true },
    results: { type: Array, required: true },
    schedule: { type: Array, required: true },
    clubs: { type: Object, required: true },
    info: { type: Object, required: true },
    leagues: { type: Object, required: true },
  });

  const teamId = ref(null);
  const { savedLeagues } = useSavedLeagues();

  // All leagues where the team has standings
  const leaguesForTeam = computed(() => {
    if (!teamId.value || !props.standings) return [];
    return Object.entries(props.standings)
      .filter(([leagueId, teams]) => teams.hasOwnProperty(teamId.value))
      .map(([leagueId]) => leagueId);
  });

  // Filter leagues based on savedLeagues
  const filteredLeaguesForTeam = computed(() => {
    if (!savedLeagues.value.length) return [];
    return leaguesForTeam.value.filter((leagueId) =>
      savedLeagues.value.includes(leagueId)
    );
  });

  // Schedule filtered by team and league
  const scheduleByLeague = computed(() => {
    if (!teamId.value || !props.schedule) return {};
    const byLeague = {};
    for (const leagueId of filteredLeaguesForTeam.value) {
      byLeague[leagueId] = props.schedule.filter(
        (m) =>
          m.league_id === leagueId &&
          (m.home_id === teamId.value || m.away_id === teamId.value)
      );
    }
    return byLeague;
  });

  // Results filtered by team and league
  const resultsByLeague = computed(() => {
    if (!teamId.value || !props.results) return {};
    const byLeague = {};
    for (const leagueId of filteredLeaguesForTeam.value) {
      byLeague[leagueId] = props.results.filter(
        (m) =>
          m.league_id === leagueId &&
          (m.home_id === teamId.value || m.away_id === teamId.value)
      );
    }
    return byLeague;
  });

  onMounted(() => {
    const params = new URLSearchParams(window.location.search);
    teamId.value = params.get('id');
  });
</script>

<style scoped>
  .settings {
    max-width: 400px;
    margin: 2rem auto;
    padding: 1rem;
    background: #f9f9f9;
    border-radius: 8px;
    font-family: sans-serif;
  }
</style>
