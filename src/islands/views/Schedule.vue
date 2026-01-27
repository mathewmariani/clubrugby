<template>
  <div v-if="hasFixtures">
    <template v-for="(daysInMonth, monthId) in fixturesByMonthDay" :key="monthId">
      <DayMatchGroup
        v-for="(fixtures, dayId) in daysInMonth"
        :key="dayId"
        :day="dayId"
        :leaguesForDay="getLeaguesByDay(fixtures)"
        :clubs="clubs"
        :leagues="leagues"
        matchComponent="FixtureListItem"
      />
    </template>
  </div>
  <div v-else class="container-fluid text-center text-muted pt-3">
    <p>No fixtures available.</p>
    <hr />
    <p>Ensure your preferences are set.</p>
  </div>
</template>


<script setup lang="ts">
import { computed } from 'vue';
import type { Club, Fixture } from '@/utils/types';
import type { Union } from '@/utils/unions';
import { useFixtureFilters } from '@/composables/useFixtureFilters';
import { groupByMonthDay } from '@/composables/utils';
import DayMatchGroup from '@/components/vue/items/DayMatchGroup.vue';

const props = defineProps<{
  union: Union;
  clubs: Record<string, Club>;
  leagues: Record<string, string>;
  fixtures: Record<string, Fixture[]>;
}>();

const { leaguesWithFixtures, hasFixtures } = useFixtureFilters(
  computed(() => props.fixtures)
);

// Group all fixtures by month/day
const fixturesByMonthDay = computed(() => {
  const allFixtures = Object.values(leaguesWithFixtures.value).flat();
  return groupByMonthDay(allFixtures);
});

// Convert flat fixture array to leagues grouped by league ID
function getLeaguesByDay(fixtures: Fixture[]): Record<string, Fixture[]> {
  const grouped: Record<string, Fixture[]> = {};
  for (const fixture of fixtures) {
    // Find which league this fixture belongs to
    const leagueId = Object.entries(props.fixtures).find(([_, leagueFixtures]) =>
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
