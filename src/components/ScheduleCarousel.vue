<template>
  <div>
    <div v-for="leagueId in filteredLeagueIds" :key="leagueId" class="mb-5">
      <h2>{{ leagues[leagueId] || leagueId }}</h2>

      <Swiper
        :slides-per-view="1.05"
        :space-between="12"
        :breakpoints="{
          640: { slidesPerView: 1.1 },
          768: { slidesPerView: 1.25 },
          1024: { slidesPerView: 1.5 }
        }"
        grab-cursor
      >
        <SwiperSlide
          v-for="match in scheduleByLeague[leagueId]"
          :key="match.date + '-' + match.home_id + '-' + match.away_id"
        >
          <div class="swiper-card-wrapper">
            <MatchCard
              :match="match"
              :clubs="clubs"
              :standings="{}"
            />
          </div>
        </SwiperSlide>
      </Swiper>

      <div v-if="!scheduleByLeague[leagueId]?.length">
        <p>No upcoming matches for this league.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import MatchCard from './MatchCard.vue';
import { Swiper, SwiperSlide } from 'swiper/vue';
import 'swiper/css';
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

<style scoped>
.swiper-card-wrapper {
  height: 255px !important; /* 25% of the viewport height */
  width: 100%;
  display: flex;
}
.swiper-card-wrapper > * {
  flex: 1;
}
</style>
