<template>
  {{ hasFixtures }}
  {{ fixturesByMonthDay }}
  <template v-if="hasFixtures">
    <template
      v-for="(daysInMonth, monthId) in fixturesByMonthDay"
      :key="monthId"
    >
      <DayMatchGroup
        v-for="(leaguesForDay, dayId) in fixturesByMonthDay"
        :key="dayId"
        :day="dayId"
        :leaguesForDay="leaguesForDay"
        matchComponent="FixtureListItem"
      />
    </template>
  </template>
  <template v-else>
    <div class="container-fluid text-center text-muted pt-3">
      <p>No fixtures available.</p>
      <hr />
      <p>Ensure your preferences are set.</p>
    </div>
  </template>
</template>

<script setup lang="ts">
  import { computed } from 'vue';
  import { useFixtureFilters } from '@/composables/useFixtureFilters';
  import { groupByMonthDay } from '@/composables/utils';
  import type { Club, Fixture } from '@/utils/types';

  import { useAppData } from '@/composables/useAppData';
  const { unions, fixtures, clubs, leagues, standings } = useAppData();

  const { leaguesWithFixtures, hasFixtures } = useFixtureFilters(
    computed(() => fixtures)
  );

  const fixturesByMonthDay = computed(() => {
    const all = Object.values(leaguesWithFixtures.value).flat();

    const byDay = groupByMonthDay(all);

    const result: Record<string, Record<string, Fixture[]>> = {};

    for (const [day, items] of Object.entries(byDay)) {
      result[day] = {};

      for (const f of items) {
        if (!result[day][f.league_id]) result[day][f.league_id] = [];
        result[day][f.league_id].push(f);
      }
    }

    return result;
  });
</script>
