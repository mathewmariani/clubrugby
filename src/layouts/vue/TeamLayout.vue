<template>
  <div class="team-view-wrapper">
    <router-view v-slot="{ Component }">
      <transition name="slide" mode="out-in">
        <component :is="Component" :key="$route.fullPath" :club-id="clubId" />
      </transition>
    </router-view>
  </div>
</template>

<script setup lang="ts">
  import { useRoute } from 'vue-router';

  const route = useRoute();
  const clubId = route.params.club_id;
</script>

<style scoped></style>
