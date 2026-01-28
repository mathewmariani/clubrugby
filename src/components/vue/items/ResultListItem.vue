<template>
  <a class="list-group-item" @click.prevent="goToEvent">
    <div class="d-flex align-items-center gap-2 mb-1">
      <img v-if="home?.logo" :src="home.logo" :alt="home.name" />
      <!-- <small>{{ home?.name || 'Unknown' }}</small> -->
      <span class="text-body-emphasis fw-normal">{{
        home?.name || 'Unknown'
      }}</span>
      <strong
        :class="scoreClass(fixture.home.result)"
        class="ms-auto"
        >{{ props.fixture.home.score }}</strong
      >
    </div>
    <div class="d-flex align-items-center gap-2 mb-1">
      <img v-if="away?.logo" :src="away.logo" :alt="away.name" />
      <span class="text-body-emphasis fw-normal">{{
        away?.name || 'Unknown'
      }}</span>
      <strong
        :class="scoreClass(fixture.away.result)"
        class="ms-auto"
        >{{ props.fixture.away.score }}</strong
      >
    </div>
  </a>
</template>

<script setup lang="ts">
  import { useRouter } from 'vue-router';
  import type { Club, Fixture } from '@/utils/types';

  const props = defineProps<{
    home: Club;
    away: Club;
    fixture: Fixture;
  }>();

  function scoreClass(result: string | null): string {
    if (result == null) return '';
    return result === 'win' ? 'text-success' : 'text-danger';
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
