<template>
  <template v-if="hasFixtures">
    <div class="list-group list-group-flush">
      <template v-for="(leaguesForDay, day) in filteredFixtures" :key="day">
        <strong class="list-group-item">{{ formatDate(day) }}</strong>
        <template v-for="(matches, leagueId) in leaguesForDay" :key="leagueId">
          <strong class="list-group-item">{{
            getLeagueName(leagueId, leagues)
          }}</strong>
          <FixtureListItem
            v-for="match in matches"
            :match="match"
            :clubs="props.clubs"
            :leagues="props.leagues"
            @click="handleMatchClick"
          />
        </template>
      </template>
    </div>
  </template>
  <!-- No fixtures fallback -->
  <template v-else>
    <div class="container mt-3 text-center text-muted">
      <p>No fixtures available.</p>
      <p>Ensure your preferences are set.</p>
    </div>
  </template>
</template>

<script setup lang="ts">
  import { computed } from 'vue';
  import FixtureListItem from '../items/FixtureListItem.vue';
  import type { Club, League, Fixture } from '../../../utils/types';
  import { formatDate } from '../../../utils/data';
  import { getLeagueName } from '../../../composables/utils';

  const props = defineProps<{
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
    fixtures: Record<string, Record<string, Fixture[]>>;
  }>();

  const emit = defineEmits<{
    (e: 'match-selected', match: Fixture): void;
  }>();

  import { toRef } from 'vue';
  import { useSavedLeagues } from '../../../composables/useSavedLeagues';
  import { useFilteredFixtures } from '../../../composables/useFilteredFixtures';

  const { savedLeagues } = useSavedLeagues();
  const filteredFixtures = useFilteredFixtures(
    toRef(props, 'fixtures'),
    savedLeagues
  );

  const hasFixtures = computed(() => {
    return Object.values(filteredFixtures.value).some(
      (leaguesForDay) => Object.values(leaguesForDay).flat().length > 0
    );
  });

  function handleMatchClick(match: Fixture) {
    emit('match-selected', match);
  }
</script>

<style scoped>
  .list-group {
    border-radius: 0;
  }
</style>
