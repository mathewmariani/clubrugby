<template>
  <a class="list-group-item" @click.prevent="goToEvent">
    <div class="d-flex align-items-center gap-2 mb-1">
      <img v-if="home?.logo" :src="home.logo" :alt="home.name" />
      <!-- <small>{{ home?.name || 'Unknown' }}</small> -->
      <span class="text-body-emphasis fw-normal">{{
        home?.name || 'Unknown'
      }}</span>
      <strong
        :class="scoreClass(match.homeScore, match.awayScore)"
        class="ms-auto"
        >{{ match.homeScore || 'Unknown' }}</strong
      >
    </div>
    <div class="d-flex align-items-center gap-2 mb-1">
      <img v-if="away?.logo" :src="away.logo" :alt="away.name" />
      <span class="text-body-emphasis fw-normal">{{
        away?.name || 'Unknown'
      }}</span>
      <strong
        :class="scoreClass(match.awayScore, match.homeScore)"
        class="ms-auto"
        >{{ match.awayScore || 'Unknown' }}</strong
      >
    </div>
  </a>
</template>

<script setup lang="ts">
  import { useRouter } from 'vue-router';
  import type { Club, Fixture } from '@/utils/types';
  import { useEncodedRoute } from "@/composables/useEncodedRoute";

  const props = defineProps<{
    home: Club;
    away: Club;
    match: Fixture;
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
    homeId: props.match.homeClubId,
    awayId: props.match.awayClubId,
    date: props.match.fixtureDate,
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
