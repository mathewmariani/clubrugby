<template>
  <nav ref="navbarRef" class="navbar bg-body-tertiary fixed-top border-bottom">
    <div class="container-fluid d-flex align-items-center gap-2">
      <!-- Left slot (optional) -->
      <component v-if="nav.left" :is="nav.left" />

      <!-- Title -->
      <div class="navbar-brand flex-grow-1 text-truncate">
        {{ $props.title }}
      </div>

      <!-- Right slot (optional) -->
      <component v-if="nav.right" :is="nav.right" />
    </div>

    <!-- Tabs slot (optional) -->
    <div
      class="container-fluid d-flex align-items-center gap-2"
      v-if="nav.tabs"
    >
      <TabScroller :titles="nav.tabs.titles" :routes="nav.tabs.routes" />
    </div>

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