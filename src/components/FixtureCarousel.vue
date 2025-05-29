<template>
  <div v-if="Object.keys(filteredGroupedByLeague).length">
    <div v-for="(dates, leagueId) in filteredGroupedByLeague" >
      <div v-for="(matches, date) in dates" :key="date">
        <Swiper
          :modules="[Pagination]"
          :space-between="12"
          :pagination="{
            dynamicBullets: true,
          }"
          grab-cursor
          nested
          :touchStartPreventDefault="false"
        >
          <SwiperSlide v-for="match in matches">
            <FixtureCard :match="match" :clubs="clubs" :leagues="leagues" />
          </SwiperSlide>
        </Swiper>
      </div>
    </div>
  </div>
  <div v-else>
    <p>Loading results...</p>
  </div>
</template>

<script setup>
  import { computed } from 'vue';
  import FixtureCard from './FixtureCard.vue';
  import { Swiper, SwiperSlide } from 'swiper/vue';
  import { Pagination } from 'swiper/modules';
  import 'swiper/css';
  import 'swiper/css/pagination';
  import { useSavedLeagues } from '../utils/useSavedLeagues';

  const props = defineProps({
    clubs: { type: Object, required: true },
    leagues: { type: Object, required: true },
    fixtures: { type: Array, required: true },
  });

  const { savedLeagues } = useSavedLeagues();

  const groupedByLeague = computed(() => {
    const grouped = {};
    props.fixtures.forEach((match) => {
      if (!match.league_id || !match.date) return;

      if (!grouped[match.league_id]) grouped[match.league_id] = {};
      if (!grouped[match.league_id][match.date])
        grouped[match.league_id][match.date] = [];

      grouped[match.league_id][match.date].push(match);
    });

    Object.keys(grouped).forEach((leagueId) => {
      const sortedDates = Object.keys(grouped[leagueId]).sort((a, b) => {
        const [da, ma, ya] = a.split('/').map(Number);
        const [db, mb, yb] = b.split('/').map(Number);
        return new Date(ya, ma - 1, da) - new Date(yb, mb - 1, db);
      });

      const sortedGroup = {};
      sortedDates.forEach((date) => {
        sortedGroup[date] = grouped[leagueId][date];
      });
      grouped[leagueId] = sortedGroup;
    });

    return grouped;
  });

  const filteredGroupedByLeague = computed(() => {
    if (!savedLeagues.value.length) return {};

    const filtered = {};
    savedLeagues.value.forEach((leagueId) => {
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

<style scoped></style>
