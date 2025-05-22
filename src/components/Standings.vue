<template>
    <div>
      <p v-if="lastModified" class="text-muted">Last updated: {{ lastModified }}</p>
  
      <div
        v-for="(teams, leagueName) in groupedStandings"
        :key="leagueName"
        class="mb-5"
      >
        <h3>{{ leagueName }}</h3>
        <StandingsTable :standings="teams" :clubs="clubs" />
      </div>
    </div>
  </template>
  
  <script>
  import Papa from 'papaparse';
  import StandingsTable from './StandingsTable.vue';
  
  export default {
    components: { StandingsTable },
  
    data() {
      return {
        standings: [],
        clubs: {},
        leagues: {},
        filteredLeagues: [],
        lastModified: null,
      };
    },
  
    computed: {
      groupedStandings() {
        const grouped = {};
        this.standings.forEach((team) => {
          if (
            this.filteredLeagues.length &&
            !this.filteredLeagues.includes(team.league_id)
          )
            return;
  
          const leagueName = this.leagues[team.league_id] || team.league_id;
          if (!grouped[leagueName]) grouped[leagueName] = [];
          grouped[leagueName].push(team);
        });
  
        return Object.fromEntries(
          Object.entries(grouped).sort(([a], [b]) => a.localeCompare(b))
        );
      },
    },
  
    methods: {
      loadSelectedLeagues() {
        const saved = localStorage.getItem('my_leagues');
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
        const [clubsText, standingsText, leaguesText] = await Promise.all([
          fetch('/data/qc/2025/clubs.csv').then((res) => res.text()),
          fetch('/data/qc/2025/standings.csv').then((res) => res.text()),
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
  
            this.loadStandings(standingsText);
          },
        });
  
        const headResponse = await fetch('/data/qc/2025/standings.csv', {
          method: 'HEAD',
        });
        if (headResponse.ok) {
          const lm = headResponse.headers.get('last-modified');
          if (lm) this.lastModified = new Date(lm).toLocaleString();
        }
      },
  
      loadStandings(standingsText) {
        Papa.parse(standingsText, {
          header: true,
          skipEmptyLines: true,
          complete: ({ data }) => {
            const cleaned = data.map(({ date_modified, ...rest }) => rest);
            this.standings = cleaned.sort((a, b) => parseInt(a.pos) - parseInt(b.pos));
          },
        });
      },
    },
  
    mounted() {
      this.loadData();
    },
  };
  </script>
  