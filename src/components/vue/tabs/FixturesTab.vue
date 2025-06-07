<template>
  <div class="list-group list-group-flush">
    <template v-for="(leaguesForDay, day) in filteredFixtures" :key="day">
      <strong class="list-group-item">{{ formatDate(day) }}</strong>

      <template v-for="(matches, leagueId) in leaguesForDay" :key="leagueId">
        <strong class="list-group-item">
          {{ props.leagues[leagueId]?.name || 'Unknown League' }}
        </strong>

        <FixtureListItem
          v-for="match in matches"
          :match="match"
          :clubs="props.clubs"
          :leagues="props.leagues"
        />
      </template>
    </template>
  </div>
</template>

<script setup lang="ts">
  import { computed } from 'vue';

  import FixtureListItem from '../items/FixtureListItem.vue';
  import { type Club, type League, type Fixture } from '../../../utils/types';
  import { formatDate } from '../../../utils/data';

  const props = defineProps<{
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
    fixtures: Record<string, Record<string, Fixture[]>>;
  }>();

  import { toRef } from 'vue';
  import { useFilteredFixtures } from '../../../composables/useFilteredFixtures';

  const filteredFixtures = useFilteredFixtures(toRef(props, 'fixtures'));
</script>

<style scoped>
  .list-group {
    border-radius: 0;
  }
</style>
