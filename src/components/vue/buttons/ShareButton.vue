<template>
  <button class="btn" type="button"  @click="handleShare">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="1.5rem"
      height="1.5rem"
      fill="currentColor"
      class="share-icon bi bi-box-arrow-up"
      viewBox="0 0 16 16"
    >
      <path
        fill-rule="evenodd"
        d="M3.5 6a.5.5 0 0 0-.5.5v8a.5.5 0 0 0 .5.5h9a.5.5 0 0 0 .5-.5v-8a.5.5 0 0 0-.5-.5h-2a.5.5 0 0 1 0-1h2A1.5 1.5 0 0 1 14 6.5v8a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 14.5v-8A1.5 1.5 0 0 1 3.5 5h2a.5.5 0 0 1 0 1z"
      />
      <path
        fill-rule="evenodd"
        d="M7.646.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 1.707V10.5a.5.5 0 0 1-1 0V1.707L5.354 3.854a.5.5 0 1 1-.708-.708z"
      />
    </svg>
  </button>
</template>

<script setup lang="ts">
  import { useRoute } from 'vue-router';
  import { useAppData } from '@/composables/useAppData';

  const route = useRoute();
  const { clubs, leagues } = useAppData();

  function handleShare() {
    if (!navigator.share) return;

    let title = 'Check this out!';

    // Fixture page
    if (
      route.name?.toString().startsWith('fixture') &&
      route.params.fixtureId
    ) {
      const home = (route.params.homeName as string) || 'Home';
      const away = (route.params.awayName as string) || 'Away';
      title = `${home} vs ${away}`;
    }
    // Club page
    else {
      const clubId = Array.isArray(route.params.clubId)
        ? route.params.clubId[0]
        : route.params.clubId;
      if (clubId && clubs[clubId]) {
        title = `Club ${clubs[clubId].name}`;
      }

      const leagueId = Array.isArray(route.params.leagueId)
        ? route.params.leagueId[0]
        : route.params.leagueId;
      if (leagueId && leagues[leagueId]) {
        title = `League ${leagues[leagueId]}`;
      }
    }

    navigator
      .share({
        url: window.location.href,
        title,
        text: 'Check out this page!',
      })
      .catch(() => console.log('Share failed'));
  }
</script>