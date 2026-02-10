<template>
  <!-- Dynamic navbar -->
  <nav ref="navbarRef" class="navbar bg-body-tertiary fixed-top border-bottom">
    <div class="container-fluid">
      <div class="d-flex w-100 justify-content-between align-items-center">
        <div class="d-flex align-items-center">
          <template v-if="isTeamView || isEventView">
            <button
              class="btn"
              type="button"
              @click="goBack"
              aria-label="Go Back"
            >
              <span style="cursor: pointer; font-size: 1rem">❮</span>
            </button>
          </template>
          <template v-if="isTeamView">
            <a class="navbar-brand mb-0 ms-2">{{ team?.name }}</a>
          </template>
          <template v-else>
            <a class="navbar-brand mb-0">
              {{ SITE_TITLE }} | {{ union.slug.toUpperCase() }}
            </a>
          </template>
        </div>
        <!-- Settings always shown -->
        <button
          class="btn"
          type="button"
          data-bs-toggle="offcanvas"
          data-bs-target="#settingsOffcanvas"
          aria-controls="settingsOffcanvas"
          aria-label="Open Settings"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
      </div>

      <!-- Tab navigation -->
      <TabScroller
        v-if="isLeagueView"
        :titles="['Fixtures', 'Results', 'Standings']"
        :routes="['/fixtures', '/results', '/standings']"
      />
      <TabScroller
        v-else-if="isTeamView"
        :titles="['Schedule', 'Stats']"
        :routes="[`/club/${teamId}/fixtures`, `/club/${teamId}/stats`]"
      />
    </div>

    <!-- Offcanvas always mounted -->
    <SettingsOffcanvas :leagues="leagues" />
  </nav>

  <!-- Spacer pushes content down based on navbar height -->
  <div :style="{ height: navbarHeight + 'px' }"></div>
</template>

<script setup lang="ts">
  import { ref, computed, onMounted, onUpdated, watch } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import { useLayout } from '@/composables/useLayout';

  import TabScroller from './TabScroller.vue';
  import SettingsOffcanvas from './SettingsOffcanvas.vue';

  import { SITE_TITLE } from '@/consts.ts';

  import { useAppData } from '@/composables/useAppData';
  const { union, clubs, leagues } = useAppData();

  const route = useRoute();
  const router = useRouter();

  const isLeagueView = computed(() =>
    ['/fixtures', '/results', '/standings'].some((v) =>
      route.path.startsWith(v)
    )
  );

  const isTeamView = computed(() => route.path.startsWith('/club/'));
  const isEventView = computed(() => route.path.startsWith('/fixture/'));

  const teamId = computed(() => route.params.club_id as string | undefined);
  const team = computed(() =>
    teamId.value && clubs ? clubs[teamId.value] : null
  );

  // Navigation handler
  function goBack() {
    router.push({ path: '/fixtures' });
  }

  // Dynamic navbar height
  const navbarRef = ref<HTMLElement | null>(null);
  const { navbarHeight } = useLayout();

  function updateNavbarHeight() {
    navbarHeight.value = navbarRef.value?.offsetHeight || 0;
  }

  // Ensure the height updates on mount and when route changes (e.g., new tab)
  onMounted(updateNavbarHeight);
  onUpdated(updateNavbarHeight);
  watch([isTeamView, teamId], updateNavbarHeight);
</script>

<style scoped></style>
