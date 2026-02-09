<template>
  <template v-if="hasResults">
    <template v-for="(daysInMonth, monthId) in resultsByMonthDay" :key="monthId">
      <DayMatchGroup
        v-for="(fixtures, dayId) in daysInMonth"
        :key="dayId"
        :day="dayId"
        :leaguesForDay="getLeaguesByDay(fixtures)"
        :clubs="clubs"
        :leagues="leagues"
        matchComponent="ResultListItem"
      />
    </template>
  </template>
  <template v-else>
    <div class="container-fluid text-center text-muted pt-3">
      <p>No results available.</p>
      <hr />
      <p>Ensure your preferences are set.</p>
    </div>
  </template>
</template>

<script setup lang="ts">
  import { computed } from 'vue';
  import type { Fixture } from '@/utils/types';
  import { useFixtureFilters } from '@/composables/useFixtureFilters';
  import { groupByMonthDay } from '@/composables/utils';
  import DayMatchGroup from '@/components/vue/items/DayMatchGroup.vue';

  import { useAppData } from '@/composables/useAppData';
  const { fixtures, clubs, leagues } = useAppData();

  const { leaguesWithResults, hasResults } = useFixtureFilters(
    computed(() => fixtures)
  );

  // Group all results by month/day
  const resultsByMonthDay = computed(() => {
    const allResults = Object.values(leaguesWithResults.value).flat();
    return groupByMonthDay(allResults);
  });

  // Convert flat fixture array to leagues grouped by league ID
  function getLeaguesByDay(fixtures: Fixture[]): Record<string, Fixture[]> {
    const grouped: Record<string, Fixture[]> = {};
    for (const fixture of fixtures) {
      // Find which league this fixture belongs to
      const leagueId = Object.entries(fixtures).find(([_, leagueFixtures]) =>
        leagueFixtures.includes(fixture)
      )?.[0];

      if (leagueId) {
        if (!grouped[leagueId]) grouped[leagueId] = [];
        grouped[leagueId].push(fixture);
      }
    }
    return grouped;
  }
</script>
