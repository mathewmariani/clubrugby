<template>
    <div class="list-group list-group-flush">

<template v-if="hasFixtures">
      <template
        v-for="(daysForMonth, month) in teamFixturesByMonthDay"
        :key="month"
      >
        <h6 class="list-group-item">
          {{ formatMonth(month) }}
        </h6>
        <template v-for="(matchesForDay, day) in daysForMonth" :key="day">
          <ScheduleListItem
            :matches="matchesForDay"
            :clubs="clubs"
            :leagues="leagues"
          />
        </template>
      </template>
  </template>
  <p v-else class="text-muted">No upcoming fixtures.</p>

  <template v-if="hasResults">
    <div class="list-group list-group-flush">
      <template
        v-for="(daysForMonth, month) in teamResultsByMonthDay"
        :key="month"
      >
        <h6 class="list-group-item">
          {{ formatMonth(month) }}
        </h6>
        <template v-for="(matchesForDay, day) in daysForMonth" :key="day">
          <ScheduleListItem
            :matches="matchesForDay"
            :clubs="clubs"
            :leagues="leagues"
          />
        </template>
      </template>
    </div>
  </template>
  <p v-else class="text-muted">No upcoming fixtures.</p>
</div>
</template>

<script setup lang="ts">
  import { computed } from 'vue';
  import type { Club, League, Fixture, Result } from '../../../utils/types';
  import { formatDate, formatMonth } from '../../utils/data';
  import ScheduleListItem from '../../components/vue/items/ScheduleListItem.vue';

  const props = defineProps<{
    club_id: string;
    fixtures: Record<string, Record<string, Fixture[]>>;
    results: Record<string, Record<string, Result[]>>;
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
  }>();

  import { parseISO, format } from 'date-fns';

  const hasFixtures = computed(() =>
    Object.values(props.fixtures).some(
      (leaguesForDay) => Object.values(leaguesForDay).flat().length > 0
    )
  );

  const hasResults = computed(() =>
    Object.values(props.results).some(
      (leaguesForDay) => Object.values(leaguesForDay).flat().length > 0
    )
  );

  const teamFixturesByMonthDay = computed(() => {
    const filtered = Object.values(props.fixtures)
      .flatMap((byLeague) => Object.values(byLeague).flat())
      .filter((f) => f.home_id === props.club_id || f.away_id === props.club_id)
      .sort(
        (a, b) => a.date.localeCompare(b.date) || a.time.localeCompare(b.time)
      );

    const grouped: Record<
      string,
      Record<string, (typeof filtered)[number][]>
    > = {};

    for (const item of filtered) {
      const date = parseISO(item.date);
      const monthKey = format(date, 'yyyy-MM');
      const dayKey = format(date, 'yyyy-MM-dd');

      if (!grouped[monthKey]) grouped[monthKey] = {};
      if (!grouped[monthKey][dayKey]) grouped[monthKey][dayKey] = [];

      grouped[monthKey][dayKey].push(item);
    }

    return grouped;
  });

  const teamResultsByMonthDay = computed(() => {
    const filtered = Object.values(props.results)
      .flatMap((byLeague) => Object.values(byLeague).flat())
      .filter((f) => f.home_id === props.club_id || f.away_id === props.club_id)
      .sort(
        (a, b) => a.date.localeCompare(b.date) || a.time.localeCompare(b.time)
      );

    const grouped: Record<
      string,
      Record<string, (typeof filtered)[number][]>
    > = {};

    for (const item of filtered) {
      const date = parseISO(item.date);
      const monthKey = format(date, 'yyyy-MM');
      const dayKey = format(date, 'yyyy-MM-dd');

      if (!grouped[monthKey]) grouped[monthKey] = {};
      if (!grouped[monthKey][dayKey]) grouped[monthKey][dayKey] = [];

      grouped[monthKey][dayKey].push(item);
    }

    return grouped;
  });

  // Flatten and filter results
  const teamResults = computed(() =>
    Object.values(props.results)
      .flatMap((byLeague) => Object.values(byLeague).flat())
      .filter((r) => r.home_id === props.club_id || r.away_id === props.club_id)
      .sort(
        (a, b) => b.date.localeCompare(a.date) || b.time.localeCompare(b.time)
      )
  );

  // Unique match key (can be customized)
  function matchKey(match: Fixture | Result) {
    return `${match.league_id}-${match.home_id}-${match.away_id}-${match.date}`;
  }
</script>
