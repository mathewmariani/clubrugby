<template>
  <div v-if="hasResults">
    <template v-for="(daysInMonth, month) in resultsByMonthDay" :key="month">
      <DayMatchGroup
        v-for="(leaguesForDay, day) in daysInMonth"
        :key="day"
        :day="day"
        :leaguesForDay="leaguesForDay"
        matchComponent="ResultListItem"
      />
    </template>
  </div>

  <div v-else class="text-center text-muted pt-3">
    <p>No results available.</p>
    <hr />
    <p>Ensure your preferences are set.</p>
  </div>
</template>

<script setup lang="ts">
  import { useAppData } from '@/composables/useAppData';
  import { useFixtureFilters } from '@/composables/useFixtureFilters';
  import DayMatchGroup from '@/components/vue/items/DayMatchGroup.vue';

  const props = defineProps<{
    leagueId?: string;
  }>();

  const { fixtures } = useAppData();

  const { resultsByMonthDay, hasResults } = useFixtureFilters(fixtures, {
    leagueId: props.leagueId,
  });
</script>
