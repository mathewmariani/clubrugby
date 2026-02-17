<template>
  <template v-if="Object.keys(leagues).length">
    <h6 class="mt-0">Leagues</h6>
    <ul class="list-group">
      <router-link
        class="list-group-item list-group-item-action d-flex justify-content-between align-items-center"
        :to="unionLink"
      >
        <span class="fw-semibold">{{ union.slug.toUpperCase() }}</span>
        <span style="font-size: 1rem">❯</span>
      </router-link>

      <router-link
        v-for="(leagueName, leagueId) in leagues"
        :key="leagueId"
        class="list-group-item list-group-item-action d-flex justify-content-between align-items-center"
        :to="leagueLink(leagueId)"
      >
        <span class="fw-semibold">{{ leagueName }}</span>
        <span style="font-size: 1rem">❯</span>
      </router-link>
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
  import { ref, onMounted, computed } from 'vue';
  import { useAppData } from '@/composables/useAppData';
  import { useRouting } from '@/composables/useRouting';

  const { union, leagues } = useAppData();
  const r = useRouting(union.slug);

  const isDarkMode = ref(false);

  const applyDarkMode = () => {
    document.documentElement.setAttribute(
      'data-bs-theme',
      isDarkMode.value ? 'dark' : 'light'
    );
  };

  const toggleDarkMode = () => {
    applyDarkMode();
    localStorage.setItem('darkMode', isDarkMode.value ? 'true' : 'false');
  };

  // Vue Router links
  const unionLink = computed(() => r.union());
  const leagueLink = (leagueId: string) => r.league(leagueId);

  onMounted(() => {
    const saved = localStorage.getItem('darkMode');
    if (saved === 'true') {
      isDarkMode.value = true;
      applyDarkMode();
    }
  });
</script>
