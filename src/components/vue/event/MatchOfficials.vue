<template>
  <div class="list-group-item">
    <div class="d-flex flex-column mt-3">
      <h6>Match Officals</h6>
      <template v-for="official in matchOfficial" :key="official.role">
        <span class="text-muted">{{ official.role }}</span>
        <p>{{ official.name }}</p>
      </template>
    </div>
  </div>
</template>

<script setup lang="ts">
  import type { MatchOfficial } from '@/utils/types';

  const props = defineProps<{
    matchOfficial: MatchOfficial[],
  }>();
</script>
