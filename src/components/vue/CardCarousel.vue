<template>
  <div v-if="Object.keys(filteredGroupedByLeague).length">
    <div v-for="(matches, leagueId) in filteredGroupedByLeague" :key="leagueId">
      <Swiper
        :modules="[Pagination]"
        :space-between="12"
        :pagination="{ dynamicBullets: true }"
        grab-cursor
        nested
        :touchStartPreventDefault="false"
      >
        <SwiperSlide v-for="match in matches" :key="match.id">
          <FixtureCard
            :match="match"
            :clubs="clubs"
            :leagues="leagues"
            :mode="cardMode"
          />
        </SwiperSlide>
      </Swiper>
    </div>
  </div>

  <div v-else>
    <p>No matches for your selected leagues.</p>
  </div>
</template>

<script setup>
  import { computed } from 'vue';
  import { Swiper, SwiperSlide } from 'swiper/vue';
  import { Pagination } from 'swiper/modules';
  import 'swiper/css';
  import 'swiper/css/pagination';

  import FixtureCard from './FixtureCard.vue';
  import { useSavedLeagues } from '../../utils/useSavedLeagues';

  const props = defineProps({
    matches: { type: Array, required: true },
    clubs: { type: Object, required: true },
    leagues: { type: Object, required: true },
    sortOrder: { type: String, required: true }, // 'asc' or 'desc'
    cardMode: { type: String, required: true }, // 'fixture' or 'result'
  });

  const { savedLeagues } = useSavedLeagues();

  // Group matches by league
  const groupedByLeague = computed(() => {
    const grouped = {};

    props.matches.forEach((match) => {
      const leagueId = match.league_id;
      if (!leagueId) return;

      if (!grouped[leagueId]) grouped[leagueId] = [];
      grouped[leagueId].push(match);
    });

    // Optional sorting
    for (const leagueId in grouped) {
      grouped[leagueId].sort((a, b) => {
        const da = parseDate(a.date);
        const db = parseDate(b.date);
        return props.sortOrder === 'desc' ? db - da : da - db;
      });
    }

    return grouped;
  });

  // Filter to only saved leagues
  const filteredGroupedByLeague = computed(() => {
    const result = {};
    for (const leagueId of savedLeagues.value) {
      if (groupedByLeague.value[leagueId]?.length) {
        result[leagueId] = groupedByLeague.value[leagueId];
      }
    }
    return result;
  });

  // Helper to parse dd/mm/yyyy → Date
  function parseDate(str) {
    const [dd, mm, yyyy] = str.split('/').map(Number);
    return new Date(yyyy, mm - 1, dd);
  }
</script>
