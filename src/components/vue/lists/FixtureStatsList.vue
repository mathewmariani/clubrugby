<template>
  <div v-if="fixture" class="list-group list-group-flush">
    <!-- Pre-game comparison -->
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
  </div>

  <div v-else class="container-fluid text-center text-muted pt-3">
    <p>No fixture was found.</p>
  </div>
</template>

<script setup lang="ts">
  import { computed } from 'vue';
  import { useFixtureFilters } from '@/composables/useFixtureFilters';
  import { useStandingsFilters } from '@/composables/useStandingsFilters';
  import {
    useMatchClubs,
    getStatValuePerGame,
    getStatValue,
  } from '@/composables/utils';

  import MatchStatComparison from '@/components/vue/event/MatchStatComparison.vue';

  import { useAppData } from '@/composables/useAppData';
  const { clubs, fixtures, standings } = useAppData();

  const props = defineProps<{
    fixtureId: string;
  }>();

  // --- Composables ---
  const { fixture, league_id } = useFixtureFilters(fixtures).useFixtureById(
    props.fixtureId
  );
  const { home: homeClub, away: awayClub } = useMatchClubs(fixture, clubs);

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
