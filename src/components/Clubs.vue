<template>
    <div class="row row-cols-1 row-cols-md-2 g-4">
      <div v-for="club in clubs" :key="club.id" class="col">
        <div class="card d-flex flex-row align-items-center p-2">
          <img
            :src="club.logo_url"
            :alt="club.name"
            class="me-3"
            style="width: 64px; height: 64px; object-fit: contain;"
          />
          <div class="card-body p-0">
            <h5 class="card-title mb-0">{{ club.name }}</h5>
            <a :href="`dashboard.html?id=${club.id}`">Dashboard</a>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import Papa from 'papaparse';
  
  export default {
    name: 'ClubsList',
    data() {
      return {
        clubs: [],
      };
    },
    methods: {
      async fetchClubs() {
        try {
          const text = await fetch('/data/qc/2025/clubs.csv').then(res => res.text());
          Papa.parse(text, {
            header: true,
            skipEmptyLines: true,
            complete: ({ data }) => {
              this.clubs = data;
            },
          });
        } catch (err) {
          console.error('Failed to load clubs:', err);
        }
      },
    },
    mounted() {
      this.fetchClubs();
    },
  };
  </script>
  