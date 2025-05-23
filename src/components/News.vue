<template>
  <div>
    <div v-for="leagueId in filteredLeagueIds" :key="leagueId" class="mb-5">
      <h2>{{ leagues[leagueId] || leagueId }}</h2>

      <div v-if="newsByLeague[leagueId]?.length">
        <NewsCard
          v-for="(item, index) in newsByLeague[leagueId]"
          :key="index"
          :news="item"
          :league-name="leagues[leagueId] || leagueId"
        />
      </div>
      <div v-else>
        <p>No news available for this league.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { computed } from 'vue';
  import NewsCard from './NewsCard.vue';

  const props = defineProps({
    news: { type: Array, required: true },
    leagues: { type: Object, required: true },
  });

  const leagueIds = computed(() => {
    const ids = new Set();
    props.news.forEach((n) => ids.add(n.league_id));
    return Array.from(ids);
  });

  const filteredLeagueIds = computed(() => {
    // You can filter leagues here if you want; for now, show all with news
    return leagueIds.value;
  });

  const newsByLeague = computed(() => {
    const byLeague = {};
    for (const leagueId of filteredLeagueIds.value) {
      byLeague[leagueId] = props.news.filter((n) => n.league_id === leagueId);
    }
    return byLeague;
  });
</script>
