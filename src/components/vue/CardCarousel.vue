<template>
  <div
    v-if="Object.keys(filteredGroupedByLeague).length"
    class="vertical-scroll-wrapper"
  >
    <div
      v-for="(matches, leagueId) in filteredGroupedByLeague"
      :key="leagueId"
      class="mt-3"
    >
      <Swiper
        :modules="[Pagination]"
        :space-between="12"
        :pagination="{ dynamicBullets: true }"
        grab-cursor
        nested
        :touchStartPreventDefault="false"
        @touchStart="onTouchStart"
        @touchMove="onTouchMove"
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
  import { Swiper, SwiperSlide } from 'swiper/vue';
  import { Pagination } from 'swiper/modules';
  import 'swiper/css';
  import 'swiper/css/pagination';

  import { computed } from 'vue';
  import FixtureCard from './FixtureCard.vue';
  import { useSavedLeagues } from '../../composables/useSavedLeagues';

  const props = defineProps({
    matches: { type: Array, required: true },
    clubs: { type: Object, required: true },
    leagues: { type: Object, required: true },
    sortOrder: { type: String, required: true },
    cardMode: { type: String, required: true },
  });

  const { savedLeagues } = useSavedLeagues();

  // Group matches by league
  const groupedByLeague = computed(() => {
    const grouped = {};
    props.matches.forEach((match) => {
      const leagueId = match.league_id;
      if (!leagueId) return;
      grouped[leagueId] ||= [];
      grouped[leagueId].push(match);
    });

    for (const leagueId in grouped) {
      grouped[leagueId].sort((a, b) => {
        const da = parseDate(a.date);
        const db = parseDate(b.date);
        return props.sortOrder === 'desc' ? db - da : da - db;
      });
    }

    return grouped;
  });

  const filteredGroupedByLeague = computed(() => {
    const result = {};
    for (const leagueId of savedLeagues.value) {
      if (groupedByLeague.value[leagueId]?.length) {
        result[leagueId] = groupedByLeague.value[leagueId];
      }
    }
    return result;
  });

  // Touch direction detection per swiper
  function onTouchStart(swiper) {
    swiper._touchStartX = swiper.touches.startX;
  }
  function onTouchMove(swiper) {
    const deltaX = swiper.touches.currentX - swiper._touchStartX;
    const isForward = deltaX < 0;

    swiper.allowSlideNext = !(isForward && swiper.isEnd);
    swiper.allowSlidePrev = !(!isForward && swiper.isBeginning);
  }

  function parseDate(str) {
    const [dd, mm, yyyy] = str.split('/').map(Number);
    return new Date(yyyy, mm - 1, dd);
  }
</script>

<style scoped>
  .vertical-scroll-wrapper {
    overflow-y: auto;
    scroll-behavior: smooth;
  }
</style>
