<template>
  <div class="container py-4">
    <h1 class="mb-3">Standings: {{ union.slug.toUpperCase() }}</h1>
    <p>
      This is the Standings view for the
      <strong>{{ union.name }}</strong> union.
    </p>
  </div>

  <nav class="btn-group mb-4" role="group">
    <router-link to="/fixtures" class="btn btn-outline-primary">Fixtures</router-link>
    <router-link to="/results" class="btn btn-outline-primary">Results</router-link>
    <router-link to="/standings" class="btn btn-outline-primary">Standings</router-link>
    <button class="btn btn-outline-secondary" @click="goBack">← Back</button>
  </nav>
</template>

<script lang="ts" setup>
  import { type Union } from '../../utils/unions';
  import { useRouter } from 'vue-router'

const router = useRouter()
  defineProps<{
    union: Union;
  }>();

  function goBack() {
  if (window.history.length > 1) {
    router.back()
  } else {
    router.push('/standings')
  }
}
</script>
