<script setup lang="ts">
  import { useRoute } from 'vue-router';

  const route = useRoute();
  const eventId = route.params.event_id;
</script>

<template>
  <router-view :event-id="eventId" />
</template>

<style scoped></style>
