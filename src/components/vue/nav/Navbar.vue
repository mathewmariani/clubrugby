<template>
  <nav ref="navbarRef" class="navbar bg-body-tertiary fixed-top border-bottom">
    <div class="container-fluid d-flex flex-nowrap align-items-center">
      <!-- Left -->
      <component v-if="nav.left" :is="nav.left" />

      <!-- Title -->
      <div class="navbar-brand flex-grow-1 text-truncate">
        {{ $props.title }}
      </div>

      <!-- Right -->
      <component v-if="nav.right" :is="nav.right" />
    </div>

    <!-- Tabs row (optional) -->
    <div
      v-if="nav.tabs"
      class="container-fluid d-flex align-items-center gap-2 mt-1"
    >
      <TabScroller :titles="nav.tabs.titles" :routes="nav.tabs.routes" />
    </div>

    <!-- Offcanvas -->
    <OffcanvasNav />
  </nav>

  <!-- spacer -->
  <div :style="{ height: navbarHeight + 'px' }"></div>
</template>

<script setup lang="ts">
  import { computed, onMounted, ref } from 'vue';
  import { useRoute } from 'vue-router';
  import { useLayout } from '@/composables/useLayout';
  import TabScroller from '@/components/vue/nav/TabScroller.vue';
  import OffcanvasNav from '@/components/vue/nav/OffcanvasNav.vue';

  const route = useRoute();

  const props = defineProps({
    title: String,
  });

  const nav = computed(() => {
    const meta = route.meta.nav;

    if (!meta) return {};

    return typeof meta === 'function' ? meta(route) : meta;
  });

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
  .brand {
    padding-top: var(--bs-navbar-brand-padding-y);
    padding-bottom: var(--bs-navbar-brand-padding-y);
    margin-right: var(--bs-navbar-brand-margin-end);
    font-size: var(--bs-navbar-brand-font-size);
    color: var(--bs-navbar-brand-color);
    text-decoration: none;
    white-space: nowrap;
  }
</style>
