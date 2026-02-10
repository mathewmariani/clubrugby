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
  import { useAppData } from '@/composables/useAppData';
  import { useFixtureFilters } from '@/composables/useFixtureFilters';
  import DayMatchGroup from '@/components/vue/items/DayMatchGroup.vue';

  const { fixtures } = useAppData();

  // optional: pass clubId if needed
  const { fixturesByMonthDay, hasFixtures } = useFixtureFilters(fixtures);
</script>
