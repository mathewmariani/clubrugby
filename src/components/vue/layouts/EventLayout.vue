<template>
  <router-view :event-id="eventId" />
</template>

<script setup lang="ts">
  import { useRoute } from 'vue-router';

  const route = useRoute();
  const eventId = route.params.event_id;
</script>

<style scoped></style>
