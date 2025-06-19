<template>
  <div ref="scrollContainer" class="info-tab-header">
    <router-link
      v-for="(title, index) in titles"
      :key="index"
      :to="routes[index]"
      class="btn btn-sm"
      :class="{ 'btn-primary': selectedIndex === index }"
      :ref="(el) => setButtonRef(el, index)"
    >
      {{ title }}
    </router-link>
  </div>
</template>

<script setup lang="ts">
  import { ref, watch, nextTick } from 'vue';
  import { useRoute } from 'vue-router';

  const props = defineProps<{
    titles: string[];
    routes: string[];
  }>();

  const scrollContainer = ref<HTMLElement | null>(null);
  const tabButtons = ref<HTMLElement[]>([]);
  const route = useRoute();

  const selectedIndex = ref(0);

  // Determine active route
  watch(
    () => route.path,
    (path) => {
      if (!props.routes || !Array.isArray(props.routes)) {
        // fallback if routes isn't provided: default to index 1 (fixtures)
        selectedIndex.value = 1;
        return;
      }

      const idx = props.routes.findIndex((r) => r === path);

      // If no match found, default to /fixtures index (assuming it's at 1)
      selectedIndex.value = idx !== -1 ? idx : 1;
    },
    { immediate: true }
  );

  const setButtonRef = (el: HTMLElement | null, index: number) => {
    if (el) tabButtons.value[index] = el;
  };
</script>
