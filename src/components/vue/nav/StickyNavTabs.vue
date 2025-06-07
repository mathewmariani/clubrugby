<template>
  <!-- Fixed Top Navbar -->
  <nav class="navbar bg-white fixed-top border-bottom">
    <div class="container-fluid">
      <a class="navbar-brand" :href="`/${union.slug}`">
        {{ SITE_TITLE }} | {{ union.slug.toUpperCase() }}
      </a>
      <a class="btn" role="button" :href="`/${union.slug}/settings`">
        <span class="navbar-toggler-icon"></span>
      </a>
    </div>
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
  </nav>
</template>

<script setup lang="ts">
  import { ref, onMounted, nextTick, watch } from 'vue';
  import { type Union } from '../../../utils/unions.ts';

  import { SITE_TITLE } from '../../../consts.ts';

  const props = defineProps<{
    union: Union;
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
