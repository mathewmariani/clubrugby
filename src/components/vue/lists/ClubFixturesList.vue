<template>
  <div>
    <!-- Empty state -->
    <template v-if="!hasFixtures && !hasResults">
      <div class="container-fluid text-center text-muted pt-3">
        <p>No fixtures or results available.</p>
        <hr />
        <p>Ensure your preferences are set.</p>
      </div>
    </template>

    <template v-else>
      <!-- Upcoming Fixtures -->
      <template v-if="hasFixtures">
        <template
          v-for="(daysForMonth, month) in fixturesByMonthDay"
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
                :clubId="clubId"
                :fixturesByLeague="matchesForDay"
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
                :clubId="clubId"
                :fixturesByLeague="matchesForDay"
              />
            </template>
          </div>
        </template>
      </template>
    </template>
  </div>
</template>

<script setup lang="ts">
  import { computed } from 'vue';
  import ScheduleListItem from '@/components/vue/items/ScheduleListItem.vue';
  import { useFixtureFilters } from '@/composables/useFixtureFilters';
  import { useLayout } from '@/composables/useLayout';
  import { useAppData } from '@/composables/useAppData';

  const { fixtures, clubs, leagues } = useAppData();
  const { navbarHeight } = useLayout();

  /* ---------------------------------
   Get club_id from URL (Astro-safe)
---------------------------------- */
  const props = defineProps<{
    clubId: string;
  }>();

  /* ---------------------------------
   Fixture filtering
---------------------------------- */
  const {
    clubFixturesByMonthDay,
    clubResultsByMonthDay,
    clubHasFixtures,
    clubHasResults,
  } = useFixtureFilters(fixtures, {
    clubId: props.clubId,
  });

  /* ---------------------------------
   Exposed values for template
---------------------------------- */
  const fixturesByMonthDay = computed(() => clubFixturesByMonthDay.value);
  const resultsByMonthDay = computed(() => clubResultsByMonthDay.value);
  const hasFixtures = computed(() => clubHasFixtures.value);
  const hasResults = computed(() => clubHasResults.value);
</script>
