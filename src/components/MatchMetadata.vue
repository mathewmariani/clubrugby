<template>
  <div>
    <span class="badge text-bg-light">{{ date }}</span>
    <span class="badge text-bg-light">{{ time }}</span>
  </div>
</template>

<script setup>
  defineProps({
    date: String,
    time: String,
  });
</script>
