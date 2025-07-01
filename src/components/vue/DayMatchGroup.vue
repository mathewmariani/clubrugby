<template>
  <div class="list-group list-group-flush">
    <div class="list-group-item bg-body-tertiary sticky-date">
      <strong>{{ formatDate(day) }}</strong>
    </div>

    <template v-for="(matches, leagueId) in leaguesForDay" :key="leagueId">
      <div class="list-group list-group-flush">
        <div class="list-group-item bg-body-tertiary sticky-league">
          <strong>{{ getLeagueName(leagueId, leagues) }}</strong>
        </div>

        <component
          :is="components[matchComponent]"
          v-for="match in matches"
          :key="match.id"
          :match="match"
          :home="clubs[match.home_id]"
          :away="clubs[match.away_id]"
        />
      </div>
    </template>
  </div>
</template>

<script setup lang="ts">
  import FixtureListItem from '@/components/vue/items/FixtureListItem.vue';
  import ResultListItem from '@/components/vue/items/ResultListItem.vue';
  import { formatDate } from '@/utils/data';
  import { getLeagueName } from '@/composables/utils';
  import type { Club, League, Fixture, Result } from '@/utils/types';

  const props = withDefaults(
    defineProps<{
      day: string;
      leaguesForDay: Record<string, (Fixture | Result)[]>;
      clubs: Record<string, Club>;
      leagues: Record<string, League>;
      matchComponent: 'FixtureListItem' | 'ResultListItem';
    }>(),
    {}
  );

  const components = {
    FixtureListItem,
    ResultListItem,
  };
</script>

<style scoped>
  .sticky-date {
    position: sticky;
    top: 88px;
    z-index: 10;
  }
  .sticky-league {
    position: sticky;
    top: calc(88px + 2.5rem);
    z-index: 9;
  }
</style>
