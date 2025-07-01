<template>
  <div v-if="hasFixtures">
    <template v-for="(leaguesForDay, day) in filteredFixtures" :key="day">
      <!-- Day wrapper -->
      <div class="list-group list-group-flush">
        <!-- Sticky Date Header -->
        <div class="list-group-item bg-body-tertiary sticky-date">
          <strong>{{ formatDate(day) }}</strong>
        </div>

        <!-- League sections inside the day group -->
        <template v-for="(matches, leagueId) in leaguesForDay" :key="leagueId">
          <!-- League wrapper to enable sticky league header to push -->
          <div class="list-group list-group-flush">
            <!-- Sticky League Header -->
            <div class="list-group-item bg-body-tertiary sticky-league">
              <strong>{{ getLeagueName(leagueId, leagues) }}</strong>
            </div>

            <!-- Matches -->
            <FixtureListItem
              v-for="match in matches"
              :match="match"
              :home="clubs[match.home_id]"
              :away="clubs[match.away_id]"
            />
          </div>
        </template>
      </div>
    </template>
  </div>

  <template v-else>
    <div class="container-fluid text-center text-muted pt-3">
      <p>No fixtures available.</p>
      <hr />
      <p>Ensure your preferences are set.</p>
    </div>
  </template>
</template>

<script setup lang="ts">
  import { computed, toRef } from 'vue';
  import type { Club, League, Fixture } from '../../utils/types';
  import type { Union } from '../../utils/unions';

  import { formatDate } from '../../utils/data';
  import { getLeagueName } from '../../composables/utils';
  import { useSavedLeagues } from '../../composables/useSavedLeagues';
  import { useFilteredFixtures } from '../../composables/useFilteredFixtures';
  import FixtureListItem from '../../components/vue/items/FixtureListItem.vue';

  const props = defineProps<{
    union: Union;
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
    fixtures: Record<string, Record<string, Fixture[]>>;
  }>();

  const fixtures = toRef(props, 'fixtures');
  const leagues = toRef(props, 'leagues');
  const clubs = toRef(props, 'clubs');

  const { savedLeagues } = useSavedLeagues();
  const filteredFixtures = useFilteredFixtures(fixtures, savedLeagues);

  const hasFixtures = computed(() =>
    Object.values(filteredFixtures.value).some(
      (leaguesForDay) => Object.values(leaguesForDay).flat().length > 0
    )
  );
</script>

<style scoped>
  .sticky-date {
    position: sticky;
    top: 88px; /* navbar height */
    z-index: 10;
  }

  .sticky-league {
    position: sticky;
    top: calc(88px + 2.5rem); /* navbar height + date header height */
    z-index: 9;
  }
</style>
