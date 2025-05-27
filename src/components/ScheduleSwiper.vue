<template>
  <!-- Sticky Date Header -->
  <div ref="scrollContainer" class="date-header">
    <button
      v-for="(date, index) in dates"
      :key="index"
      :class="['date-button', { active: selectedIndex === index }]"
      @click="goToSlide(index)"
      :ref="(el) => setButtonRef(el, index)"
    >
      {{ formatDate(date) }}
    </button>
  </div>

  <!-- Swiper Slide Area -->
  <Swiper
    @swiper="onSwiper"
    :initial-slide="selectedIndex"
    @slideChange="onSlideChange"
    :modules="[Pagination]"
    class="day-swiper"
  >
    <SwiperSlide v-for="(date, index) in dates" :key="index">
      <div class="day-content">
        <div class="fixture-list">
          <FixtureCard
            v-for="match in groupedFixtures[date]"
            :key="match.id"
            :match="match"
            :clubs="clubs"
          />
        </div>
      </div>
    </SwiperSlide>
  </Swiper>
</template>

<script setup>
  import { ref, computed, nextTick, onMounted, watchEffect } from 'vue';
  import { Swiper, SwiperSlide } from 'swiper/vue';
  import { Pagination } from 'swiper/modules';
  import 'swiper/css';
  import FixtureCard from './FixtureCard.vue';

  const props = defineProps({
    schedule: { type: Array, required: true },
    clubs: { type: Object, required: true },
  });

  // Group schedule by ISO date
  const groupedFixtures = computed(() => {
    const grouped = {};
    props.schedule.forEach((match) => {
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
  const scrollContainer = ref(null);
  const dateButtons = ref([]);

  watchEffect(() => {
    const today = new Date();
    const index = dates.value.findIndex((dateStr) => {
      const [year, month, day] = dateStr.split('-').map(Number);
      const date = new Date(year, month - 1, day);
      return date >= today;
    });

    selectedIndex.value = index !== -1 ? index : dates.value.length - 1;
  });

  const setButtonRef = (el, index) => {
    if (el) dateButtons.value[index] = el;
  };

  function normalizeDate(dateStr) {
    const match = dateStr.match(/^(\d{2})\/(\d{2})\/(\d{4})$/);
    if (!match) return null;
    const [_, day, month, year] = match;
    const date = new Date(Number(year), Number(month) - 1, Number(day)); // local time
    return date.toISOString().slice(0, 10); // safe normalized ISO format
  }

  const formatDate = (iso) => {
    const [year, month, day] = iso.split('-').map(Number);
    const date = new Date(year, month - 1, day); // local date again
    return date.toLocaleDateString('en-US', {
      weekday: 'short',
      month: 'short',
      day: '2-digit',
    });
  };

  const centerSelected = () => {
    nextTick(() => {
      const container = scrollContainer.value;
      const selected = dateButtons.value[selectedIndex.value];
      if (container && selected) {
        const containerWidth = container.offsetWidth;
        const selectedLeft = selected.offsetLeft;
        const selectedWidth = selected.offsetWidth;
        const scrollTo = selectedLeft - containerWidth / 2 + selectedWidth / 2;
        container.scrollTo({ left: scrollTo, behavior: 'smooth' });
      }
    });
  };

  const goToSlide = (index) => {
    selectedIndex.value = index;
    swiperInstance.value?.slideTo(index);
    centerSelected();
  };

  const onSlideChange = (swiper) => {
    selectedIndex.value = swiper.activeIndex;
    centerSelected();
  };

  const onSwiper = (swiper) => {
    swiperInstance.value = swiper;
    centerSelected();
  };

  onMounted(() => {
    centerSelected();
  });
</script>

<style scoped>
  .date-swiper-wrapper {
    max-width: 800px;
    margin: 0 auto;
    padding-top: 1rem;
  }

  .date-header {
    display: flex;
    overflow-x: auto;
    gap: 0.5rem;
    padding: 0.5rem 0;
    margin-bottom: 1rem;
    scroll-behavior: smooth;
    white-space: nowrap;
    scrollbar-width: none;
    scroll-padding-left: 50%;
    scroll-padding-right: 50%;
  }
  .date-header::-webkit-scrollbar {
    display: none;
  }

  .date-button {
    padding: 8px 14px;
    border: none;
    border-radius: 20px;
    background: rgba(0, 0, 0, 0.1);
    font-size: 14px;
    cursor: pointer;
    flex-shrink: 0;
    transition: 0.2s;
  }

  .date-button.active {
    background: #007aff;
    color: white;
    font-weight: bold;
  }

  .day-swiper {
    height: auto;
  }

  .day-content {
    background: white;
    padding: 1rem;
    border-radius: 12px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  }

  .fixture-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }
</style>
