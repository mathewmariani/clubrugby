<template>
  <div v-if="Object.keys(filteredGroupedByLeague).length">
    <div v-for="(dates, leagueId) in filteredGroupedByLeague" :key="leagueId" class="mb-5">
      <h2>{{ leagues[leagueId] || leagueId }}</h2>

      <div v-for="(matches, date) in dates" :key="date" class="mb-4">
        <h4>{{ formatDate(date) }}</h4>
        <div class="row row-cols-1 row-cols-md-2 g-4">
          <div v-for="match in matches" :key="match.id" class="col">
            <ResultCard :match="match" :clubs="clubs" />
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-else>
    <p>Loading results...</p>
  </div>
</template>

<script>
import Papa from 'papaparse';
import ResultCard from './ResultCard.vue';

export default {
  components: { ResultCard },

  data() {
    return {
      clubs: {},
      matches: [],
      leagues: {},
      filteredLeagues: [],
    };
  },

  computed: {
    groupedByLeague() {
      const grouped = {};
      this.matches.forEach((match) => {
        if (!match.date || !match.league_id) return;

        if (!grouped[match.league_id]) grouped[match.league_id] = {};
        if (!grouped[match.league_id][match.date]) grouped[match.league_id][match.date] = [];

        grouped[match.league_id][match.date].push(match);
      });

      Object.keys(grouped).forEach((leagueId) => {
        const sortedDates = Object.keys(grouped[leagueId]).sort((a, b) => {
          const [da, ma, ya] = a.split('/').map(Number);
          const [db, mb, yb] = b.split('/').map(Number);
          return new Date(ya, ma - 1, da) - new Date(yb, mb - 1, db);
        });

        const sortedGroup = {};
        sortedDates.forEach((d) => (sortedGroup[d] = grouped[leagueId][d]));
        grouped[leagueId] = sortedGroup;
      });

      return grouped;
    },

    filteredGroupedByLeague() {
      if (!this.filteredLeagues.length) return this.groupedByLeague;

      const filtered = {};
      this.filteredLeagues.forEach((leagueId) => {
        if (this.groupedByLeague[leagueId]) {
          filtered[leagueId] = this.groupedByLeague[leagueId];
        }
      });
      return filtered;
    },
  },

  methods: {
    formatDate(dateStr) {
      const [day, month, year] = dateStr.split('/');
      const date = new Date(`${year}-${month}-${day}`);
      return new Intl.DateTimeFormat('en-US', {
        weekday: 'long',
        month: 'long',
        day: 'numeric',
      }).format(date);
    },

    loadSelectedLeagues() {
      const saved = localStorage.getItem("my_leagues");
      if (saved) {
        try {
          this.filteredLeagues = JSON.parse(saved);
        } catch {
          this.filteredLeagues = [];
        }
      } else {
        this.filteredLeagues = Object.keys(this.leagues);
      }
    },

    async loadData() {
      try {
        const [clubsText, resultsText, leaguesText] = await Promise.all([
          fetch('/data/qc/2025/clubs.csv').then((res) => res.text()),
          fetch('/data/qc/2025/results.csv').then((res) => res.text()),
          fetch('/data/qc/2025/leagues.csv').then((res) => res.text()),
        ]);

        Papa.parse(clubsText, {
          header: true,
          skipEmptyLines: true,
          complete: ({ data }) => {
            const mapped = {};
            data.forEach((club) => {
              mapped[club.id] = {
                name: club.name,
                logo: club.logo_url,
              };
            });
            this.clubs = mapped;
          },
        });

        Papa.parse(resultsText, {
          header: true,
          skipEmptyLines: true,
          complete: ({ data }) => {
            this.matches = data;
          },
        });

        Papa.parse(leaguesText, {
          header: true,
          skipEmptyLines: true,
          complete: ({ data }) => {
            const mapped = {};
            data.forEach((league) => {
              mapped[league.id] = league.name;
            });
            this.leagues = mapped;

            this.loadSelectedLeagues();
          },
        });
      } catch (err) {
        console.error('Error loading CSV data:', err);
      }
    },
  },

  mounted() {
    this.loadData();
  },
};
</script>
