<template>
  <div
    class="sticky list-group-header list-group-item"
    :style="{ top: navbarHeight + 'px' }"
  >
    {{ str }}
  </div>
</template>

<script setup lang="ts">
  import { useLayout } from '@/composables/useLayout';

  const props = defineProps<{
    str: string;
  }>();

  const { navbarHeight } = useLayout();
  const dateHeaderHeight = 32;

  //   const leagueTopOffset = computed(() => navbarHeight.value + dateHeaderHeight);
</script>
