<template>
  <!-- clickable event card -->
  <a class="list-group-item" @click.prevent="goToEvent">
    <div class="d-flex justify-content-between w-100 mb-2">
      <small class="text-body-secondary">{{ match.venue }}</small>
      <div class="d-flex align-items-center gap-2">
        <small class="text-body-secondary">
          {{ match.time }}
          <span>❯</span>
        </small>
      </div>
    </div>

    <div class="d-flex align-items-center gap-2 mb-1">
      <img v-if="home?.logo_url" :src="home.logo_url" :alt="home.name" />
      <span class="text-body-emphasis fw-normal">{{
        home?.name || 'Unknown'
      }}</span>
    </div>

    <div class="d-flex align-items-center gap-2 mb-1">
      <img v-if="away?.logo_url" :src="away.logo_url" :alt="away.name" />
      <span class="text-body-emphasis fw-normal">{{
        away?.name || 'Unknown'
      }}</span>
    </div>
  </a>
</template>

<script setup lang="ts">
  import { useRouter } from 'vue-router';
  import type { Club, Fixture } from '@/utils/types';

  const props = defineProps<{
    home: Club;
    away: Club;
    match: Fixture;
  }>();

  const router = useRouter();
  function goToEvent() {
    const id = `${props.match.league_id}-${props.match.home_id}-${props.match.away_id}-${props.match.date}`;
    router.push({ path: `/event/${id}` });
  }
</script>

<style scoped>
  img {
    width: 32px;
    height: 32px;
    object-fit: contain;
  }
</style>
