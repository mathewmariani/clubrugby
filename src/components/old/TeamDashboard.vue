<template>
  <div v-if="teamId !== null && teamId !== ''">Were looking at a team</div>
  <div v-else>
    <p>No team ID specified in URL.</p>
  </div>
</template>

<script setup>
  import { onMounted, ref } from 'vue';

  const teamId = ref(null);

  onMounted(() => {
    const params = new URLSearchParams(window.location.search);
    teamId.value = params.get('id');
  });
</script>

<style scoped></style>
