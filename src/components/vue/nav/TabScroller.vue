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
        selectedIndex.value = -1;
        return;
      }

      const idx = props.routes.findIndex((r) => r === path);
      selectedIndex.value = idx; // -1 means no match
    },
    { immediate: true }
  );

  const setButtonRef = (el: HTMLElement | null, index: number) => {
    if (el) tabButtons.value[index] = el;
  };
</script>
