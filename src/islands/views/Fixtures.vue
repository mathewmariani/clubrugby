<template>
  <div class="container py-4">
    <h1 class="mb-3">Fixtures: {{ union.slug.toUpperCase() }}</h1>
    <p>
      This is the Fixtures view for the <strong>{{ union.name }}</strong> union.
    </p>
  </div>

  <nav class="btn-group mb-4" role="group">
    <router-link to="/fixtures" class="btn btn-outline-primary">Fixtures</router-link>
    <router-link to="/results" class="btn btn-outline-primary">Results</router-link>
    <router-link to="/standings" class="btn btn-outline-primary">Standings</router-link>
  </nav>
</template>

<script lang="ts" setup>
  import { type Union } from '../../utils/unions';
  defineProps<{
    union: Union;
  }>();
</script>
