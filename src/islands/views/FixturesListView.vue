<template>
  <div v-if="hasFixtures">
    <template v-for="(daysInMonth, month) in fixturesByMonthDay" :key="month">
      <DayMatchGroup
        v-for="(leaguesForDay, day) in daysInMonth"
        :key="day"
        :day="day"
        :leaguesForDay="leaguesForDay"
        matchComponent="FixtureListItem"
      />
    </template>
  </div>

  <div v-else class="text-center text-muted pt-3">
    <p>No fixtures available.</p>
    <hr />
    <p>Ensure your preferences are set.</p>
  </div>
</template>

<script setup lang="ts">
  import { useRoute } from 'vue-router';

  import { useAppData } from '@/composables/useAppData';
  import { useFixtureFilters } from '@/composables/useFixtureFilters';
  import DayMatchGroup from '@/components/vue/items/DayMatchGroup.vue';

  const route = useRoute();
  const { fixtures } = useAppData();

  const { fixturesByMonthDay, hasFixtures } = useFixtureFilters(fixtures, {
    leagueId: route.params.league_id as string | undefined,
  });
</script>
