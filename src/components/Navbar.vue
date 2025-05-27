<template>
  <!-- Fixed top navbar -->
  <nav class="navbar bg-light fixed-top shadow-sm">
    <div class="container-fluid">
      <!-- Offcanvas toggle button -->
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="offcanvas"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- Brand -->
      <a class="navbar-brand" href="/">{{ siteTitle }}</a>

      <!-- Offcanvas menu -->
      <div
        class="offcanvas offcanvas-start"
        tabindex="-1"
        id="navbarNav"
        aria-labelledby="navbarNavLabel"
      >
        <div
          class="offcanvas-header"
          style="position: sticky; top: 0; background-color: white; z-index: 1"
        >
          <h5 class="offcanvas-title" id="navbarNavLabel">{{ siteTitle }}</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="offcanvas"
            aria-label="Close"
          ></button>
        </div>
        <div class="offcanvas-body">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item" v-for="(link, index) in navLinks" :key="index">
              <h1><a class="nav-link" :href="link.href">{{ link.label }}</a></h1>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { onMounted } from 'vue';
import { Offcanvas } from 'bootstrap';

// Props
defineProps({
  siteTitle: {
    type: String,
    default: 'My Site',
  },
});

// Navigation links
const navLinks = [
  { label: 'Clubs', href: '/clubs' },
  { label: 'Fixtures', href: '/schedule' },
  { label: 'Results', href: '/results' },
  { label: 'Standings', href: '/standings' },
  { label: 'Settings', href: '/settings' },
];

// Manually initialize offcanvas to ensure it works after navigation
onMounted(() => {
  const offcanvasEl = document.getElementById('navbarNav');
  if (offcanvasEl) {
    new Offcanvas(offcanvasEl);
  }
});
</script>

<style scoped>
.offcanvas {
  max-width: 75%;
}
</style>
