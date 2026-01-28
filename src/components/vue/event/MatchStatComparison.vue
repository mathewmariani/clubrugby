<template>
  <div class="mb-3">
    <div class="d-flex justify-content-between mb-1">
      <small class="text-body-primary">
        {{ leftValue.toFixed(1) }}
        <small v-if="leftRank" class="text-body-secondary fw-light">
          ({{ leftRank }})
        </small>
      </small>

      <small class="text-body-secondary">{{ label }}</small>

      <small class="text-body-primary">
        <small v-if="rightRank" class="text-body-secondary fw-light">
          ({{ rightRank }})
        </small>
        {{ rightValue.toFixed(1) }}
      </small>
    </div>

    <!-- Bars -->
    <div v-if="showBars" class="progress-stacked">
      <div class="progress" :style="{ width: leftWidth + '%' }">
        <div class="progress-bar bg-primary"></div>
      </div>
      <div class="progress" :style="{ width: rightWidth + '%' }">
        <div class="progress-bar bg-warning"></div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { computed } from 'vue';

  const props = defineProps<{
    label: string;
    leftValue: number;
    rightValue: number;
    leftRank?: number;
    rightRank?: number;
    showBars?: boolean;
  }>();

  const total = computed(() => props.leftValue + props.rightValue);
  const leftWidth = computed(() =>
    total.value ? (props.leftValue / total.value) * 100 : 50
  );
  const rightWidth = computed(() => 100 - leftWidth.value);
</script>
