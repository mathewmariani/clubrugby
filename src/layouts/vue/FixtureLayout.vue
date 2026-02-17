<template>
  <div style="display: contents">
    <template v-if="fixture">
      <div class="list-group list-group-flush">
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

        <!-- Pre-game comparison -->
        <template v-if="!isResult">
          <div class="list-group-item">
            <div class="d-flex justify-content-between align-items-center my-3">
              <img :src="homeClub?.logo" />
              <div class="text-center"><strong>Record</strong></div>
              <img :src="awayClub?.logo" />
            </div>
            <MatchStatComparison
              v-for="stat in recordStats"
              :key="stat.key"
              :label="stat.label"
              :leftValue="getStatValue(homeStanding, stat.key)"
              :rightValue="getStatValue(awayStanding, stat.key)"
            />
          </div>

          <!-- Stats Comparison -->
          <div class="list-group-item">
            <div class="d-flex justify-content-between align-items-center my-3">
              <img :src="homeClub?.logo" />
              <div class="text-center">
                <strong>Stats</strong>
                <div class="text-muted">TOTAL</div>
              </div>
              <img :src="awayClub?.logo" />
            </div>
            <MatchStatComparison
              v-for="stat in pointsTotalStats"
              :key="stat.key"
              :label="stat.label"
              :leftValue="getStatValue(homeStanding, stat.key)"
              :rightValue="getStatValue(awayStanding, stat.key)"
              :showBars="true"
            />
          </div>

          <div class="list-group-item">
            <div class="d-flex justify-content-between align-items-center my-3">
              <img :src="homeClub?.logo" />
              <div class="text-center">
                <strong>Stats</strong>
                <div class="text-muted">PER GAME</div>
              </div>
              <img :src="awayClub?.logo" />
            </div>
            <MatchStatComparison
              v-for="stat in pointsPerGameStats"
              :key="stat.key"
              :label="stat.label"
              :leftValue="getStatValuePerGame(homeStanding, stat.key)"
              :rightValue="getStatValuePerGame(awayStanding, stat.key)"
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
          :venueLong="fixture.venuelng || ''"
          :venueLat="fixture.venuelat || ''"
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
  </div>
</template>

<script setup lang="ts">
  import { computed } from 'vue';
  import { SITE_TITLE } from '@/consts';

  import { useFixtureFilters } from '@/composables/useFixtureFilters';
  import { useStandingsFilters } from '@/composables/useStandingsFilters';
  import {
    useMatchClubs,
    getLeagueName,
    getClubStandings,
    getStatValuePerGame,
    rankByPerGame,
    getStatValue,
  } from '@/composables/utils';

  import MatchHeader from '@/components/vue/event/MatchHeader.vue';
  import TeamHeader from '@/components/vue/event/TeamHeader.vue';
  import CalendarButton from '@/components/vue/buttons/CalendarButton.vue';
  import BoxScore from '@/components/vue/event/BoxScore.vue';
  import MatchOfficials from '@/components/vue/event/MatchOfficials.vue';
  import GameDetails from '@/components/vue/event/GameDetails.vue';
  import MatchStatComparison from '@/components/vue/event/MatchStatComparison.vue';

  import { useAppData } from '@/composables/useAppData';
  const { union, clubs, leagues, fixtures, standings } = useAppData();

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

  const homeStanding = computed(() => {
    const league = league_id.value;
    const club = fixture.value?.home.club_id;

    return league && club ? getClubInLeague(league, club) : null;
  });

  const awayStanding = computed(() => {
    const league = league_id.value;
    const club = fixture.value?.away.club_id;

    return league && club ? getClubInLeague(league, club) : null;
  });

  // Officials
  const hasMatchOfficials = computed(
    () => (fixture.value?.matchOfficials?.length ?? 0) > 0
  );

  // Stats
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
</script>

<style scoped>
  img {
    width: 64px;
    height: 64px;
    object-fit: contain;
  }
</style>
