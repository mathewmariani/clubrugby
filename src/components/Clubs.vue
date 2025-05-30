<template>
  <div class="row row-cols-1 row-cols-md-2 g-4">
    <div v-for="club in clubList" :key="club.id" class="col">
      <div class="card">
        <div class="card-body d-flex flex-row align-items-center p-2">
          <img
            :src="club.logo"
            :alt="club.name"
            class="me-3"
            style="width: 64px; height: 64px; object-fit: contain"
          />
          <h5 class="card-title mb-0">{{ club.name }}</h5>
        </div>
        <div class="card-footer">
          <a :href="info[teamId]?.url" class="card-link">Website</a>
          <a :href="'mailto:' + info[teamId]?.email" class="card-link">Email</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { computed } from 'vue';
  const props = defineProps({
    clubs: { type: Object, required: true },
    info: { type: Object, required: true },
  });

  const clubList = computed(() => Object.values(props.clubs));
</script>
