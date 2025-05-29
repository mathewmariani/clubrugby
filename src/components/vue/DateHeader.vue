<template>
  <div ref="scrollContainer" class="date-header">
    <button
      v-for="(date, index) in dates"
      :key="index"
      :class="['date-button', { active: selectedIndex === index }]"
      @click="$emit('select', index)"
      :ref="(el) => setButtonRef(el, index)"
    >
      {{ formatDate(date) }}
    </button>
  </div>
</template>

<script setup>
  import { ref, watch, nextTick } from 'vue';

  const props = defineProps({
    dates: { type: Array, required: true },
    selectedIndex: { type: Number, required: true },
  });

  const emit = defineEmits(['select']);

  const scrollContainer = ref(null);
  const dateButtons = ref([]);

  const setButtonRef = (el, index) => {
    if (el) dateButtons.value[index] = el;
  };

  // center selected button when selectedIndex changes
  watch(
    () => props.selectedIndex,
    () => {
      nextTick(() => {
        const container = scrollContainer.value;
        const selected = dateButtons.value[props.selectedIndex];
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

  function formatDate(iso) {
    const [year, month, day] = iso.split('-').map(Number);
    const date = new Date(year, month - 1, day);
    return date.toLocaleDateString('en-US', {
      weekday: 'short',
      month: 'short',
      day: '2-digit',
    });
  }
</script>

<style scoped>
  .date-header {
    display: flex;
    overflow-x: auto;
    gap: 0.5rem;
    padding: 0.5rem 0;
    margin-bottom: 1rem;
    scroll-behavior: smooth;
    white-space: nowrap;
    scrollbar-width: none;
    scroll-padding-left: 50%;
    scroll-padding-right: 50%;
  }
  .date-header::-webkit-scrollbar {
    display: none;
  }
  .date-button {
    padding: 8px 14px;
    border: none;
    border-radius: 20px;
    background: rgba(0, 0, 0, 0.1);
    font-size: 14px;
    cursor: pointer;
    flex-shrink: 0;
    transition: 0.2s;
  }
  .date-button.active {
    background: #007aff;
    color: white;
    font-weight: bold;
  }
</style>
