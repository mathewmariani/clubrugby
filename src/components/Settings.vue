<template>
    <div class="settings">
      <h3>Choose leagues to display</h3>
      <div v-if="availableLeagues.length === 0">Loading leagues...</div>
      <ul v-else class="list-group">
        <li
          v-for="league in availableLeagues"
          :key="league.id"
          class="list-group-item d-flex justify-content-between align-items-center"
        >
          <label>
            <input
              type="checkbox"
              :value="league.id"
              v-model="selectedLeagues"
            />
            {{ league.name }}
          </label>
        </li>
      </ul>
      <button @click="saveSettings" class="btn btn-primary mt-3">Save</button>
    </div>
  </template>
  
  <script>
  import Papa from "papaparse";
  
  export default {
    name: "Settings",
    data() {
      return {
        availableLeagues: [],
        selectedLeagues: [],
        storageKey: "my_leagues",
      };
    },
    methods: {
      loadLeagues() {
        fetch("/data/qc/2025/leagues.csv")
          .then((res) => res.text())
          .then((text) => {
            Papa.parse(text, {
              header: true,
              skipEmptyLines: true,
              complete: ({ data }) => {
                this.availableLeagues = data;
                this.loadSettings();
              },
            });
          })
          .catch(() => {
            this.availableLeagues = [];
          });
      },
      loadSettings() {
        const saved = localStorage.getItem(this.storageKey);
        if (saved) {
          try {
            this.selectedLeagues = JSON.parse(saved);
          } catch {
            this.selectedLeagues = [];
          }
        }
      },
      saveSettings() {
        localStorage.setItem(
          this.storageKey,
          JSON.stringify(this.selectedLeagues)
        );
        alert("Settings saved!");
        // Optionally emit an event or call a method to notify parent about changes
        this.$emit("update-leagues", this.selectedLeagues);
      },
    },
    mounted() {
      this.loadLeagues();
    },
  };
  </script>
  
  <style scoped>
  .settings {
    max-width: 400px;
  }
  </style>
  