<template>
  <div class="list-group-item">
    <div
      v-if="isResult"
      class="d-flex align-items-center justify-content-between my-3"
    >
      <router-link v-if="home" :to="`/team/${home.id}`">
        <img :src="home.logo_url" alt="" />
      </router-link>
      <EventScore :homeScore="homeScore" :awayScore="awayScore" />
      <router-link v-if="away" :to="`/team/${away.id}`">
        <img :src="away.logo_url" alt="" />
      </router-link>
    </div>
    <template v-else>
      <div class="d-flex gap-3 my-3">
        <router-link v-if="home" :to="`/team/${home.id}`">
          <img :src="home.logo_url" alt="" />
        </router-link>
        <div class="d-flex flex-column justify-content-center">
          <h6>{{ home?.name }}</h6>
          <span class="text-muted">{{ homeRecord }}</span>
        </div>
      </div>
      <div class="d-flex gap-3 mb-3 my-3">
        <router-link v-if="away" :to="`/team/${away.id}`">
          <img :src="away.logo_url" alt="" />
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
    homeRecord?: string;
    awayRecord?: string;
    isResult: boolean;
    homeScore?: number;
    awayScore?: number;
  }>();
</script>

<style scoped>
  img {
    width: 64px;
    height: 64px;
    object-fit: contain;
  }
</style>
