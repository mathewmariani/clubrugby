<template>
  <div class="settings">
    <h3>Choose leagues to display</h3>

    <div v-if="!leagues || leagues.length === 0">No leagues available.</div>

    <ul class="list-group">
      <li
        v-for="leagueId in Object.keys(leagues)"
        :key="leagueId"
        class="list-group-item"
      >
        <label>
          <input type="checkbox" :value="leagueId" v-model="selectedLeagues" />
          {{ leagues[leagueId] }}
        </label>
      </li>
    </ul>

    <button @click="saveSettings" class="btn btn-primary mt-3">Save</button>
  </div>
</template>

<script setup>
  import { ref, watch, onMounted } from 'vue';

  const props = defineProps({
    leagues: {
      type: Object,
      required: true,
    },
  });

  const emit = defineEmits(['update-leagues']);

  const selectedLeagues = ref([]);
  const storageKey = 'my_leagues';

  const loadSettings = () => {
    try {
      const saved = localStorage.getItem(storageKey);
      if (saved) {
        selectedLeagues.value = JSON.parse(saved);
      }
    } catch {
      selectedLeagues.value = [];
    }
  };

  const saveSettings = () => {
    localStorage.setItem(storageKey, JSON.stringify(selectedLeagues.value));
    alert('Settings saved!');
    emit('update-leagues', selectedLeagues.value);
  };

  onMounted(() => {
    loadSettings();
  });
</script>

<style scoped>
  .settings {
    max-width: 400px;
  }

  .list-group {
    padding: 0;
    margin: 0;
    list-style: none;
  }

  .list-group-item {
    padding: 0.5rem 0;
    border-bottom: 1px solid #eee;
  }
</style>
