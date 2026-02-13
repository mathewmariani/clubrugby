<template>
  <a
    class="list-group-item"
    :href="`${union.slug}/fixture/${fixture.fixtureId}`"
  >
    <div class="d-flex align-items-center gap-2 mb-1">
      <img v-if="home?.logo" :src="home.logo" :alt="home.name" />
      <!-- <small>{{ home?.name || 'Unknown' }}</small> -->
      <span class="text-body-emphasis fw-normal">{{
        home?.name || 'Unknown'
      }}</span>
      <strong :class="scoreClass(fixture.home.result)" class="ms-auto">{{
        props.fixture.home.score
      }}</strong>
    </div>
    <div class="d-flex align-items-center gap-2 mb-1">
      <img v-if="away?.logo" :src="away.logo" :alt="away.name" />
      <span class="text-body-emphasis fw-normal">{{
        away?.name || 'Unknown'
      }}</span>
      <strong :class="scoreClass(fixture.away.result)" class="ms-auto">{{
        props.fixture.away.score
      }}</strong>
    </div>
  </a>
</template>

<script setup lang="ts">
  import { computed } from 'vue';
  import type { Club, Fixture } from '@/utils/types';
  import { formattedTime } from '@/composables/utils';
  import { useAppData } from '@/composables/useAppData';

  const { union } = useAppData();

  const props = defineProps<{
    home: Club;
    away: Club;
    fixture: Fixture;
  }>();

  function scoreClass(result: string | null): string {
    if (result == null) return '';
    return result === 'win' ? 'text-success' : 'text-danger';
  }
</script>

<style scoped>
  img {
    width: 32px;
    height: 32px;
    object-fit: contain;
  }
</style>
