<template>
  <nav class="navbar navbar-expand-lg navbar bg-light">
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
            <a class="nav-link" :href="link.href" @click="closeNavbar">{{
              link.label
            }}</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
  import { ref, onMounted } from 'vue';
  import { Collapse } from 'bootstrap'; // ✅ Import only Collapse class

  // Props
  defineProps({
    siteTitle: {
      type: String,
      default: 'My Site',
    },
  });

  // Navbar links
  const navLinks = [
    { label: 'Clubs', href: '/clubs' },
    { label: 'Fixtures', href: '/schedule' },
    { label: 'Results', href: '/results' },
    { label: 'Standings', href: '/standings' },
    { label: 'Settings', href: '/settings' },
  ];

  // Bootstrap collapse control
  const navbarCollapse = ref(null);
  let collapseInstance = null;

  onMounted(() => {
    collapseInstance = Collapse.getOrCreateInstance(navbarCollapse.value);
  });

  const closeNavbar = () => {
    if (collapseInstance && navbarCollapse.value.classList.contains('show')) {
      collapseInstance.hide();
    }
  };
</script>
