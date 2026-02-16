<template>
  <div style="display: contents">
    <Navbar :defaultTitle="`${clubName} | ${union.slug.toUpperCase()}`">
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
          :titles="['Fixtures', 'Stats', 'Standings']"
          :routes="[
            `/club/${props.clubId}/fixtures`,
            `/club/${props.clubId}/stats`,
            `/club/${props.clubId}/standings`,
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
  const { union, clubs } = useAppData();

  const props = defineProps<{
    clubId: string;
  }>();

  const clubName = computed(() => clubs[props.clubId]?.name ?? 'Unknown');
</script>
