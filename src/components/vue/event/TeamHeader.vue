<template>
  <div class="list-group-item">
    <template v-if="isResult">
      <div class="d-flex align-items-center justify-content-between my-3">
        <router-link v-if="home" :to="`/club/${homeClubId}`">
          <img :src="home.logo" alt="" />
        </router-link>
        <EventScore :homeScore="homeScore" :awayScore="awayScore" />
        <router-link v-if="away" :to="`/club/${awayClubId}`">
          <img :src="away.logo" alt="" />
        </router-link>
      </div>
    </template>
    <template v-else>
      <div class="d-flex gap-3 my-3">
        <router-link v-if="home" :to="`/club/${homeClubId}`">
          <img :src="home.logo" alt="" />
        </router-link>
        <div class="d-flex flex-column justify-content-center">
          <h6>{{ home?.name }}</h6>
          <span class="text-muted">{{ homeRecord }}</span>
        </div>
      </div>
      <div class="d-flex gap-3 mb-3 my-3">
        <router-link v-if="away" :to="`/club/${awayClubId}`">
          <img :src="away.logo" alt="" />
        </router-link>
        <div class="d-flex flex-column justify-content-center">
          <h6>{{ away?.name }}</h6>
          <span class="text-muted">{{ awayRecord }}</span>
        </div>
      </div>
    </template>
  </div>
</template>

<script setup lang="ts">
  import type { Club } from '@/utils/types';
  import EventScore from './EventScore.vue';
  defineProps<{
    home?: Club;
    away?: Club;
    homeClubId?: string;
    awayClubId?: string;
    homeRecord?: string;
    awayRecord?: string;
    isResult: boolean;
    homeScore?: string;
    awayScore?: string;
  }>();
</script>

<style scoped>
  img {
    width: 64px;
    height: 64px;
    object-fit: contain;
  }
</style>
