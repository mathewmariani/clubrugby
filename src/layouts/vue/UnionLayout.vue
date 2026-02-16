<template>
  <div style="display: contents">
    <Navbar
      :defaultTitle="`${SITE_TITLE.toUpperCase()} | ${union.slug.toUpperCase()}`"
    >
      <template #left>
        <button
          class="btn btn-sm"
          data-bs-toggle="offcanvas"
          data-bs-target="#settingsOffcanvas"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
      </template>

      <template #right>
        <ShareButton />
      </template>

      <template #tabs>
        <TabScroller
          :titles="['Fixtures', 'Results', 'Standings']"
          :routes="[`/fixtures`, `/results`, `/standings`]"
        />
      </template>
    </Navbar>
    <router-view />
  </div>
</template>

<script setup lang="ts">
  import { SITE_TITLE } from '@/consts';
  import Navbar from '@/components/vue/nav/Navbar.vue';
  import ShareButton from '@/components/vue/buttons/ShareButton.vue';
  import TabScroller from '@/components/vue/nav/TabScroller.vue';

  import { useAppData } from '@/composables/useAppData';
  const { union } = useAppData();
</script>
