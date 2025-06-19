<script setup lang="ts">
  import { useRoute } from 'vue-router';

  const route = useRoute();
  const clubId = route.params.club_id;
  // use `clubId` to show standings, stats, per game averages
</script>

<template>
  <div class="container mt-4">
    <h4 class="mb-3">Team Stats</h4>
    <!-- Use tables, per-game stat comparisons, rankings -->
  </div>
</template>
