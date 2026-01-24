<template>
  <div v-if="hasFixtures">
    <template v-for="(fixtures, leagueId) in leaguesWithResults" :key="leagueId">
      <div class="list-group list-group-flush">
        <div class="sticky-league" :style="{ top: leagueTopOffset + 'px' }">
          <div class="list-group-header list-group-item bg-body-tertiary">
            <small>{{ getLeagueName(leagueId.toString(), props.leagues) }}</small>
          </div>
        </div>

        <ResultListItem
          v-for="fixture in fixtures"
          :key="fixture.fixtureId"
          :fixture="fixture"
          :home="clubs[fixture.homeClubId]"
          :away="clubs[fixture.awayClubId]"
        />
      </div>
    </template>
  </div>
  <div v-else class="container-fluid text-center text-muted pt-3">
    <p>No fixtures available.</p>
    <hr />
    <p>Ensure your preferences are set.</p>
  </div>
</template>


<script setup lang="ts">
import { computed } from 'vue';
import type { Club, Fixture } from '@/utils/types';
import type { Union } from '@/utils/unions';
import { getLeagueName } from '@/composables/utils';
import ResultListItem from '@/components/vue/items/ResultListItem.vue';

const props = defineProps<{
  union: Union;
  clubs: Record<string, Club>;
  leagues: Record<string, string>;
  fixtures: Record<string, Fixture[]>;
}>();

const leaguesWithResults = computed(() =>
  Object.fromEntries(
    Object.entries(props.fixtures).map(([leagueId, fixtures]) => [
      leagueId,
      fixtures.filter(f => f.fixtureStatus === 'result'),
    ]).filter(([_, fixtures]) => fixtures.length > 0)
  )
);

const hasFixtures = computed(() => Object.keys(leaguesWithResults.value).length > 0);

</script>
