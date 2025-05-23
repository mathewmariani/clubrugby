<template>
  <div class="row row-cols-1 row-cols-md-2 g-4">
    <div v-for="club in clubList" :key="club.id" class="col">
      <div class="card d-flex flex-row align-items-center p-2">
        <img
          :src="club.logo"
          :alt="club.name"
          class="me-3"
          style="width: 64px; height: 64px; object-fit: contain"
        />
        <div class="card-body p-0">
          <h5 class="card-title mb-0">{{ club.name }}</h5>
          <a :href="`dashboard.html?id=${club.id}`">Dashboard</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { computed } from 'vue';
  const props = defineProps({
    clubs: { type: Object, required: true },
  });

  const clubList = computed(() => Object.values(props.clubs));
</script>
