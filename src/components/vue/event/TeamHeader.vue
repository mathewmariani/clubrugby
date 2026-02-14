<template>
  <div class="list-group-item">
    <template v-if="isResult">
      <div class="d-flex align-items-center justify-content-between my-3">
        <a v-if="home && homeHref" :href="homeHref">
          <img :src="home.logo" alt="" />
        </a>

        <EventScore :home="homeSummary.score" :away="awaySummary.score" />

        <a v-if="away && awayHref" :href="awayHref">
          <img :src="away.logo" alt="" />
        </a>
      </div>
    </template>

    <template v-else>
      <div class="d-flex gap-3 my-3">
        <a v-if="home && homeHref" :href="homeHref">
          <img :src="home.logo" alt="" />
        </a>

        <div class="d-flex flex-column justify-content-center">
          <h6>{{ home?.name }}</h6>
        </div>
      </div>

      <div class="d-flex gap-3 mb-3 my-3">
        <a v-if="away && awayHref" :href="awayHref">
          <img :src="away.logo" alt="" />
        </a>

        <div class="d-flex flex-column justify-content-center">
          <h6>{{ away?.name }}</h6>
        </div>
      </div>
    </template>
  </div>
</template>

<script setup lang="ts">
  import { computed } from 'vue';
  import type { Club, FixtureResultSummary } from '@/utils/types';
  import EventScore from './EventScore.vue';

  const props = defineProps<{
    home?: Club;
    away?: Club;
    isResult: boolean;
    homeSummary: FixtureResultSummary;
    awaySummary: FixtureResultSummary;
  }>();

  const homeHref = computed(() =>
    props.homeSummary?.club_id
      ? `/qc/club/${props.homeSummary.club_id}`
      : undefined
  );

  const awayHref = computed(() =>
    props.awaySummary?.club_id
      ? `/qc/club/${props.awaySummary.club_id}`
      : undefined
  );
</script>

<style scoped>
  img {
    width: 64px;
    height: 64px;
    object-fit: contain;
  }

  a {
    text-decoration: none;
    color: inherit;
  }
</style>
