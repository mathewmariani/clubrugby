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
        :homeScore="fixture.homeScore"
        :awayScore="fixture.awayScore"
        :homeRecord="homeTeamRecord"
        :awayRecord="awayTeamRecord"
        :isResult="isResult"
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
              <div class="text-muted">TOTAL</div>
            </div>
            <img :src="away?.logo" />
          </div>
          <MatchStatComparison
            v-for="stat in regularStats"
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
              <div class="text-muted">PER GAME</div>
            </div>
            <img :src="away?.logo" />
          </div>
          <MatchStatComparison
            v-for="stat in perGameStats"
            :key="stat.key"
            :label="stat.label"
            :leftValue="getStatValue(homeTeam, stat.key)"
            :rightValue="getStatValue(awayTeam, stat.key)"
          />
        </div>
      </template>

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
      <p>No event was found.</p>
      <hr />
      <p>Ensure your preferences are set.</p>
    </div>
  </template>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router';
import { computed } from 'vue';

import { getLeagueName, useMatchClubs, useFixtureById, getRecordString } from '@/composables/utils';

import MatchHeader from '@/components/vue/event/MatchHeader.vue';
import TeamHeader from '@/components/vue/event/TeamHeader.vue';
import GameDetails from '@/components/vue/event/GameDetails.vue';
import MatchStatComparison from '@/components/vue/event/MatchStatComparison.vue';

import type { Fixture, Standing, Club } from '@/utils/types';

const props = defineProps<{
  clubs: Record<string, Club>;
  leagues: Record<string, string>;
  standings: Record<string, Standing[]>;
  fixtures: Record<string, Fixture[]>;
}>();

const route = useRoute();
const fixture_id = computed(() => route.params.event_id as string | undefined);

const { fixture, league_id } = useFixtureById(fixture_id, props.fixtures );
const { home, away } = useMatchClubs(fixture, props.clubs);
const isResult = computed(() => fixture.value?.fixtureStatus === 'result');

const leagueName = getLeagueName(league_id.value, props.leagues);
const homeTeamRecord = computed(() => getRecordString(homeTeam.value));
const awayTeamRecord = computed(() => getRecordString(awayTeam.value));

const standingsForLeague = computed(() =>
  props.standings[league_id.value] ?? []
);

const homeTeam = computed(() =>
  standingsForLeague.value.find(s => s.club_id === fixture.value?.homeClubId)
);

const awayTeam = computed(() =>
  standingsForLeague.value.find(s => s.club_id === fixture.value?.awayClubId)
);

const regularStats = [
  { key: 'played', label: 'Played' },
  { key: 'gamesWon', label: 'Wins' },
  { key: 'gamesDraw', label: 'Draws' },
  { key: 'gameLost', label: 'Losses' },
  { key: 'points', label: 'Points' },
] as const;

const perGameStats = [
  { key: 'pointsFor', label: 'Points For' },
  { key: 'pointsAgainst', label: 'Points Against' },
  { key: 'triesFor', label: 'Tries For' },
  { key: 'triesAgainst', label: 'Tries Against' },
] as const;

function getStatValue(team: Standing | undefined, key: keyof Standing): number {
  return Number(team?.[key] ?? 0);
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