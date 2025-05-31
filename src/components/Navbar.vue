<template>
  <nav class="navbar bg-white fixed-top border-bottom">
    <div class="container-fluid">
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="offcanvas"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <a class="navbar-brand" href="/">{{ siteTitle }}</a>

      <div class="offcanvas offcanvas-start" id="navbarNav" tabindex="-1">
        <div class="offcanvas-header border-bottom bg-white sticky-top">
          <h5 class="offcanvas-title">{{ siteTitle }}</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="offcanvas"
            aria-label="Close"
          ></button>
        </div>
        <div class="offcanvas-body">
          <ul class="navbar-nav">
            <li class="nav-item" v-for="link in navLinks" :key="link.href">
              <a class="nav-link" :href="link.href">{{ link.label }}</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { Offcanvas } from 'bootstrap'
import { useFixedOffset } from '../composables/useFixedOffset'

defineProps({
  siteTitle: { type: String, default: 'My Site' },
})

const navLinks = [
  { label: 'Clubs', href: '/clubs' },
  { label: 'Fixtures', href: '/fixtures' },
  { label: 'Results', href: '/results' },
  { label: 'Standings', href: '/standings' },
  { label: 'Settings', href: '/settings' },
]

useFixedOffset()

onMounted(() => {
  const el = document.getElementById('navbarNav')
  if (el) new Offcanvas(el)
})
</script>

<style scoped>
#navbarNav.offcanvas-start {
  width: 65vw;
}
</style>
