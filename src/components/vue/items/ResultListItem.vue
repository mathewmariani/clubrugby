<template>
  <a class="list-group-item">
    <div class="d-flex align-items-center gap-2 mb-1">
      <img
        v-if="home?.logo_url"
        :src="home.logo_url"
        :alt="home.name"
        width="32"
        height="32"
        style="object-fit: contain"
      />
      <small>{{ home?.name || 'Unknown' }}</small>
      <strong
        :class="scoreClass(match.home_score, match.away_score)"
        class="ms-auto"
        >{{ match.home_score || 'Unknown' }}</strong
      >
    </div>
    <div class="d-flex align-items-center gap-2 mb-1">
      <img
        v-if="away?.logo_url"
        :src="away.logo_url"
        :alt="away.name"
        width="32"
        height="32"
        style="object-fit: contain"
      />
      <small>{{ away?.name || 'Unknown' }}</small>
      <strong
        :class="scoreClass(match.away_score, match.home_score)"
        class="ms-auto"
        >{{ match.away_score || 'Unknown' }}</strong
      >
    </div>
  </a>
</template>

<script setup lang="ts">
  import { toRef } from 'vue';
  import type { Club, League, Result } from '../../../utils/types';
  import { useMatchClubs } from '../../../composables/utils';

  const props = defineProps<{
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
    match: Result;
  }>();

  const { home, away } = useMatchClubs(toRef(props, 'match'), props.clubs);

  function scoreClass(score: string, opponentScore: string) {
    if (score == null || opponentScore == null) return '';
    if (score === opponentScore) return ''; // tie no color
    return Number(score) > Number(opponentScore)
      ? 'text-success'
      : 'text-danger';
  }
</script>

<style scoped></style>
