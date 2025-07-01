<template>
  <div v-if="hasFixtures">
    <DayMatchGroup
      v-for="(leaguesForDay, day) in filteredFixtures"
      :key="day"
      :day="day"
      :leagues-for-day="leaguesForDay"
      :clubs="clubs"
      :leagues="leagues"
      match-component="FixtureListItem"
    />
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
  import DayMatchGroup from '@/components/vue/DayMatchGroup.vue';
  import FixtureListItem from '@/components/vue/items/FixtureListItem.vue';
  import { useSavedLeagues } from '@/composables/useSavedLeagues';
  import { useFilteredMatches } from '@/composables/useFilteredMatches';
  import type { Club, League, Fixture } from '@/utils/types';
  import type { Union } from '@/utils/unions';

  const props = defineProps<{
    union: Union;
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
    fixtures: Record<string, Record<string, Fixture[]>>;
  }>();

  const clubs = toRef(props, 'clubs');
  const leagues = toRef(props, 'leagues');
  const fixtures = toRef(props, 'fixtures');
  const { savedLeagues } = useSavedLeagues();
  const filteredFixtures = useFilteredMatches(fixtures, savedLeagues);

  const hasFixtures = computed(() =>
    Object.values(filteredFixtures.value).some(
      (leaguesForDay) => Object.values(leaguesForDay).flat().length > 0
    )
  );
</script>
