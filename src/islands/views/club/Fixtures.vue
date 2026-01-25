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
import { groupByMonthDay, flattenFixturesForClub } from '@/composables/utils';
import { useSavedLeagues } from '@/composables/useSavedLeagues';
import { useLayout } from '@/composables/useLayout';

const props = defineProps<{
  club_id: string;
  fixtures: Record<string, Fixture[]>;
  clubs: Record<string, Club>;
  leagues: Record<string, string>;
}>();

const { navbarHeight } = useLayout();

// --- Computed fixtures/results ---
const upcomingByMonthDay = computed(() =>
  groupByMonthDay(flattenFixturesForClub(props.fixtures, props.club_id, 'fixture'))
);

const resultsByMonthDay = computed(() =>
  groupByMonthDay(flattenFixturesForClub(props.fixtures, props.club_id, 'result'))
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
