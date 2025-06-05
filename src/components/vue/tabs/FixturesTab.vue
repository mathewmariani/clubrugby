<template>
  <div class="list-group">
    <template v-for="(fixtures, day) in dailyFixtures" :key="day">
      <strong class="list-group-item">{{ formatDate(day) }}</strong>
      <FixtureListItem
        v-for="fixture in fixtures"
        :match="fixture"
        :clubs="clubs"
        :leagues="leagues"
      />
    </template>
  </div>
</template>

<script setup>
  import { computed } from 'vue';
  import FixtureListItem from '../FixtureListItem.vue';
  import { groupFixturesByDay, formatDate } from '../../../utils';
  const props = defineProps({
    clubs: Object,
    leagues: Object,
    fixtures: Object,
  });

  const dailyFixtures = computed(() => groupFixturesByDay(props.fixtures));
</script>

<style scoped>
  .list-group {
    border-radius: 0;
    border-radius: 0;
  }
</style>
