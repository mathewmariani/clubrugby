<template>
  <h6>
    <span class="badge text-bg-danger venue-badge">{{ venue }}</span>
  </h6>
</template>

<script setup>
  defineProps({
    venue: String,
  });
</script>
