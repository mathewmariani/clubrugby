<template>
  <div v-if="hasFixtures">
    <DayMatchGroup
      v-for="(leaguesForDay, day) in fixturesByDay"
      :key="day"
      :day="day"
      :leagues-for-day="leaguesForDay"
      :clubs="clubs"
      :leagues="leagues"
      match-component="FixtureListItem"
    />
  </div>

  <template v-else>
    <div class="container-fluid text-center text-muted pt-3">
      <p>No fixtures available.</p>
      <hr />
      <p>Ensure your preferences are set.</p>
    </div>
  </template>
</template>

<script setup lang="ts">
import { toRef, computed } from 'vue';
import DayMatchGroup from '@/components/vue/DayMatchGroup.vue';
import { useSavedLeagues } from '@/composables/useSavedLeagues';
import { useFilteredMatches } from '@/composables/useFilteredMatches';
import type { Club, League, Match } from '@/utils/types';
import type { Union } from '@/utils/unions';

const props = defineProps<{
  union: Union;
  clubs: Record<string, Club>;
  leagues: Record<string, League>;
  fixtures: Record<string, Record<string, Match[]>>; // leagueId => day => Match[]
}>();

const clubs = toRef(props, 'clubs');
const leagues = toRef(props, 'leagues');

const { savedLeagues } = useSavedLeagues();

// Filter leagues based on user preferences
const { filtered: filteredFixtures, has: hasFixtures } = useFilteredMatches(
  toRef(props, 'fixtures'),
  savedLeagues
);

// Group fixtures by day (date string) for easier iteration
const fixturesByDay = computed(() => {
  const result: Record<string, Record<string, Match[]>> = {};

  for (const [leagueId, matchesByDay] of Object.entries(filteredFixtures)) {
    for (const [dayKey, matches] of Object.entries(matchesByDay)) {
      if (!result[dayKey]) result[dayKey] = {};
      result[dayKey][leagueId] = matches;
    }
  }

  return result;
});
</script>
