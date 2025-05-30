<template>
  <div class="card mb-3">
    <div class="card-body">
      <!-- Metadata row -->
      <div class="d-flex flex-wrap gap-2 mb-2">
        <span class="badge text-bg-light">{{ news.date }}</span>
        <span class="badge text-bg-light">{{ news.time }}</span>
        <span class="badge text-bg-light">{{ news.venue }}</span>
      </div>

      <!-- Headline -->
      <h5 class="card-title mb-0">{{ news.headline }}</h5>
    </div>
  </div>
</template>

<script setup>
  defineProps({
    news: { type: Object, required: true },
  });
</script>
