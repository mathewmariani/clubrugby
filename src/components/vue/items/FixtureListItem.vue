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
      <img
        v-if="home?.logo_url"
        :src="home.logo_url"
        :alt="home.name"
        width="32"
        height="32"
        style="object-fit: contain"
      />
      <span class="text-body-emphasis fw-normal">{{ home?.name || 'Unknown' }}</span>
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
      <span class="text-body-emphasis fw-normal">{{ away?.name || 'Unknown' }}</span>
    </div>
  </a>
</template>

<script setup lang="ts">
  import { toRef } from 'vue';
  import { useRouter } from 'vue-router';
  import type { Club, League, Fixture } from '../../../utils/types';
  import { useMatchClubs } from '../../../composables/utils';

  const props = defineProps<{
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
    match: Fixture;
  }>();

  const { home, away } = useMatchClubs(toRef(props, 'match'), props.clubs);

  const router = useRouter();

  function goToEvent() {
    const id = `${props.match.league_id}-${props.match.home_id}-${props.match.away_id}-${props.match.date}`;
    router.push({ path: `/event/${id}` });
  }
</script>
