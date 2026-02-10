<template>
  <div
    class="offcanvas offcanvas-start"
    id="settingsOffcanvas"
    tabindex="-1"
    ref="offcanvasRef"
  >
    <div class="offcanvas-header">
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="offcanvas"
        aria-label="Close"
      ></button>
    </div>
    <div class="offcanvas-body">
      <SettingsComponent />
    </div>
  </div>
</template>

<script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import SettingsComponent from './Settings.vue';

  const offcanvasRef = ref<HTMLElement | null>(null);

  onMounted(async () => {
    const { Offcanvas } = await import('bootstrap');
    if (offcanvasRef.value) {
      new Offcanvas(offcanvasRef.value);
    }
  });
</script>

<style scoped>
  .offcanvas.offcanvas-start {
    width: 75vw;
  }
</style>
