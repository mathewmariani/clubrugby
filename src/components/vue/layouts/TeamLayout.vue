<script setup lang="ts">
  import { useRoute } from 'vue-router';

  const route = useRoute();
  const clubId = route.params.club_id;
</script>

<template>
  <router-view :club-id="clubId" />
</template>

<style scoped></style>
