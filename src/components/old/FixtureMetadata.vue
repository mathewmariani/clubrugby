<template>
  <div class="d-flex flex-column text-center">
    <h4>
      <span class="badge text-bg-danger">{{ time }}</span>
    </h4>
    <h6>
      <span class="badge text-bg-light mb-2">{{ date }}</span>
    </h6>
  </div>
</template>

<script setup>
  defineProps({
    date: String,
    time: String,
  });
</script>
