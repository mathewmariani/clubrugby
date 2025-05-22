<template>
  <div v-if="Object.keys(filteredGroupedByLeague).length">
    <div v-for="(dates, leagueId) in filteredGroupedByLeague" :key="leagueId" class="mb-5">
      <h2>{{ leagues[leagueId] || leagueId }}</h2>

      <div v-for="(matches, date) in dates" :key="date" class="mb-4">
        <h4>{{ formatDate(date) }}</h4>
        <div class="row row-cols-1 row-cols-md-2 g-4">
          <div v-for="match in matches" :key="match.id || (match.date + match.home_id + match.away_id)" class="col">
            <ResultCard :match="match" :clubs="clubs" />
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-else>
    <p>Loading results...</p>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import ResultCard from './ResultCard.vue';
import { useSavedLeagues } from '../utils/useSavedLeagues';

const props = defineProps({
  results: { type: Array, required: true },
  clubs: { type: Object, required: true },
  leagues: { type: Object, required: true },
});

const { savedLeagues } = useSavedLeagues();

const groupedByLeague = computed(() => {
  const grouped = {};
  props.results.forEach(match => {
    if (!match.league_id || !match.date) return;

    if (!grouped[match.league_id]) grouped[match.league_id] = {};
    if (!grouped[match.league_id][match.date]) grouped[match.league_id][match.date] = [];

    grouped[match.league_id][match.date].push(match);
  });

  // Sort dates ascending within each league
  Object.keys(grouped).forEach(leagueId => {
    const sortedDates = Object.keys(grouped[leagueId]).sort((a, b) => {
      const [da, ma, ya] = a.split('/').map(Number);
      const [db, mb, yb] = b.split('/').map(Number);
      return new Date(ya, ma - 1, da) - new Date(yb, mb - 1, db);
    });

    const sortedGroup = {};
    sortedDates.forEach(date => {
      sortedGroup[date] = grouped[leagueId][date];
    });
    grouped[leagueId] = sortedGroup;
  });

  return grouped;
});

// Filter grouped results by saved leagues
const filteredGroupedByLeague = computed(() => {
  if (!savedLeagues.value.length) return {};

  const filtered = {};
  savedLeagues.value.forEach(leagueId => {
    if (groupedByLeague.value[leagueId]) {
      filtered[leagueId] = groupedByLeague.value[leagueId];
    }
  });
  return filtered;
});

function formatDate(dateStr) {
  const [day, month, year] = dateStr.split('/');
  const date = new Date(`${year}-${month}-${day}`);
  return new Intl.DateTimeFormat('en-US', {
    weekday: 'long',
    month: 'long',
    day: 'numeric',
  }).format(date);
}
</script>
