<template>
  <div style="display: contents">
    <Navbar :defaultTitle="`${leagueName} | ${union.slug.toUpperCase()}`">
      <template #left>
        <button
          class="btn btn-sm"
          data-bs-toggle="offcanvas"
          data-bs-target="#settingsOffcanvas"
        >
          <span class="navbar-toggler-icon" />
        </button>
      </template>

      <template #right>
        <ShareButton />
      </template>

      <template #tabs>
        <TabScroller
          :titles="['Fixtures', 'Results', 'Standings']"
          :routes="[
            `/league/${leagueId}/fixtures`,
            `/league/${leagueId}/results`,
            `/league/${leagueId}/standings`,
          ]"
        />
      </template>
    </Navbar>
    <router-view />
  </div>
</template>

<script setup lang="ts">
  import { computed } from 'vue';

  import Navbar from '@/components/vue/nav/Navbar.vue';
  import ShareButton from '@/components/vue/buttons/ShareButton.vue';
  import TabScroller from '@/components/vue/nav/TabScroller.vue';

  import { useAppData } from '@/composables/useAppData';
  const { union, leagues } = useAppData();

  const props = defineProps<{
    leagueId: string;
  }>();

  const leagueName = computed(() => leagues[props.leagueId] ?? 'Unknown');
</script>
