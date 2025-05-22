<template>
  <div>
    <div v-for="leagueId in filteredLeagueIds" :key="leagueId" class="mb-5">
      <h2>{{ leagues[leagueId] || leagueId }}</h2>

      <div v-if="scheduleByLeague[leagueId]?.length">
        <MatchCard
          v-for="match in scheduleByLeague[leagueId]"
          :key="match.date + '-' + match.home_id + '-' + match.away_id"
          :match="match"
          :clubs="clubs"
          :standings="{}"
        />
      </div>
      <div v-else>
        <p>No upcoming matches for this league.</p>
      </div>
    </div>
  </div>
</template>

<script>
import MatchCard from './MatchCard.vue';

export default {
  name: 'Schedule',
  props: {
    schedule: { type: Array, required: true },
    clubs: { type: Object, required: true },
    leagues: { type: Object, required: true },
  },
  components: { MatchCard },
  data() {
    return {
      savedLeagues: [], // leagues from localStorage
    };
  },
  computed: {
    leagueIds() {
      const ids = new Set();
      this.schedule.forEach(m => ids.add(m.league_id));
      return Array.from(ids);
    },
    filteredLeagueIds() {
      // If no saved leagues, show none (or you can default to all)
      if (!this.savedLeagues.length) return [];

      // Filter leagueIds based on savedLeagues
      return this.leagueIds.filter(id => this.savedLeagues.includes(id));
    },
    scheduleByLeague() {
      const byLeague = {};
      for (const leagueId of this.filteredLeagueIds) {
        byLeague[leagueId] = this.schedule.filter(m => m.league_id === leagueId);
      }
      return byLeague;
    },
  },
  mounted() {
    try {
      const saved = localStorage.getItem('my_leagues');
      if (saved) {
        this.savedLeagues = JSON.parse(saved);
      }
    } catch (e) {
      console.error('Failed to parse saved leagues from localStorage:', e);
      this.savedLeagues = [];
    }
  },
};
</script>
