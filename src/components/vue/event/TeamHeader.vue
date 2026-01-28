<template>
  <div class="list-group-item">
    <template v-if="isResult">
      <div class="d-flex align-items-center justify-content-between my-3">
        <router-link v-if="home" :to="`/club/${homeSummary.club_id}`">
          <img :src="home.logo" alt="" />
        </router-link>
        <EventScore :home="homeSummary.score" :away="awaySummary.score" />
        <router-link v-if="away" :to="`/club/${awaySummary.club_id}`">
          <img :src="away.logo" alt="" />
        </router-link>
      </div>
    </template>
    <template v-else>
      <div class="d-flex gap-3 my-3">
        <router-link v-if="home" :to="`/club/${homeSummary.club_id}`">
          <img :src="home.logo" alt="" />
        </router-link>
        <div class="d-flex flex-column justify-content-center">
          <h6>{{ away?.name }}</h6>
          <!-- <span class="text-muted">{{ homeRecord }}</span> -->
        </div>
      </div>
      <div class="d-flex gap-3 mb-3 my-3">
        <router-link v-if="away" :to="`/club/${awaySummary.club_id}`">
          <img :src="away.logo" alt="" />
        </router-link>
        <div class="d-flex flex-column justify-content-center">
          <h6>{{ away?.name }}</h6>
          <!-- <span class="text-muted">{{ awayRecord }}</span> -->
        </div>
      </div>
    </template>
  </div>
</template>

<script setup lang="ts">
  import type { Club, FixtureResultSummary } from '@/utils/types';
  import EventScore from './EventScore.vue';
  defineProps<{
    home?: Club;
    away?: Club;
    isResult: boolean;
    homeSummary: FixtureResultSummary;
    awaySummary: FixtureResultSummary;
  }>();
</script>

<style scoped>
  img {
    width: 64px;
    height: 64px;
    object-fit: contain;
  }
</style>
