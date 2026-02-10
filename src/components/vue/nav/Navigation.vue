<template>
  <template v-if="Object.keys(leagues).length">
    <h6 class="mt-0">Leagues</h6>
    <ul class="list-group">
      <li
        v-for="(league, league_id) in leagues"
        :key="league_id"
        class="list-group-item list-group-item-action d-flex justify-content-between align-items-center"
        @click="goToLeague(league_id)"
        style="cursor: pointer"
      >
        <span class="fw-semibold">{{ league }}</span>
        <span style="font-size: 1rem">❯</span>
      </li>
    </ul>
  </template>

  <h6 class="mt-3">Display</h6>
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
        <label class="form-check-label" for="switchCheckDefault">
          Dark Mode
        </label>
      </div>
    </li>
  </ul>
</template>

<script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import { useAppData } from '@/composables/useAppData';
  import { useRouter } from 'vue-router';

  const { leagues } = useAppData();
  const router = useRouter();

  const isDarkMode = ref(false);

  const applyDarkMode = () => {
    const html = document.documentElement;
    html.setAttribute('data-bs-theme', isDarkMode.value ? 'dark' : 'light');
  };

  const toggleDarkMode = () => {
    applyDarkMode();
    localStorage.setItem('darkMode', isDarkMode.value ? 'true' : 'false');
  };

  onMounted(() => {
    const saved = localStorage.getItem('darkMode');
    if (saved === 'true') {
      isDarkMode.value = true;
      applyDarkMode();
    }
  });

  // Navigate to league page when item is clicked
  const goToLeague = (league_id: string) => {
    router.push(`/league/${league_id}`);
  };
</script>
