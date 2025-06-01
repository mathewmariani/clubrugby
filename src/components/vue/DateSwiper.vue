<template>
  <DateHeader
    :dates="dates"
    :selected-index="selectedIndex"
    @select="goToSlide"
  />

  <Swiper
    @swiper="onSwiper"
    :initial-slide="selectedIndex"
    @slideChange="onSlideChange"
    :modules="[Pagination]"
    grab-cursor
    :autoHeight="true"
    :space-between="12"
  >
    <SwiperSlide v-for="(date, index) in dates" :key="date">
      <CardCarousel
        :matches="groupedMatches[date]"
        :clubs="clubs"
        :leagues="leagues"
        :cardMode="cardMode"
        sortOrder="desc"
      />
    </SwiperSlide>
  </Swiper>
</template>

<script setup>
  import { ref, computed, watch, watchEffect } from 'vue';
  import { Swiper, SwiperSlide } from 'swiper/vue';
  import { Pagination } from 'swiper/modules';
  import 'swiper/css';
  import 'swiper/css/pagination';

  import DateHeader from './DateHeader.vue';
  import CardCarousel from './CardCarousel.vue';
  import { useSavedLeagues } from '../../composables/useSavedLeagues';

  const props = defineProps({
    items: { type: Array, required: true },
    clubs: { type: Object, required: true },
    leagues: { type: Object, required: true },
    cardMode: { type: String, required: true },
  });

  const { savedLeagues } = useSavedLeagues();

  function normalizeDate(dateStr) {
    const [day, month, year] = dateStr.split('/');
    return new Date(year, month - 1, day).toISOString().slice(0, 10);
  }

  // Filter items by saved leagues
  const filteredItems = computed(() => {
    return props.items.filter(
      (match) => match.league_id && savedLeagues.value.includes(match.league_id)
    );
  });

  // Group filtered items by date (ISO format)
  const groupedMatches = computed(() => {
    const grouped = {};
    for (const match of filteredItems.value) {
      const iso = normalizeDate(match.date);
      if (!grouped[iso]) grouped[iso] = [];
      grouped[iso].push(match);
    }

    return Object.fromEntries(
      Object.entries(grouped).sort(([a], [b]) => new Date(a) - new Date(b))
    );
  });

  // All date keys (for slides and header)
  const dates = computed(() => Object.keys(groupedMatches.value));

  const selectedIndex = ref(0);
  const swiperInstance = ref(null);

  // Set initial index to the next upcoming day
  watchEffect(() => {
    if (props.cardMode === 'result') {
      selectedIndex.value = dates.value.length - 1;
    } else {
      const today = new Date();
      const index = dates.value.findIndex((d) => new Date(d) >= today);
      selectedIndex.value = index !== -1 ? index : 0;
    }
  });

  watch(selectedIndex, (newIndex) => {
    if (swiperInstance.value && swiperInstance.value.activeIndex !== newIndex) {
      swiperInstance.value.slideTo(newIndex);
    }
  });

  function goToSlide(index) {
    selectedIndex.value = index;
    swiperInstance.value?.slideTo(index);
  }

  function onSlideChange(swiper) {
    selectedIndex.value = swiper.activeIndex;
  }

  function onSwiper(swiper) {
    swiperInstance.value = swiper;
  }
</script>

<style scoped>
  .swiper {
    transition-duration: 0ms !important;
  }
  .swiper-slide {
    transition: opacity 150ms ease;
  }
  .swiper-slide-active {
    opacity: 1;
  }
  .swiper-slide:not(.swiper-slide-active) {
    opacity: 0.5;
    pointer-events: none;
  }
</style>
