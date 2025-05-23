<template>
    <div v-if="Object.keys(filteredGroupedByLeague).length">
      <div
        v-for="(dates, leagueId) in filteredGroupedByLeague"
        :key="leagueId"
        class="mb-5"
      >
        <h2>{{ leagues[leagueId] || leagueId }}</h2>
  
        <div v-for="(matches, date) in dates" :key="date" class="mb-4">
          <h4>{{ formatDate(date) }}</h4>
  
          <Swiper
            :slides-per-view="1.05"
            :space-between="12"
            :breakpoints="{
              640: { slidesPerView: 2 },
              768: { slidesPerView: 3 },
              1024: { slidesPerView: 4 }
            }"
            grab-cursor
          >
            <SwiperSlide
              v-for="match in matches"
              :key="match.id || match.date + match.home_id + match.away_id"
              class="swiper-slide-custom"
            >
              <ResultCard :match="match" :clubs="clubs" />
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
  import ResultCard from './ResultCard.vue';
  import { Swiper, SwiperSlide } from 'swiper/vue';
  import 'swiper/css';
  import { useSavedLeagues } from '../utils/useSavedLeagues';
  
  const props = defineProps({
    results: { type: Array, required: true },
    clubs: { type: Object, required: true },
    leagues: { type: Object, required: true },
  });
  
  const { savedLeagues } = useSavedLeagues();
  
  const groupedByLeague = computed(() => {
    const grouped = {};
    props.results.forEach((match) => {
      if (!match.league_id || !match.date) return;
  
      if (!grouped[match.league_id]) grouped[match.league_id] = {};
      if (!grouped[match.league_id][match.date]) grouped[match.league_id][match.date] = [];
  
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
  
  <style scoped>
  /* Make swiper slides and their content fill 25vh */
  .swiper-slide-custom {
    height: 255px !important;
    display: flex;
    align-items: stretch; /* full height for children */
  }
  
  .swiper-slide-custom > * {
    flex-grow: 1;
    height: 100%;
  }
  </style>
  