<script setup lang="ts">
  import { useRoute } from 'vue-router';

  const route = useRoute();
  const clubId = route.params.club_id;
</script>

<template>
  <div class="whatever">
    <router-view :club-id="clubId" />
  </div>
</template>

<style scoped>
</style>
