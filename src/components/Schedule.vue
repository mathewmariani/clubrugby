<template>
  <div>
    <div v-for="leagueId in filteredLeagueIds" :key="leagueId" class="mb-5">
      <h2>{{ leagues[leagueId] || leagueId }}</h2>

      <div v-if="scheduleByLeague[leagueId]?.length">
        <MatchCard
          v-for="match in scheduleByLeague[leagueId]"
          :key="match.date + '-' + match.home_id + '-' + match.away_id"
          :match="match"
          :clubs="clubs"
          :standings="{}"
        />
      </div>
      <div v-else>
        <p>No upcoming matches for this league.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { computed } from 'vue';
  import MatchCard from './MatchCard.vue';
  import { useSavedLeagues } from '../utils/useSavedLeagues';

  const props = defineProps({
    schedule: { type: Array, required: true },
    clubs: { type: Object, required: true },
    leagues: { type: Object, required: true },
  });

  const { savedLeagues } = useSavedLeagues();

  const leagueIds = computed(() => {
    const ids = new Set();
    props.schedule.forEach((m) => ids.add(m.league_id));
    return Array.from(ids);
  });

  const filteredLeagueIds = computed(() => {
    if (!savedLeagues.value.length) return [];
    return leagueIds.value.filter((id) => savedLeagues.value.includes(id));
  });

  const scheduleByLeague = computed(() => {
    const byLeague = {};
    for (const leagueId of filteredLeagueIds.value) {
      byLeague[leagueId] = props.schedule.filter(
        (m) => m.league_id === leagueId
      );
    }
    return byLeague;
  });
</script>
