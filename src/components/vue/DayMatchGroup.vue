<template>
  <div class="list-group list-group-flush">
    <div class="sticky-date" :style="{ top: navbarHeight + 'px' }">
      <div class="list-group-header list-group-item bg-body-tertiary">
        {{ day }}
      </div>
    </div>

    <template v-for="(matches, leagueId) in leaguesForDay" :key="leagueId">
      <div class="list-group list-group-flush">
        <div class="sticky-league" :style="{ top: leagueTopOffset + 'px' }">
          <div class="list-group-header list-group-item bg-body-tertiary">
            <small>{{ getLeagueName(leagueId, leagues) }}</small>
          </div>
        </div>

        <component
          :is="components[matchComponent]"
          v-for="match in matches"
          :key="match.fixtureId"
          :match="match"
          :home="clubs[match.homeClubId]"
          :away="clubs[match.awayClubId]"
        />
      </div>
    </template>
  </div>
</template>

<script setup lang="ts">
  import { computed } from 'vue';
  import FixtureListItem from '@/components/vue/items/FixtureListItem.vue';
  import ResultListItem from '@/components/vue/items/ResultListItem.vue';
  import { formatDate } from '@/utils/data';
  import { getLeagueName } from '@/composables/utils';
  import type { Club, League, Fixture } from '@/utils/types';

  const props = withDefaults(
    defineProps<{
      day: string;
      leaguesForDay: Record<string, Fixture[]>;
      clubs: Record<string, Club>;
      leagues: Record<string, League>;
      matchComponent: 'FixtureListItem' | 'ResultListItem';
    }>(),
    {}
  );

  import { useLayout } from '@/composables/useLayout';

  const { navbarHeight } = useLayout();
  const dateHeaderHeight = 32;

  const leagueTopOffset = computed(() => navbarHeight.value + dateHeaderHeight);

  const components = {
    FixtureListItem,
    ResultListItem,
  };
</script>

<style scoped>
  .sticky-date {
    position: sticky;
    z-index: 10;
  }
  .sticky-league {
    position: sticky;
    z-index: 9;
  }
</style>
