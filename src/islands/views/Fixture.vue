<template>
  <template v-if="fixture">
    <div class="list-group list-group-flush">
      <MatchHeader
        :leagueName="leagueName"
        :isResult="isResult"
        :fixtureDate="fixture.fixtureDate"
      />

      <!-- displays both home and away teams -->
      <TeamHeader
        :home="home"
        :away="away"
        :homeSummary="fixture.home"
        :awaySummary="fixture.away"
        :isResult="isResult"
      />

      <CalendarButton
        :fixture="fixture"
        :home="homeTeamName"
        :away="awayTeamName"
      />

      <!-- Pre-game comparison -->
      <template v-if="!isResult">
        <!-- Record Comparison -->
        <div class="list-group-item">
          <!-- NOTE: can be a component -->
          <div class="d-flex justify-content-between align-items-center my-3">
            <img :src="home?.logo" />
            <div class="text-center">
              <strong>Record</strong>
            </div>
            <img :src="away?.logo" />
          </div>
          <MatchStatComparison
            v-for="stat in recordStats"
            :key="stat.key"
            :label="stat.label"
            :leftValue="getStatValue(homeTeam, stat.key)"
            :rightValue="getStatValue(awayTeam, stat.key)"
          />
        </div>

        <!-- Stats Comparison -->
        <div class="list-group-item">
          <div class="d-flex justify-content-between align-items-center my-3">
            <img :src="home?.logo" />
            <div class="text-center">
              <strong>Stats</strong>
              <div class="text-muted">TOTAL</div>
            </div>
            <img :src="away?.logo" />
          </div>
          <MatchStatComparison
            v-for="stat in pointsTotalStats"
            :key="stat.key"
            :label="stat.label"
            :leftValue="getStatValue(homeTeam, stat.key)"
            :rightValue="getStatValue(awayTeam, stat.key)"
            :showBars="true"
          />
        </div>
        <div class="list-group-item">
          <div class="d-flex justify-content-between align-items-center my-3">
            <img :src="home?.logo" />
            <div class="text-center">
              <strong>Stats</strong>
              <div class="text-muted">PER GAME</div>
            </div>
            <img :src="away?.logo" />
          </div>
          <MatchStatComparison
            v-for="stat in pointsPerGameStats"
            :key="stat.key"
            :label="stat.label"
            :leftValue="getStatValuePerGame(homeTeam, stat.key)"
            :rightValue="getStatValuePerGame(awayTeam, stat.key)"
            :showBars="true"
          />
        </div>
      </template>

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
        :isResult="isResult"
      />
    </div>
  </template>

  <template v-else>
    <div class="container-fluid text-center text-muted pt-3">
      <p>No fixture was found.</p>
      <hr />
      <p>Ensure your preferences are set.</p>
    </div>
  </template>
</template>

<script setup lang="ts">
  import { useRoute } from 'vue-router';
  import { computed } from 'vue';

  import {
    getLeagueName,
    useMatchClubs,
    useFixtureById,
    getRecordString,
  } from '@/composables/utils';

  import MatchHeader from '@/components/vue/event/MatchHeader.vue';
  import BoxScore from '@/components/vue/event/BoxScore.vue';
  import MatchOfficials from '@/components/vue/event/MatchOfficials.vue';
  import TeamHeader from '@/components/vue/event/TeamHeader.vue';
  import GameDetails from '@/components/vue/event/GameDetails.vue';
  import MatchStatComparison from '@/components/vue/event/MatchStatComparison.vue';

  import type { Fixture, Standing, Club } from '@/utils/types';
  import CalendarButton from '@/components/vue/event/CalendarButton.vue';

  const props = defineProps<{
    clubs: Record<string, Club>;
    leagues: Record<string, string>;
    standings: Record<string, Standing[]>;
    fixtures: Record<string, Fixture[]>;
  }>();

  const route = useRoute();
  const fixture_id = computed(
    () => route.params.fixture_id as string | undefined
  );

  const { fixture, league_id } = useFixtureById(fixture_id, props.fixtures);
  const { home, away } = useMatchClubs(fixture, props.clubs);
  const isResult = computed(() => fixture.value?.fixtureStatus === 'result');

  const leagueName = getLeagueName(league_id.value, props.leagues);
  const homeTeamRecord = computed(() => getRecordString(homeTeam.value));
  const awayTeamRecord = computed(() => getRecordString(awayTeam.value));

  const standingsForLeague = computed(
    () => props.standings[league_id.value] ?? []
  );

  const homeTeam = computed(() =>
    standingsForLeague.value.find(
      (s) => s.club_id === fixture.value?.home.club_id
    )
  );

  const awayTeam = computed(() =>
    standingsForLeague.value.find(
      (s) => s.club_id === fixture.value?.away.club_id
    )
  );

  const homeTeamName = computed(
    () =>
      standingsForLeague.value.find(
        (s) => s.club_id === fixture.value?.home.club_id
      )?.name ?? 'Unknown'
  );

  const awayTeamName = computed(
    () =>
      standingsForLeague.value.find(
        (s) => s.club_id === fixture.value?.away.club_id
      )?.name ?? 'Unknown'
  );

  const hasMatchOfficials = computed(() => {
    return (
      fixture.value?.matchOfficials && fixture.value.matchOfficials.length > 0
    );
  });

  const recordStats = [
    { key: 'played', label: 'Played' },
    { key: 'gamesWon', label: 'Wins' },
    { key: 'gamesDraw', label: 'Draws' },
    { key: 'gameLost', label: 'Losses' },
    { key: 'points', label: 'Points' },
    { key: 'bonusPointsW', label: 'Offensive Bonus Points' },
    { key: 'bonusPointsL', label: 'Defensive Bonus Points' },
  ] as const;

  const pointsTotalStats = [
    { key: 'pointsFor', label: 'Points For' },
    { key: 'pointsAgainst', label: 'Points Against' },
    { key: 'triesFor', label: 'Tries For' },
    { key: 'triesAgainst', label: 'Tries Against' },
    { key: 'Conv', label: 'Conversions' },
    { key: 'Pen', label: 'Penalties' },
    { key: 'Drop', label: 'Drop Kicks' },
  ] as const;

  const pointsPerGameStats = [
    { key: 'triesFor', label: 'Tries For' },
    { key: 'triesAgainst', label: 'Tries Against' },
    { key: 'Conv', label: 'Conversions' },
    { key: 'Pen', label: 'Penalties' },
    { key: 'Drop', label: 'Drop Kicks' },
  ] as const;

  function getStatValue(team: Standing, key: keyof Standing): number {
    return Number(team[key]);
  }

  function getStatValuePerGame(team: Standing, key: keyof Standing): number {
    return Number(team[key]) / Number(team.played);
  }
</script>

<style scoped>
  .progress-stacked {
    height: 8px;
  }
  .sticky-match-header {
    position: sticky;
    z-index: 10;
  }
  img {
    width: 64px;
    height: 64px;
    object-fit: contain;
  }
</style>
