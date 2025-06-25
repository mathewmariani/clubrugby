<template>
  <nav class="navbar bg-body-tertiary fixed-top border-bottom">
    <div class="container-fluid">
      <!-- Top row: Caret back (team view only) + settings -->
      <div class="d-flex w-100 justify-content-between align-items-center">
        <!-- Back caret -->
        <template v-if="isTeamView">
          <div class="d-flex">
            <button class="btn" type="button" @click="goBack">
              <span style="cursor: pointer; font-size: 1rem">❮</span>
            </button>
            <a class="navbar-brand">{{ team.name }}</a>
          </div>
        </template>
        <template v-else>
          <a class="navbar-brand">
            {{ SITE_TITLE }} | {{ union.slug.toUpperCase() }}
          </a>
        </template>

        <!-- Settings always shown -->
        <button
          class="btn"
          type="button"
          data-bs-toggle="offcanvas"
          data-bs-target="#settingsOffcanvas"
          aria-controls="settingsOffcanvas"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
      </div>

      <!-- Brand row -->
      <template v-if="isTeamView">
        <!-- <div class="w-100 d-flex flex-column align-items-center gap-2">
        <img
          :src="team.logo_url"
          :alt="team.name"
          width="64"
          height="64"
          style="object-fit: contain;"
        />
        <p class="text-muted mb-0">{{ team.name }}</p>
      </div> -->
        <TabScroller
          :titles="['Schedule', 'Team Stats']"
          :routes="[`/team/${teamId}/schedule`, `/team/${teamId}/stats`]"
        />
      </template>
      <template v-else>
        <!-- Tab navigation -->
        <TabScroller
          :titles="['Fixtures', 'Results', 'Standings']"
          :routes="['/fixtures', '/results', '/standings']"
        />
      </template>
    </div>

    <!-- Offcanvas always mounted -->
    <SettingsOffcanvas :leagues="leagues" />
  </nav>
</template>

<script setup lang="ts">
  import { computed } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import TabScroller from './TabScroller.vue';
  import SettingsOffcanvas from './SettingsOffcanvas.vue';
  import { SITE_TITLE } from '../../../consts.ts';
  import type { League, Club } from '../../../utils/types.ts';
  import type { Union } from '../../../utils/unions.ts';

  const props = defineProps<{
    union: Union;
    leagues: Record<string, League>;
    clubs?: Record<string, Club>;
  }>();

  const route = useRoute();
  const router = useRouter();

  const isTeamView = computed(() => route.path.startsWith('/team/'));
  const teamId = computed(() => route.params.club_id as string | undefined);
  const team = computed(() =>
    teamId.value && props.clubs ? props.clubs[teamId.value] : null
  );

  function goBack() {
    router.push({ path: `/fixtures` });
  }
</script>

<style scoped></style>
