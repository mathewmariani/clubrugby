<template>
  <nav
    ref="navbarRef"
    class="navbar bg-body-tertiary fixed-top border-bottom"
  >
    <div
      class="container-fluid d-flex align-items-center gap-2"
    >
      <!-- LEFT -->
      <div class="d-flex align-items-center gap-1">
        <slot name="left" />
      </div>

      <!-- TITLE -->
      <div class="navbar-brand text-truncate flex-grow-1 mb-0">
        <slot name="title">
          {{ defaultTitle }}
        </slot>
      </div>

      <!-- RIGHT -->
      <div class="d-flex align-items-center gap-1">
        <slot name="right" />
      </div>
    </div>

    <!-- TABS -->
    <div v-if="$slots.tabs" class="tabs-wrapper">
      <slot name="tabs" />
    </div>

    <OffcanvasNav />
  </nav>

  <!-- spacer -->
  <div :style="{ height: navbarHeight + 'px' }" />
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useLayout } from '@/composables/useLayout';
import OffcanvasNav from './OffcanvasNav.vue';

defineProps<{
  defaultTitle?: string;
}>();

const navbarRef = ref<HTMLElement | null>(null);
const { navbarHeight } = useLayout();

onMounted(() => {
  if (!navbarRef.value) return;

  const observer = new ResizeObserver(() => {
    navbarHeight.value = navbarRef.value!.offsetHeight;
  });

  observer.observe(navbarRef.value);
});
</script>

<style scoped>
.tabs-wrapper {
  overflow-x: auto;
  white-space: nowrap;
  -webkit-overflow-scrolling: touch;
}
</style>