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

      <a class="navbar-brand" :href="`/${federation.slug}`"
        >{{ title }} | {{ federation.slug.toUpperCase() }}</a
      >

      <div class="offcanvas offcanvas-start" id="navbarNav" tabindex="-1">
        <div class="offcanvas-header bg-white sticky-top">
          <a class="navbar-brand" href="/">{{ title }}</a>
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
  import { onMounted } from 'vue';
  import { Offcanvas } from 'bootstrap';
  import { useFixedOffset } from '../../composables/useFixedOffset';
  import { type Federation } from '../../federations.ts';

  const props = defineProps<{
    title: string;
    federation: Federation;
  }>();

  const baseLinks = [
    { label: 'Clubs', href: '/clubs' },
    { label: 'Fixtures', href: '/fixtures' },
    { label: 'Results', href: '/results' },
    { label: 'Standings', href: '/standings' },
  ];

  const navLinks = baseLinks.map((link) => ({
    ...link,
    href: `/${props.federation.slug}${link.href}`,
  }));

  useFixedOffset();

  onMounted(() => {
    const el = document.getElementById('navbarNav');
    if (el) new Offcanvas(el);
  });
</script>

<style scoped>
  #navbarNav.offcanvas-start {
    width: 65vw;
  }
</style>
