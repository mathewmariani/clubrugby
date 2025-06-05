<template>
  <div class="list-group">
    <template v-for="(results, day) in dailyResults" :key="day">
      <strong class="list-group-item">{{ formatDate(day) }}</strong>
      <ResultListItem
        v-for="result in results"
        :match="result"
        :clubs="clubs"
        :leagues="leagues"
      />
    </template>
  </div>
</template>

<script setup>
  import { computed } from 'vue';
  import ResultListItem from '../ResultListItem.vue';
  import { groupResultsByDay, formatDate } from '../../../utils';
  const props = defineProps({
    clubs: Object,
    leagues: Object,
    results: Object,
  });

  const dailyResults = computed(() => groupResultsByDay(props.results));
</script>

<style scoped>
  .list-group {
    border-radius: 0;
    border-radius: 0;
  }
</style>
