<template>
  <div class="list-group-item">
    <div class="d-flex flex-column mt-3 mb-3">
      <h6>Box Score</h6>

      <!-- SCORE -->
      <div class="d-flex align-items-center py-1">
        <span class="fw-semibold">{{ home.score }}</span>
        <span class="flex-grow-1 text-center text-muted">SCORE</span>
        <span class="fw-semibold">{{ away.score }}</span>
      </div>

      <!-- CONVERSIONS -->
      <div class="d-flex align-items-center py-1">
        <span class="fw-semibold">{{ home.conv }}</span>
        <span class="flex-grow-1 text-center text-muted">CONVERSIONS</span>
        <span class="fw-semibold">{{ away.conv }}</span>
      </div>

      <!-- PENALTIES -->
      <div class="d-flex align-items-center py-1">
        <span class="fw-semibold">{{ home.pen }}</span>
        <span class="flex-grow-1 text-center text-muted">PENALTIES</span>
        <span class="fw-semibold">{{ away.pen }}</span>
      </div>

      <!-- DROP KICKS -->
      <div class="d-flex align-items-center py-1">
        <span class="fw-semibold">{{ home.drop }}</span>
        <span class="flex-grow-1 text-center text-muted">DROP KICKS</span>
        <span class="fw-semibold">{{ away.drop }}</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import type { FixtureResultSummary } from '@/utils/types';

  const props = defineProps<{
    home: FixtureResultSummary,
    away: FixtureResultSummary,
  }>();
</script>
