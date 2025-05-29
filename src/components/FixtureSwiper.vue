<template>
  <DateHeader
    :dates="dates"
    :selected-index="selectedIndex"
    @select="goToSlide"
    ref="scrollContainer"
  />
  <Swiper
    @swiper="onSwiper"
    :initial-slide="selectedIndex"
    @slideChange="onSlideChange"
    :modules="[Pagination]"
    class="day-swiper"
  >
    <SwiperSlide v-for="(date, index) in dates" :key="index">
      <FixtureCarousel
        :clubs="clubs"
        :leagues="leagues"
        :fixtures="groupedFixtures[date]"
      />
    </SwiperSlide>
  </Swiper>
</template>

<script setup>
  import { ref, computed, nextTick, onMounted, watchEffect } from 'vue';
  import { Swiper, SwiperSlide } from 'swiper/vue';
  import { Pagination } from 'swiper/modules';
  import 'swiper/css';

  import FixtureCarousel from './FixtureCarousel.vue';
  import DateHeader from './vue/DateHeader.vue';

  const props = defineProps({
    fixtures: { type: Array, required: true },
    leagues: { type: Object, required: true },
    clubs: { type: Object, required: true },
  });

  const groupedFixtures = computed(() => {
    const grouped = {};
    props.fixtures.forEach((match) => {
      const iso = normalizeDate(match.date);
      if (!grouped[iso]) grouped[iso] = [];
      grouped[iso].push(match);
    });
    return Object.fromEntries(
      Object.entries(grouped).sort(([a], [b]) => new Date(a) - new Date(b))
    );
  });

  const dates = computed(() => Object.keys(groupedFixtures.value));
  const selectedIndex = ref(0);
  const swiperInstance = ref(null);

  watchEffect(() => {
    const today = new Date();
    const index = dates.value.findIndex((dateStr) => {
      const [year, month, day] = dateStr.split('-').map(Number);
      const date = new Date(year, month - 1, day);
      return date >= today;
    });
    selectedIndex.value = index !== -1 ? index : dates.value.length - 1;
  });

  function normalizeDate(dateStr) {
    const match = dateStr.match(/^(\d{2})\/(\d{2})\/(\d{4})$/);
    if (!match) return null;
    const [_, day, month, year] = match;
    return new Date(Number(year), Number(month) - 1, Number(day))
      .toISOString()
      .slice(0, 10);
  }

  const goToSlide = (index) => {
    selectedIndex.value = index;
    swiperInstance.value?.slideTo(index);
  };

  const onSlideChange = (swiper) => {
    selectedIndex.value = swiper.activeIndex;
  };

  const onSwiper = (swiper) => {
    swiperInstance.value = swiper;
  };
</script>
