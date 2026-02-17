<template>
  <div v-if="fixture" class="list-group list-group-flush">
    <MatchHeader
      :leagueName="leagueName"
      :isResult="isResult"
      :fixtureDate="fixture.fixtureDate"
    />

    <!-- displays both home and away teams -->
    <TeamHeader
      :home="homeClub"
      :away="awayClub"
      :homeSummary="fixture.home"
      :awaySummary="fixture.away"
      :isResult="isResult"
    />

    <CalendarButton v-if="!isResult" :fixture="fixture" />

    <!-- post game boxscore -->
    <BoxScore v-if="isResult" :home="fixture.home" :away="fixture.away" />

    <MatchOfficials
      v-if="hasMatchOfficials"
      :matchOfficial="fixture.matchOfficials || []"
    />

    <GameDetails
      :fixtureDate="fixture.fixtureDate"
      :league="leagueName"
      :venue="fixture.venue"
      :venueLong="fixture.venuelng || ''"
      :venueLat="fixture.venuelat || ''"
      :isResult="isResult"
    />
  </div>

  <div v-else class="container-fluid text-center text-muted pt-3">
    <p>No fixture was found.</p>
  </div>
</template>

<script setup lang="ts">
  import { computed } from 'vue';
  import { useFixtureFilters } from '@/composables/useFixtureFilters';
  import { useStandingsFilters } from '@/composables/useStandingsFilters';
  import { useMatchClubs, getLeagueName } from '@/composables/utils';

  import MatchHeader from '@/components/vue/event/MatchHeader.vue';
  import TeamHeader from '@/components/vue/event/TeamHeader.vue';
  import CalendarButton from '@/components/vue/buttons/CalendarButton.vue';
  import BoxScore from '@/components/vue/event/BoxScore.vue';
  import MatchOfficials from '@/components/vue/event/MatchOfficials.vue';
  import GameDetails from '@/components/vue/event/GameDetails.vue';

  import { useAppData } from '@/composables/useAppData';
  const { clubs, leagues, fixtures, standings } = useAppData();

  const props = defineProps<{
    fixtureId: string;
  }>();

  // --- Composables ---
  const { fixture, league_id } = useFixtureFilters(fixtures).useFixtureById(
    props.fixtureId
  );
  const { home: homeClub, away: awayClub } = useMatchClubs(fixture, clubs);
  const isResult = computed(() => fixture.value?.fixtureStatus === 'result');

  // League name
  const leagueName = computed(() => getLeagueName(league_id.value, leagues));

  const { getClubInLeague } = useStandingsFilters(standings);

  // Officials
  const hasMatchOfficials = computed(
    () => (fixture.value?.matchOfficials?.length ?? 0) > 0
  );
</script>

<style scoped>
  img {
    width: 64px;
    height: 64px;
    object-fit: contain;
  }
</style>
