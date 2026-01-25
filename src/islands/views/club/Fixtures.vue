<template>
  <!-- Empty state -->
  <div
    v-if="!hasFixtures && !hasResults"
    class="container-fluid text-center text-muted pt-3"
  >
    <p>No fixtures or results available.</p>
    <hr />
    <p>Ensure your preferences are set.</p>
  </div>

  <div v-else>
    <!-- Upcoming Fixtures -->
    <template v-if="hasFixtures">
      <template
        v-for="(daysForMonth, month) in upcomingByMonthDay"
        :key="month"
      >
        <div class="list-group list-group-flush">
          <div class="sticky-month" :style="{ top: navbarHeight + 'px' }">
            <div class="list-group-header list-group-item bg-body-tertiary">
              {{ month }}
            </div>
          </div>
          <template v-for="(matchesForDay, day) in daysForMonth" :key="day">
            <ScheduleListItem
              :fixtures="matchesForDay"
              :clubs="clubs"
              :leagues="leagues"
            />
          </template>
        </div>
      </template>
    </template>

    <p v-else class="list-group-item text-muted">No upcoming fixtures.</p>

    <!-- Results -->
    <template v-if="hasResults">
      <template
        v-for="(daysForMonth, month) in resultsByMonthDay"
        :key="month"
      >
        <div class="list-group list-group-flush">
          <div class="sticky-month" :style="{ top: navbarHeight + 'px' }">
            <div class="list-group-header list-group-item bg-body-tertiary">
              {{ month }}
            </div>
          </div>
          <template v-for="(matchesForDay, day) in daysForMonth" :key="day">
            <ScheduleListItem
              :fixtures="matchesForDay"
              :clubs="clubs"
              :leagues="leagues"
            />
          </template>
        </div>
      </template>
    </template>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import type { Club, Fixture } from '@/utils/types';
import ScheduleListItem from '@/components/vue/items/ScheduleListItem.vue';
import { format } from 'date-fns';
import { useSavedLeagues } from '@/composables/useSavedLeagues';
import { useLayout } from '@/composables/useLayout';

const props = defineProps<{
  club_id: string;
  fixtures: Record<string, Fixture[]>; // league_id -> Fixture[]
  clubs: Record<string, Club>;
  leagues: Record<string, string>;
}>();

const { navbarHeight } = useLayout();

// --- Flatten & filter fixtures for this club ---
function flattenClubMatches(status: 'fixture' | 'result') {
  const all: Fixture[] = [];
  for (const [leagueId, matches] of Object.entries(props.fixtures)) {
    for (const match of matches) {
      if (
        match.homeClubId === props.club_id ||
        match.awayClubId === props.club_id
      ) {
        if (match.fixtureStatus === status) {
          all.push(match);
        }
      }
    }
  }
  return all;
}

// --- Group by month/day ---
function groupByMonthDay(matches: Fixture[]) {
  const grouped: Record<string, Record<string, Fixture[]>> = {};
  const sorted = [...matches].sort((a, b) => a.fixtureDate - b.fixtureDate);

  for (const match of sorted) {
    const date = new Date(match.fixtureDate * 1000);
    const monthKey = format(date, 'yyyy-MM');
    const dayKey = format(date, 'yyyy-MM-dd');

    if (!grouped[monthKey]) grouped[monthKey] = {};
    if (!grouped[monthKey][dayKey]) grouped[monthKey][dayKey] = [];

    grouped[monthKey][dayKey].push(match);
  }

  return grouped;
}

// --- Computed fixtures/results ---
const upcomingByMonthDay = computed(() =>
  groupByMonthDay(flattenClubMatches('fixture'))
);

const resultsByMonthDay = computed(() =>
  groupByMonthDay(flattenClubMatches('result'))
);

const hasFixtures = computed(() => Object.keys(upcomingByMonthDay.value).length > 0);
const hasResults = computed(() => Object.keys(resultsByMonthDay.value).length > 0);
</script>

<style scoped>
.sticky-month {
  position: sticky;
  z-index: 10;
}
</style>
