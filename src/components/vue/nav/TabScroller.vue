<template>
  <div ref="scrollContainer" class="info-tab-header">
    <button
      v-for="(title, index) in titles"
      :key="index"
      :class="['btn btn-sm', { 'btn-primary': selectedIndex === index }]"
      @click="$emit('select', index)"
      :ref="(el) => setButtonRef(el, index)"
    >
      {{ title }}
    </button>
  </div>
</template>

<script setup lang="ts">
  import { ref, watch, nextTick } from 'vue';

  const props = defineProps<{
    titles: string[];
    selectedIndex: number;
  }>();

  const emit = defineEmits<{
    (e: 'select', index: number): void;
  }>();

  const scrollContainer = ref<HTMLElement | null>(null);
  const tabButtons = ref<HTMLElement[]>([]);

  const setButtonRef = (el: HTMLElement | null, index: number) => {
    if (el) tabButtons.value[index] = el;
  };

  watch(
    () => props.selectedIndex,
    () => {
      nextTick(() => {
        const container = scrollContainer.value;
        const selected = tabButtons.value[props.selectedIndex];
        if (container && selected) {
          const containerWidth = container.offsetWidth;
          const selectedLeft = selected.offsetLeft;
          const selectedWidth = selected.offsetWidth;
          const scrollTo =
            selectedLeft - containerWidth / 2 + selectedWidth / 2;
          container.scrollTo({ left: scrollTo, behavior: 'smooth' });
        }
      });
    }
  );
</script>

<style scoped>
  .info-tab-header {
    display: flex;
    overflow-x: auto;
    padding: 0.5rem;
    scroll-behavior: smooth;
    white-space: nowrap;
    scrollbar-width: none;
  }
  .info-tab-header::-webkit-scrollbar {
    display: none;
  }
</style>
