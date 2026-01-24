<template>
  <div class="list-group-item">
    <div class="d-flex flex-column mt-3">
      <h6>Match Details</h6>
      <span class="text-muted">Date</span>
      <p>{{ date }}</p>
      <span class="text-muted">League</span>
      <p>{{ league }}</p>
      <template v-if="!isResult">
        <span class="text-muted">Venue</span>
        <p>{{ venue }}</p>
      </template>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { formattedDate } from '@/composables/utils';
  import { computed } from 'vue';

  const props = defineProps<{
    fixtureDate: number;
    league: string;
    venue: string;
    isResult: boolean;
  }>();

  const date = computed(() => formattedDate(props.fixtureDate));
</script>
