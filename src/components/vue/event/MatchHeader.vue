<template>
  <div class="sticky-match-header" :style="{ top: navbarHeight + 'px' }">
    <div class="list-group-header list-group-item bg-body-tertiary">
      <div class="d-flex justify-content-between align-items-center">
        {{ leagueName }}
        <span v-if="isResult" class="badge text-bg-secondary">FINAL</span>
        <span v-else class="badge text-bg-danger">{{ time }}</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { useLayout } from '@/composables/useLayout';
  const { navbarHeight } = useLayout();

  import { formattedTime } from '@/composables/utils';
  import { computed } from 'vue';


  const props = defineProps<{
    leagueName: string;
    isResult: boolean;
    fixtureDate: number;
  }>();

  const time = computed(() => formattedTime(props.fixtureDate));
</script>
