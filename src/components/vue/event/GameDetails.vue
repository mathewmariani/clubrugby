<template>
  <div class="list-group-item">
    <div class="d-flex flex-column mt-3">
      <h6>Game Details</h6>
      <span class="text-muted">Date</span>
      <p>{{ date }} {{ time }}</p>
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
    venue?: string;
    isResult: boolean;
  }>();
</script>
