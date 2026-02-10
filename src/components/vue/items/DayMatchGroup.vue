<template>
  <div class="list-group list-group-flush">
    <div class="sticky-date" :style="{ top: navbarHeight + 'px' }">
      <div class="list-group-header list-group-item bg-body-tertiary">
        {{ day }}
      </div>
    </div>

    <template v-for="(fixtures, leagueId) in leaguesForDay" :key="leagueId">
      <div class="list-group list-group-flush">
        <div class="sticky-league" :style="{ top: leagueTopOffset + 'px' }">
          <div class="list-group-header list-group-item bg-body-tertiary">
            <small>{{ getLeagueName(leagueId.toString(), leagues) }}</small>
          </div>
        </div>

        <component
          :is="components[matchComponent]"
          v-for="fixture in fixtures"
          :key="fixture.fixtureId"
          :fixture="fixture"
          :home="clubs[fixture.home.club_id]"
          :away="clubs[fixture.away.club_id]"
        />
      </div>
    </template>
  </div>
</template>

<script setup lang="ts">
  import { computed } from 'vue';
  import FixtureListItem from '@/components/vue/items/FixtureListItem.vue';
  import ResultListItem from '@/components/vue/items/ResultListItem.vue';
  import { getLeagueName } from '@/composables/utils';
  import { useLayout } from '@/composables/useLayout';
  import type { Club, Fixture } from '@/utils/types';

  import { useAppData } from '@/composables/useAppData';
  const { clubs, leagues } = useAppData();

  const props = defineProps<{
    day: string;
    leaguesForDay: Record<string, Fixture[]>;
    matchComponent: 'FixtureListItem' | 'ResultListItem';
  }>();

  const { navbarHeight } = useLayout();
  const dateHeaderHeight = 32;

  const leagueTopOffset = computed(() => navbarHeight.value + dateHeaderHeight);

  const components = {
    FixtureListItem,
    ResultListItem,
  };
</script>
