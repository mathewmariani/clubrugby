<template>
  <template v-if="hasFixtures">
    <div class="list-group list-group-flush">
      <template v-for="(leaguesForDay, day) in filteredFixtures" :key="day">
        <div class="list-group-item bg-body-tertiary">
          <strong>{{ formatDate(day) }}</strong>
        </div>
        <template v-for="(matches, leagueId) in leaguesForDay" :key="leagueId">
          <div class="list-group-item bg-body-tertiary">
            <strong>{{ getLeagueName(leagueId, leagues) }}</strong>
          </div>
          <FixtureListItem
            v-for="match in matches"
            :key="match.id"
            :match="match"
            :clubs="clubs"
            :leagues="leagues"
          />
        </template>
      </template>
    </div>
  </template>
  <template v-else>
    <div class="container-fluid text-center text-muted pt-3">
      <p>No fixtures available.</p>
      <hr />
      <p>Ensure your preferences are set.</p>
    </div>
  </template>
</template>

<script lang="ts" setup>
  import { ref, computed, toRef, onMounted } from 'vue';
  import type { Club, League, Fixture } from '../../utils/types';

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
