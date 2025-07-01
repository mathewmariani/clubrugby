<template>
  <h6>Display</h6>
  <ul class="list-group">
    <li class="list-group-item">
      <div class="form-check form-switch">
        <input
          class="form-check-input"
          type="checkbox"
          role="switch"
          id="switchCheckDefault"
          v-model="isDarkMode"
          @change="toggleDarkMode"
        />
        <label class="form-check-label" for="switchCheckDefault"
          >Dark Mode</label
        >
      </div>
    </li>
  </ul>

  <template v-if="!Object.keys(leagues).length"> </template>
  <template v-else>
    <h6 class="mt-3">Leagues</h6>
    <ul class="list-group">
      <li
        v-for="(league, index) in leagues"
        :key="league.id"
        class="list-group-item"
      >
        <div class="form-check form-switch">
          <input
            class="form-check-input"
            type="checkbox"
            role="switch"
            :id="`league-${index}`"
            :checked="!isLeagueSelected(league.id)"
            @change="toggleLeague(league.id)"
          />
          <label class="form-check-label" :for="`league-${index}`">
            {{ league.name }}
          </label>
        </div>
      </li>
    </ul>
  </template>
</template>

<script setup lang="ts">
  import { useSavedLeagues } from '@/composables/useSavedLeagues';
  import { type League } from '@/utils/types';

  import { ref, watch, onMounted } from 'vue';

  const props = defineProps<{
    leagues: Record<string, League>;
  }>();

  const isDarkMode = ref(false);

  const applyDarkMode = () => {
    const html = document.documentElement;
    if (isDarkMode.value) {
      html.setAttribute('data-bs-theme', 'dark');
    } else {
      html.setAttribute('data-bs-theme', 'light');
    }
  };

  const toggleDarkMode = () => {
    applyDarkMode();
    localStorage.setItem('darkMode', isDarkMode.value ? 'true' : 'false');
  };

  // On mount, read saved preference
  onMounted(() => {
    const saved = localStorage.getItem('darkMode');
    if (saved === 'true') {
      isDarkMode.value = true;
      applyDarkMode(true);
    }
  });
  const { savedLeagues: selectedLeagues, setSavedLeagues } = useSavedLeagues();

  const isLeagueSelected = (id: string) => selectedLeagues.value.includes(id);

  const toggleLeague = (id: string) => {
    if (isLeagueSelected(id)) {
      selectedLeagues.value = selectedLeagues.value.filter((lid) => lid !== id);
    } else {
      selectedLeagues.value.push(id);
    }
    setSavedLeagues(selectedLeagues.value);
  };
</script>
