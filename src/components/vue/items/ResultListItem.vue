<template>
  <a class="list-group-item" @click.prevent="goToEvent">
    <div class="d-flex align-items-center gap-2 mb-1">
      <img v-if="home?.logo" :src="home.logo" :alt="home.name" />
      <!-- <small>{{ home?.name || 'Unknown' }}</small> -->
      <span class="text-body-emphasis fw-normal">{{
        home?.name || 'Unknown'
      }}</span>
      <strong
        :class="scoreClass(homeScore, awayScore)"
        class="ms-auto"
        >{{ homeScore }}</strong
      >
    </div>
    <div class="d-flex align-items-center gap-2 mb-1">
      <img v-if="away?.logo" :src="away.logo" :alt="away.name" />
      <span class="text-body-emphasis fw-normal">{{
        away?.name || 'Unknown'
      }}</span>
      <strong
        :class="scoreClass(awayScore, homeScore)"
        class="ms-auto"
        >{{ awayScore }}</strong
      >
    </div>
  </a>
</template>

<script setup lang="ts">
  import { useRouter } from 'vue-router';
  import type { Club, Fixture } from '@/utils/types';
  import { extractMainScore } from '@/composables/utils';
  import { computed } from 'vue';

  const props = defineProps<{
    home: Club;
    away: Club;
    fixture: Fixture;
  }>();

  const homeScore = computed(() => { return extractMainScore(props.fixture.home.score); });
  const awayScore = computed(() => { return extractMainScore(props.fixture.away.score); });

  function scoreClass(score: number, opponentScore: number) {
    if (score == null || opponentScore == null) return '';
    if (score === opponentScore) return ''; // tie no color
    return Number(score) > Number(opponentScore)
      ? 'text-success'
      : 'text-danger';
  }

  const router = useRouter();
  function goToEvent() {
    router.push({ path: `/fixture/${props.fixture.fixtureId}` });
  }
</script>

<style scoped>
  img {
    width: 32px;
    height: 32px;
    object-fit: contain;
  }
</style>
