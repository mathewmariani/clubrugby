<template>
    <div v-if="isClient">
      <RouterView :union="union" />
    </div>
  </template>
  
  <script lang="ts" setup>
  import { ref, onMounted } from 'vue'
  import { createRouter, createWebHashHistory, RouterView } from 'vue-router'
  import { createApp, defineComponent, h } from 'vue'
  
  import Fixtures from './views/Fixtures.vue'
  import Results from './views/Results.vue'
  import Standings from './views/Standings.vue'
  
  const props = defineProps<{
    union: string
  }>()
  
  const isClient = ref(false)
  
  onMounted(() => {
    isClient.value = true
  
    const routes = [
      { path: '/', redirect: '/standings' },
      { path: '/fixtures', component: Fixtures, props: { union: props.union } },
      { path: '/results', component: Results, props: { union: props.union } },
      { path: '/standings', component: Standings, props: { union: props.union } },
    ]
  
    const router = createRouter({
      history: createWebHashHistory(),
      routes
    })
  
    const RootComponent = defineComponent({
      render: () => h(RouterView)
    })
  
    const app = createApp(RootComponent)
    app.use(router)
    app.mount('#app')
  })
  </script>
  