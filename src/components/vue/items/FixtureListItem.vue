<template>
  <!-- clickable event card -->
  <a class="list-group-item" @click.prevent="goToEvent">
    <!-- top info: venue and time -->
    <div class="d-flex justify-content-between w-100 mb-2">
      <small class="text-body-secondary">{{ fixture.venue }}</small>
      <div class="d-flex align-items-center gap-2">
        <small class="text-body-secondary">
          {{ time }}
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
import type { Club, Fixture } from '@/utils/types';
import { formattedTime } from '@/composables/utils';
import { computed } from 'vue';

const props = defineProps<{
  home: Club;
  away: Club;
  fixture: Fixture;
}>();


const time = computed(() => { return formattedTime(props.fixture.fixtureDate); });

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
