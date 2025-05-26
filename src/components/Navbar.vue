<template>
  <nav class="navbar navbar-expand-lg bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="/">{{ siteTitle }}</a>

      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav" ref="navbarCollapse">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item" v-for="(link, index) in navLinks" :key="index">
            <a class="nav-link" :href="link.href">
              {{ link.label }}
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue';
import { Collapse } from 'bootstrap';

defineProps({
  siteTitle: {
    type: String,
    default: 'My Site',
  },
});

const navLinks = [
  { label: 'Clubs', href: '/clubs' },
  { label: 'Fixtures', href: '/schedule' },
  { label: 'Results', href: '/results' },
  { label: 'Standings', href: '/standings' },
  { label: 'Settings', href: '/settings' },
];

</script>
