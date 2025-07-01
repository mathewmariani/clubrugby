<template>
  <div class="list-group-item bg-body-tertiary sticky-match-header">
    <div class="d-flex justify-content-between align-items-center">
      <strong>{{ leagueName }}</strong>
      <span v-if="isResult" class="badge text-bg-secondary">FINAL</span>
      <span v-else class="badge text-bg-danger">{{ time }}</span>
    </div>
  </div>
</template>

<script setup lang="ts">
  defineProps<{
    leagueName: string;
    isResult: boolean;
    time?: string;
  }>();
</script>
