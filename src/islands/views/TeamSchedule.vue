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

  <!-- Fixtures and Results -->
  <div v-else>
    <!-- Fixtures -->
    <template v-if="hasFixtures">
      <template
        v-for="(daysForMonth, month) in teamFixturesByMonthDay"
        :key="month"
      >
        <div class="list-group list-group-flush">
          <div class="list-group-item bg-body-tertiary sticky-month">
            <strong>{{ formatMonth(month) }}</strong>
          </div>
          <template v-for="(matchesForDay, day) in daysForMonth" :key="day">
            <ScheduleListItem
              :matches="matchesForDay"
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
        v-for="(daysForMonth, month) in teamResultsByMonthDay"
        :key="month"
      >
        <div class="list-group list-group-flush">
          <div class="list-group-item bg-body-tertiary sticky-month">
            <strong>{{ formatMonth(month) }}</strong>
          </div>
          <template v-for="(matchesForDay, day) in daysForMonth" :key="day">
            <ScheduleListItem
              :matches="matchesForDay"
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
  import type { Club, League, Fixture, Result } from '../../utils/types';
  import { formatDate, formatMonth } from '../../utils/data';
  import ScheduleListItem from '../../components/vue/items/ScheduleListItem.vue';
  import { parseISO, format } from 'date-fns';

  // Import your saved leagues composable
  import { useSavedLeagues } from '../../composables/useSavedLeagues';

  const props = defineProps<{
    club_id: string;
    fixtures: Record<string, Record<string, Fixture[]>>;
    results: Record<string, Record<string, Result[]>>;
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
  }>();

  const { savedLeagues } = useSavedLeagues();

  function leagueIsIncluded(leagueId: string) {
    // Adjust logic to either include or exclude saved leagues
    // Here, show only leagues that are saved
    return !savedLeagues.value.includes(leagueId);
  }

  const hasFixtures = computed(() =>
    Object.entries(props.fixtures).some(([day, leaguesForDay]) => {
      return Object.entries(leaguesForDay).some(([leagueId, matches]) => {
        if (!leagueIsIncluded(leagueId)) return false;
        return matches.some(
          (match) =>
            match.home_id === props.club_id || match.away_id === props.club_id
        );
      });
    })
  );

  const hasResults = computed(() =>
    Object.entries(props.results).some(([day, leaguesForDay]) => {
      return Object.entries(leaguesForDay).some(([leagueId, matches]) => {
        if (!leagueIsIncluded(leagueId)) return false;
        return matches.some(
          (match) =>
            match.home_id === props.club_id || match.away_id === props.club_id
        );
      });
    })
  );

  const teamFixturesByMonthDay = computed(() => {
    // Go through days
    const filteredByDay: Record<string, Fixture[]> = {};

    for (const [day, leaguesForDay] of Object.entries(props.fixtures)) {
      // Filter leagues inside this day by hide list
      const filteredLeagues = Object.fromEntries(
        Object.entries(leaguesForDay).filter(([leagueId]) =>
          leagueIsIncluded(leagueId)
        )
      );

      // Flatten filtered matches from included leagues
      const matches = Object.values(filteredLeagues).flat();

      // Keep only matches involving the club
      const filteredMatches = matches.filter(
        (f) => f.home_id === props.club_id || f.away_id === props.club_id
      );

      if (filteredMatches.length > 0) {
        filteredByDay[day] = filteredMatches;
      }
    }

    // Flatten all matches from all days to a list for grouping by month/day
    const allMatches = Object.values(filteredByDay).flat();

    // Sort matches by date/time
    allMatches.sort(
      (a, b) => a.date.localeCompare(b.date) || a.time.localeCompare(b.time)
    );

    // Group matches by month/day
    const grouped: Record<string, Record<string, Fixture[]>> = {};

    for (const match of allMatches) {
      const date = parseISO(match.date);
      const monthKey = format(date, 'yyyy-MM');
      const dayKey = format(date, 'yyyy-MM-dd');

      if (!grouped[monthKey]) grouped[monthKey] = {};
      if (!grouped[monthKey][dayKey]) grouped[monthKey][dayKey] = [];

      grouped[monthKey][dayKey].push(match);
    }

    return grouped;
  });

  const teamResultsByMonthDay = computed(() => {
    const filteredByDay: Record<string, Result[]> = {};

    for (const [day, leaguesForDay] of Object.entries(props.results)) {
      const filteredLeagues = Object.fromEntries(
        Object.entries(leaguesForDay).filter(([leagueId]) =>
          leagueIsIncluded(leagueId)
        )
      );

      const matches = Object.values(filteredLeagues).flat();

      const filteredMatches = matches.filter(
        (f) => f.home_id === props.club_id || f.away_id === props.club_id
      );

      if (filteredMatches.length > 0) {
        filteredByDay[day] = filteredMatches;
      }
    }

    const allMatches = Object.values(filteredByDay).flat();

    allMatches.sort(
      (a, b) => a.date.localeCompare(b.date) || a.time.localeCompare(b.time)
    );

    const grouped: Record<string, Record<string, Result[]>> = {};

    for (const match of allMatches) {
      const date = parseISO(match.date);
      const monthKey = format(date, 'yyyy-MM');
      const dayKey = format(date, 'yyyy-MM-dd');

      if (!grouped[monthKey]) grouped[monthKey] = {};
      if (!grouped[monthKey][dayKey]) grouped[monthKey][dayKey] = [];

      grouped[monthKey][dayKey].push(match);
    }

    return grouped;
  });
</script>

<style scoped>
  .sticky-month {
    position: sticky;
    top: 88px; /* navbar height */
    z-index: 10;
  }
</style>
