<template>
  <nav class="navbar bg-white fixed-top border-bottom">
    <div class="container-fluid">
      <a class="navbar-brand" :href="`/${federation.slug}`"
        >{{ title }} | {{ federation.slug.toUpperCase() }}</a
      >
    </div>
  </nav>
</template>

<script setup lang="ts">
  import { type Union } from '../../utils/unions.ts';

  const props = defineProps<{
    title: string;
    federation: Union;
  }>();
</script>

<style scoped>
  #navbarNav.offcanvas-start {
    width: 65vw;
  }
</style>
