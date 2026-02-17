<template>
  <div class="d-flex gap-2">
    <router-link
      v-for="(title, index) in titles"
      :key="index"
      :to="resolvedRoutes[index]"
      class="btn btn-sm"
      :class="{ 'btn-primary': selectedIndex === index }"
      :ref="(el) => setButtonRef(el, index)"
    >
      {{ title }}
    </router-link>
  </div>
</template>

<script setup lang="ts">
  import { ref, watch, computed, type ComponentPublicInstance } from 'vue';
  import { useRoute, useRouter, type RouteLocationRaw } from 'vue-router';

  const props = defineProps<{
    titles: string[];
    routes: RouteLocationRaw[];
  }>();

  const tabButtons = ref<HTMLElement[]>([]);
  const route = useRoute();
  const router = useRouter();
  const selectedIndex = ref(0);

  // Precompute resolved hrefs for router-link
  const resolvedRoutes = computed(() =>
    props.routes.map((r) => router.resolve(r))
  );

  // Determine active tab based on route name & params
  watch(
    () => route.fullPath,
    () => {
      const idx = props.routes.findIndex((r) => {
        const resolved = router.resolve(r);
        return resolved.href === router.resolve(route.fullPath).href;
      });
      selectedIndex.value = idx >= 0 ? idx : 0;
    },
    { immediate: true }
  );

  const setButtonRef = (
    el: Element | ComponentPublicInstance | null,
    index: number
  ) => {
    if (el instanceof HTMLElement) tabButtons.value[index] = el;
  };
</script>
