<template>
  <div class="mt-3">
    <div v-if="!Object.keys(leagues).length">No leagues available.</div>
    <ul v-else class="list-group">
      <li class="list-group-item">
        <strong>Choose leagues to display</strong>
      </li>
      <li v-for="(name, id) in leagues" :key="id" class="list-group-item">
        <div class="form-check">
          <input
            @change="saveSettings"
            :value="id"
            v-model="selectedLeagues"
            class="form-check-input"
            type="checkbox"
            :id="`league-${id}`"
          />
          <label class="form-check-label" :for="`league-${id}`">
            {{ name }}
          </label>
        </div>
      </li>
    </ul>
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
  };

  onMounted(loadSettings);
</script>
