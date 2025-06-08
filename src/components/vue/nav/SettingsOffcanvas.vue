<template>
  <div
    class="offcanvas offcanvas-end"
    id="settingsOffcanvas"
    tabindex="-1"
    ref="offcanvasRef"
  >
    <div class="offcanvas-header bg-white">
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="offcanvas"
        aria-label="Close"
      ></button>
    </div>
    <div class="offcanvas-body">
      <SettingsComponent :leagues="leagues" />
    </div>
  </div>
</template>

<script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import { Offcanvas } from 'bootstrap';
  import SettingsComponent from '../Settings.vue';
  import { type League } from '../../../utils/types.ts';

  const props = defineProps<{
    leagues: Record<string, League>;
  }>();

  const offcanvasRef = ref<HTMLElement | null>(null);

  onMounted(() => {
    if (offcanvasRef.value) new Offcanvas(offcanvasRef.value);
  });
</script>

<style scoped>
  .offcanvas.offcanvas-end {
    width: 75vw;
  }
</style>
