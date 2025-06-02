<template>
  <div class="row row-cols-1 mt-3 gap-3">
    <div v-for="club in clubList" :key="club.id" class="col">
      <div class="card">
        <div class="card-body d-flex flex-row align-items-center p-2">
          <img
            :src="club.logo_url"
            :alt="club.name"
            class="me-3"
            style="width: 64px; height: 64px; object-fit: contain"
          />
          <h5 class="card-title mb-0">{{ club.name }}</h5>
        </div>
        <div class="card-footer">
          <!-- <a
            :href="infoMap[club.id]?.url"
            class="btn btn-link"
            :class="{ disabled: !infoMap[club.id]?.url }"
            >Website</a
          > -->
          <!-- <a
            :href="vendor[club.id]?.instagram"
            class="btn btn-link"
            :class="{ disabled: !vendor[club.id]?.instagram }"
            >Instagram</a
          > -->
          <!-- <a
            :href="vendor[club.id]?.facebook"
            class="btn btn-link"
            :class="{ disabled: !vendor[club.id]?.facebook }"
            >Facebook</a
          > -->
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { computed } from 'vue';
  const props = defineProps({
    clubs: { type: Object, required: true },
    // info: { type: Object, required: true },
    // vendor: { type: Object, required: true },
  });

  // can be composable
  const clubList = computed(() => Object.values(props.clubs));
  const infoMap = computed(() => {
    return Object.values(props.info).reduce((acc, item) => {
      acc[item.id] = item;
      return acc;
    }, {});
  });
</script>
