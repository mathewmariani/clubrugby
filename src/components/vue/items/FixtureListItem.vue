<template>
  <!-- make this an href to a stats page -->
  <a class="list-group-item" @click="emit('click', match)">
    <div class="d-flex justify-content-between w-100 mb-2">
      <small class="text-muted">{{ match.venue }}</small>
      <span class="badge text-bg-danger">
        {{ match.time }}
      </span>
    </div>
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
    </div>
  </a>
</template>

<script setup lang="ts">
  import { toRef } from 'vue';
  import type { Club, League, Fixture } from '../../../utils/types';
  import { useMatchClubs } from '../../../composables/utils';

  const props = defineProps<{
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
    match: Fixture;
  }>();

  const emit = defineEmits<{
    (e: 'click', match: Fixture): void;
  }>();

  const { home, away } = useMatchClubs(toRef(props, 'match'), props.clubs);
</script>

<style scoped></style>
