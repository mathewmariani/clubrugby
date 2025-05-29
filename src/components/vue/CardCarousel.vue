<template>
  <div v-if="Object.keys(filteredGroupedByLeague).length">
    <div v-for="(dates, leagueId) in filteredGroupedByLeague" :key="leagueId">
      <div v-for="(matches, date) in dates" :key="date">
        <Swiper
          :modules="[Pagination]"
          :space-between="12"
          :pagination="{ dynamicBullets: true }"
          grab-cursor
          nested
          :touchStartPreventDefault="false"
        >
          <SwiperSlide v-for="match in matches" :key="match.id">
            <component
              :is="cardComponent"
              :match="match"
              :clubs="clubs"
              :leagues="leagues"
            />
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
  import { Swiper, SwiperSlide } from 'swiper/vue';
  import { Pagination } from 'swiper/modules';
  import 'swiper/css';
  import 'swiper/css/pagination';
  import { useSavedLeagues } from '../../utils/useSavedLeagues';

  const props = defineProps({
    matches: { type: Array, required: true },
    clubs: { type: Object, required: true },
    leagues: { type: Object, required: true },
    cardComponent: { type: [Object, String], required: true },
    sortOrder: { type: String, default: 'asc' }, // 'asc' or 'desc'
  });

  const { savedLeagues } = useSavedLeagues();

  const groupedByLeague = computed(() => {
    const grouped = {};
    props.matches.forEach((match) => {
      if (!match.league_id || !match.date) return;

      if (!grouped[match.league_id]) grouped[match.league_id] = {};
      if (!grouped[match.league_id][match.date])
        grouped[match.league_id][match.date] = [];

      grouped[match.league_id][match.date].push(match);
    });

    for (const leagueId in grouped) {
      const sortedDates = Object.keys(grouped[leagueId]).sort((a, b) => {
        const [da, ma, ya] = a.split('/').map(Number);
        const [db, mb, yb] = b.split('/').map(Number);
        const d1 = new Date(ya, ma - 1, da);
        const d2 = new Date(yb, mb - 1, db);
        return props.sortOrder === 'desc' ? d2 - d1 : d1 - d2;
      });

      const sortedGroup = {};
      for (const date of sortedDates) {
        sortedGroup[date] = grouped[leagueId][date];
      }

      grouped[leagueId] = sortedGroup;
    }

    return grouped;
  });

  const filteredGroupedByLeague = computed(() => {
    if (!savedLeagues.value.length) return {};
    const filtered = {};
    for (const leagueId of savedLeagues.value) {
      if (groupedByLeague.value[leagueId]) {
        filtered[leagueId] = groupedByLeague.value[leagueId];
      }
    }
    return filtered;
  });
</script>
