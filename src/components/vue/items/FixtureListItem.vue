<template>
  <!-- clickable event card -->
  <a class="list-group-item" @click.prevent="goToEvent">
    <!-- top info: venue and time -->
    <div class="d-flex justify-content-between w-100 mb-2">
      <small class="text-body-secondary">{{ match.venue }}</small>
      <div class="d-flex align-items-center gap-2">
        <small class="text-body-secondary">
          {{ formattedTime }}
          <span>❯</span>
        </small>
      </div>
    </div>

    <!-- home team -->
    <div class="d-flex align-items-center gap-2 mb-1">
      <img v-if="home?.logo" :src="home.logo" :alt="home.name" />
      <span class="text-body-emphasis fw-normal">
        {{ home?.name || 'Unknown' }}
      </span>
    </div>

    <!-- away team -->
    <div class="d-flex align-items-center gap-2 mb-1">
      <img v-if="away?.logo" :src="away.logo" :alt="away.name" />
      <span class="text-body-emphasis fw-normal">
        {{ away?.name || 'Unknown' }}
      </span>
    </div>
  </a>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';
import type { Club } from '@/utils/types';
import type { Fixture } from '@/utils/types';
import { computed } from 'vue';

const props = defineProps<{
  home: Club;
  away: Club;
  match: Fixture;
}>();

const router = useRouter();

// Convert unix timestamp to human-readable "h:mm a"
const formattedTime = computed(() => {
  if (!props.match.fixtureDate) return '';
  const date = new Date(props.match.fixtureDate * 1000);
  return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
});

// Navigate to the event page
function goToEvent() {
  router.push({ path: `/event/${props.match.fixtureId}` });
}
</script>

<style scoped>
img {
  width: 32px;
  height: 32px;
  object-fit: contain;
}
</style>
