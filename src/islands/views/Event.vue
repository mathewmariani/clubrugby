<template>
  <template v-if="match">
    <div class="list-group list-group-flush">
      <MatchHeader
        :leagueName="leagueName"
        :isResult="isResult"
        :time="match.time"
      />

      <TeamHeader
        :home="home"
        :away="away"
        :homeScore="Number(match.home_score)"
        :awayScore="Number(match.away_score)"
        :homeRecord="team1Record"
        :awayRecord="team2Record"
        :isResult="isResult"
      />

      <template v-if="!isResult">
        <div class="list-group-item">
          <div class="d-flex justify-content-between align-items-center my-3">
            <img :src="home?.logo_url" width="32" height="32" />
            <div class="d-flex flex-column text-center">
              <strong>Record</strong>
              <span class="text-muted">TOTAL</span>
            </div>
            <img :src="away?.logo_url" width="32" height="32" />
          </div>

          <MatchStatComparison
            v-for="stat in regularStats"
            :key="stat.key"
            :label="stat.label"
            :leftValue="getStatValue(team1, stat.key)"
            :rightValue="getStatValue(team2, stat.key)"
          />
        </div>

        <div class="list-group-item">
          <div class="d-flex justify-content-between align-items-center my-3">
            <img :src="home?.logo_url" width="32" height="32" />
            <div class="d-flex flex-column text-center">
              <strong>Stats</strong>
              <span class="text-muted">PER GAME</span>
            </div>
            <img :src="away?.logo_url" width="32" height="32" />
          </div>

          <MatchStatComparison
            v-for="stat in perGameStats"
            :key="stat.key"
            :label="stat.label"
            :leftValue="stat.team1"
            :rightValue="stat.team2"
            :leftRank="stat.team1Rank"
            :rightRank="stat.team2Rank"
          />
        </div>
      </template>

      <GameDetails
        :date="formatDate(match.date)"
        :time="formatTime(match.time)"
        :venue="match.venue"
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
  import { formatDate, formatTime } from '../../utils/data';
  import { getLeagueName, useMatchClubs } from '../../composables/utils';
  import MatchHeader from '../../components/vue/event/MatchHeader.vue';
  import TeamHeader from '../../components/vue/event/TeamHeader.vue';
  import GameDetails from '../../components/vue/event/GameDetails.vue';
  import MatchStatComparison from '../../components/vue/event/MatchStatComparison.vue';
  import type { Fixture, Result, Standing, Club, League } from '@/utils/types';

  const route = useRoute();

  const props = defineProps<{
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
    standings: Record<string, Standing[]>;
    fixtures: Record<string, Record<string, Fixture[]>>;
    results: Record<string, Record<string, Result[]>>;
  }>();

  const eventParts = computed(
    () => (route.params.event_id as string)?.split('-') || []
  );
  const leagueId = computed(() => eventParts.value[0]);
  const homeId = computed(() => eventParts.value[1]);
  const awayId = computed(() => eventParts.value[2]);
  const date = computed(() => eventParts.value.slice(3).join('-'));

  const match = computed(() => {
    const f = props.fixtures[date.value]?.[leagueId.value]?.find(
      (f) =>
        f.home_id.toString() === homeId.value &&
        f.away_id.toString() === awayId.value
    );
    if (f) return f;
    const r = props.results[date.value]?.[leagueId.value]?.find(
      (r) =>
        r.home_id.toString() === homeId.value &&
        r.away_id.toString() === awayId.value
    );
    return r ?? null;
  });

  const isResult = computed(() => match.value && 'home_score' in match.value);
  const leagueName = computed(() =>
    getLeagueName(leagueId.value, props.leagues)
  );
  const { home, away } = useMatchClubs(match, props.clubs);

  const team1 = computed(() =>
    props.standings[leagueId.value]?.find((s) => s.team_id === home.value?.id)
  );
  const team2 = computed(() =>
    props.standings[leagueId.value]?.find((s) => s.team_id === away.value?.id)
  );

  function getRecordString(team?: Standing): string {
    return `${Number(team?.w ?? 0)}-${Number(team?.d ?? 0)}-${Number(team?.l ?? 0)}`;
  }
  const team1Record = computed(() => getRecordString(team1.value));
  const team2Record = computed(() => getRecordString(team2.value));

  const regularStats = [
    { key: 'pld', label: 'Played' },
    { key: 'w', label: 'Wins' },
    { key: 'd', label: 'Draws' },
    { key: 'l', label: 'Losses' },
    { key: 'pts', label: 'Points' },
  ] as const;

  function getStatValue(
    team: Standing | undefined,
    key: keyof Standing
  ): number {
    return Number(team?.[key] ?? 0);
  }

  function perGame(team: Standing | undefined, key: keyof Standing): number {
    const played = Number(team?.pld ?? 0);
    const value = Number(team?.[key] ?? 0);
    return played > 0 ? value / played : 0;
  }

  function getPerGameRank(
    standings: Standing[] | undefined,
    teamId: string | undefined,
    key: keyof Standing
  ): number | null {
    if (!standings || !teamId) return null;
    const list = standings.map((t) => ({
      id: t.team_id,
      value: perGame(t, key),
    }));
    list.sort((a, b) => b.value - a.value);
    const index = list.findIndex((t) => t.id === teamId);
    return index >= 0 ? index + 1 : null;
  }

  const perGameStats = computed(() => {
    const keys = [
      { key: 'pf', label: 'Points For' },
      { key: 'pa', label: 'Points Against' },
      { key: 'tf', label: 'Tries For' },
      { key: 'ta', label: 'Tries Against' },
    ] as const;

    const standings = props.standings[leagueId.value];

    return keys.map(({ key, label }) => {
      const team1Val = team1.value ? perGame(team1.value, key) : 0;
      const team2Val = team2.value ? perGame(team2.value, key) : 0;
      return {
        key,
        label,
        team1: team1Val,
        team2: team2Val,
        team1Rank: getPerGameRank(standings, team1.value?.team_id, key),
        team2Rank: getPerGameRank(standings, team2.value?.team_id, key),
      };
    });
  });
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
