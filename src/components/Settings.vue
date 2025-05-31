<template>
  <div class="mt-3">
    <div v-if="!Object.keys(leagues).length">No leagues available.</div>
    <ul v-else class="list-group">
      <li class="list-group-item">
        <strong>Choose leagues to display</strong>
      </li>
      <li v-for="(name, id) in leagues" :key="id" class="list-group-item">
        <label>
          <input type="checkbox" :value="id" v-model="selectedLeagues" />
          {{ name }}
        </label>
      </li>
    </ul>
    <button @click="saveSettings" class="btn-save">Save</button>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue';

  const props = defineProps({
    leagues: { type: Object, required: true },
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
    emit('update-leagues', selectedLeagues.value);
    alert('Settings saved!');
  };

  onMounted(loadSettings);
</script>

<style scoped>
  /* .settings {
    max-width: 400px;
    margin: 2rem auto;
    padding: 1rem;
    background: #f9f9f9;
    border-radius: 8px;
    font-family: sans-serif;
  } */

  h3 {
    margin-bottom: 1rem;
    font-size: 1.25rem;
  }

  .list-group {
    list-style: none;
    padding: 0;
    margin: 0;
  }

  .list-group-item {
    padding: 0.5rem;
    border-bottom: 1px solid #ddd;
    display: flex;
    align-items: center;
  }

  input[type='checkbox'] {
    margin-right: 0.5rem;
  }

  .btn-save {
    margin-top: 1rem;
    padding: 0.5rem 1rem;
    font-weight: bold;
    background: #007aff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  .btn-save:hover {
    background: #005ecb;
  }
</style>
