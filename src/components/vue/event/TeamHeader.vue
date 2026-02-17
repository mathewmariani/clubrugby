<template>
  <div class="list-group-item">
    <template v-if="isResult">
      <div class="d-flex align-items-center justify-content-between my-3">
        <router-link v-if="home" :to="homeLink">
          <img :src="home.logo" :alt="home.name" />
        </router-link>

        <EventScore :home="homeSummary.score" :away="awaySummary.score" />

        <router-link v-if="away" :to="awayLink">
          <img :src="away.logo" :alt="away.name" />
        </router-link>
      </div>
    </template>

    <template v-else>
      <div class="d-flex gap-3 my-3">
        <router-link v-if="home" :to="homeLink">
          <img :src="home.logo" :alt="home.name" />
        </router-link>
        <div class="d-flex flex-column justify-content-center">
          <h6>{{ home?.name }}</h6>
        </div>
      </div>

      <div class="d-flex gap-3 mb-3 my-3">
        <router-link v-if="away" :to="awayLink">
          <img :src="away.logo" :alt="away.name" />
        </router-link>
        <div class="d-flex flex-column justify-content-center">
          <h6>{{ away?.name }}</h6>
        </div>
      </div>
    </template>
  </div>
</template>

<script setup lang="ts">
  import { computed } from 'vue';
  import { useRouting } from '@/composables/useRouting';
  import EventScore from '@/components/vue/event/EventScore.vue';
  import type { Club, FixtureResultSummary } from '@/types/appData';

  const r = useRouting();

  const props = defineProps<{
    home?: Club;
    away?: Club;
    isResult: boolean;
    homeSummary: FixtureResultSummary;
    awaySummary: FixtureResultSummary;
  }>();

  const homeLink = computed(() => r.club(props.homeSummary.club_id));
  const awayLink = computed(() => r.club(props.awaySummary.club_id));
</script>

<style scoped>
  img {
    width: 64px;
    height: 64px;
    object-fit: contain;
  }
</style>
