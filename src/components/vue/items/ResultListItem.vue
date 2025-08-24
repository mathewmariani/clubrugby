<template>
  <a class="list-group-item" @click.prevent="goToEvent">
    <div class="d-flex align-items-center gap-2 mb-1">
      <img v-if="home?.logo_url" :src="home.logo_url" :alt="home.name" />
      <!-- <small>{{ home?.name || 'Unknown' }}</small> -->
      <span class="text-body-emphasis fw-normal">{{
        home?.name || 'Unknown'
      }}</span>
      <strong
        :class="scoreClass(match.home_score, match.away_score)"
        class="ms-auto"
        >{{ match.home_score || 'Unknown' }}</strong
      >
    </div>
    <div class="d-flex align-items-center gap-2 mb-1">
      <img v-if="away?.logo_url" :src="away.logo_url" :alt="away.name" />
      <span class="text-body-emphasis fw-normal">{{
        away?.name || 'Unknown'
      }}</span>
      <strong
        :class="scoreClass(match.away_score, match.home_score)"
        class="ms-auto"
        >{{ match.away_score || 'Unknown' }}</strong
      >
    </div>
  </a>
</template>

<script setup lang="ts">
  import { useRouter } from 'vue-router';
  import type { Club, Result } from '@/utils/types';
  import { useEncodedRoute } from "@/composables/useEncodedRoute";

  const props = defineProps<{
    home: Club;
    away: Club;
    match: Result;
  }>();

  function scoreClass(score: string, opponentScore: string) {
    if (score == null || opponentScore == null) return '';
    if (score === opponentScore) return ''; // tie no color
    return Number(score) > Number(opponentScore)
      ? 'text-success'
      : 'text-danger';
  }

  const { encode } = useEncodedRoute();
  const router = useRouter();
  function goToEvent() {
  const obj = {
    leagueId: props.match.league_id,
    homeId: props.match.home_id,
    awayId: props.match.away_id,
    date: props.match.date,
  };

  const encoded = encode(obj);

  router.push({ path: `/event/${encoded}` }); // use encoded object in URL
}
</script>

<style scoped>
  img {
    width: 32px;
    height: 32px;
    object-fit: contain;
  }
</style>
