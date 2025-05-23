<template>
  <h6>
    <span class="badge text-bg-light venue-badge">{{ venue }}</span>
  </h6>
</template>

<script setup>
  defineProps({
    venue: String,
  });
</script>
