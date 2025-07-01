<template>
  <div class="list-group-item">
    <div class="d-flex flex-column mt-3">
      <h6>Match Details</h6>
      <span class="text-muted">Date</span>
      <p>{{ date }} {{ time }}</p>
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
  defineProps<{
    date: string;
    time: string;
    league: string
    venue?: string;
    isResult: boolean;
  }>();
</script>
