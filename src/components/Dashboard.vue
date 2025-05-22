<template>
    <div v-if="teamId">
      <h1 class="d-flex align-items-center gap-2">
        <img
          v-if="clubs[teamId]?.logo"
          :src="clubs[teamId].logo"
          alt="Team Logo"
          width="128"
          height="128"
          style="object-fit: contain;"
        />
        {{ clubs[teamId]?.name || teamId }}
      </h1>
  
      <section v-if="teamStanding">
        <h2>Standings</h2>
        <StandingsTable :standings="[teamStanding]" :clubs="clubs" />
      </section>
  
      <section v-if="teamSchedule.length">
        <h2>Upcoming Schedule</h2>
        <div class="row row-cols-1 row-cols-md-2 g-4">
          <MatchCard
            v-for="match in teamSchedule"
            :key="match.id"
            :match="match"
            :clubs="clubs"
            :highlightTeam="teamId"
          />
        </div>
      </section>
  
      <section v-if="teamResults.length">
        <h2>Recent Results</h2>
        <div class="row row-cols-1 row-cols-md-2 g-4">
          <ResultCard
            v-for="match in teamResults"
            :key="match.id"
            :match="match"
            :clubs="clubs"
            :highlightTeam="teamId"
          />
        </div>
      </section>
    </div>
  
    <div v-else>
      <p>No team ID specified in URL.</p>
    </div>
  </template>
  
  <script>
  import Papa from 'papaparse';
  import StandingsTable from './StandingsTable.vue';
  import MatchCard from './MatchCard.vue';
  import ResultCard from './ResultCard.vue';
  
  export default {
    components: { StandingsTable, MatchCard, ResultCard },
    data() {
      return {
        teamId: null,
        clubs: {},
        standings: {},
        schedule: [],
        results: [],
      };
    },
    computed: {
      teamStanding() {
        return this.standings[this.teamId] || null;
      },
      teamSchedule() {
        const now = new Date();
        return this.schedule.filter(
          (m) =>
            (m.home_id === this.teamId || m.away_id === this.teamId) &&
            new Date(m.date_iso) >= now
        );
      },
      teamResults() {
        const now = new Date();
        return this.results.filter(
          (m) =>
            (m.home_id === this.teamId || m.away_id === this.teamId) &&
            new Date(m.date_iso) < now
        );
      },
    },
    methods: {
      getTeamIdFromUrl() {
        const params = new URLSearchParams(window.location.search);
        return params.get('id');
      },
      async loadData() {
        try {
          const [clubsText, standingsText, scheduleText, resultsText] = await Promise.all([
            fetch('/data/qc/2025/clubs.csv').then((res) => res.text()),
            fetch('/data/qc/2025/standings.csv').then((res) => res.text()),
            fetch('/data/qc/2025/schedule.csv').then((res) => res.text()),
            fetch('/data/qc/2025/results.csv').then((res) => res.text()),
          ]);
  
          // Parse clubs
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
  
          // Parse standings
          Papa.parse(standingsText, {
            header: true,
            skipEmptyLines: true,
            complete: ({ data }) => {
              const standingsMap = {};
              data.forEach((row) => {
                standingsMap[row.team_id] = row;
              });
              this.standings = standingsMap;
            },
          });
  
          // Parse schedule
          Papa.parse(scheduleText, {
            header: true,
            skipEmptyLines: true,
            complete: ({ data }) => {
              this.schedule = data.map((m) => ({
                ...m,
                date_iso: this.convertToISO(m.date),
              }));
            },
          });
  
          // Parse results
          Papa.parse(resultsText, {
            header: true,
            skipEmptyLines: true,
            complete: ({ data }) => {
              this.results = data.map((m) => ({
                ...m,
                date_iso: this.convertToISO(m.date),
              }));
            },
          });
        } catch (error) {
          console.error('Failed to load data:', error);
        }
      },
      convertToISO(dateStr) {
        const [day, month, year] = dateStr.split('/');
        return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`;
      },
    },
    mounted() {
      this.teamId = this.getTeamIdFromUrl();
      if (this.teamId) {
        this.loadData();
      }
    },
  };
  </script>
  
  <style scoped>
  /* Optional styling for the header image */
  h1 img {
    border-radius: 6px;
    object-fit: contain;
  }
  </style>
  