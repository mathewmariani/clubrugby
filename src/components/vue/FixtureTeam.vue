<template>
  <div class="team-block d-flex flex-column align-items-center">
    <img
      :src="club?.logo"
      :alt="club?.name"
      width="64"
      height="64"
      class="image-fluid"
    />
    <div class="text-center text-wrap">
      {{ club.name || club.id || 'Unknown' }}
    </div>
  </div>
</template>

<script setup>
  defineProps({
    club: Object,
  });
</script>

<style scoped>
  .team-block {
    flex: 1;
    max-width: 33%;
    min-width: 0;
  }
</style>
