<template>
  <div
    ref="scrollContainer"
    class="info-tab-header full-width-breakout bg-white border-bottom"
  >
    <button
      v-for="(title, index) in titles"
      :key="index"
      :class="['info-tab-button', { active: selectedIndex === index }]"
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
  .full-width-breakout {
    width: 100vw;
    position: relative;
    left: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    z-index: 1;
  }

  .info-tab-header {
    display: flex;
    overflow-x: auto;
    gap: 0.5rem;
    padding: 0.5rem;
    scroll-behavior: smooth;
    white-space: nowrap;
    scrollbar-width: none;
    scroll-padding-left: 50%;
    scroll-padding-right: 50%;
  }
  .info-tab-header::-webkit-scrollbar {
    display: none;
  }

  .info-tab-button {
    padding: 8px 14px;
    border: none;
    border-radius: 20px;
    background: rgba(0, 0, 0, 0.1);
    font-size: 14px;
    cursor: pointer;
    flex-shrink: 0;
    transition: 0.2s;
  }

  .info-tab-button.active {
    background: #007aff;
    color: white;
    font-weight: bold;
  }
</style>
