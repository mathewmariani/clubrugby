<template>
  <template v-if="match">
    <div class="list-group list-group-flush">
      <!-- Sticky match header -->
      <div class="list-group-item bg-body-tertiary sticky-match-header">
        <div class="d-flex justify-content-between align-items-center">
          <strong>{{ league_name }}</strong>
          <template v-if="isResult()">
            <span class="badge text-bg-secondary">FINAL</span>
          </template>
          <template v-else>
            <span class="badge text-bg-danger">{{ match?.time }}</span>
          </template>
        </div>
      </div>

      <!-- Team headers -->
      <div class="list-group-item">
        <template v-if="isResult()">
          <div class="d-flex align-items-center justify-content-between my-3">
            <router-link :to="`/team/${home?.id}`" v-if="home">
              <img :src="home.logo_url" alt="" />
            </router-link>
            <EventScore
              :homeScore="Number(match?.home_score)"
              :awayScore="Number(match?.away_score)"
            />
            <router-link :to="`/team/${away?.id}`" v-if="away">
              <img :src="away.logo_url" alt="" />
            </router-link>
          </div>
        </template>
        <template v-else>
          <div class="d-flex gap-3 my-3">
            <router-link :to="`/team/${home?.id}`" v-if="home">
              <img :src="home.logo_url" alt="" />
            </router-link>
            <div class="d-flex flex-column justify-content-center">
              <h6>{{ home?.name }}</h6>
              <span class="text-muted">{{ team1Record }}</span>
            </div>
          </div>

          <div class="d-flex gap-3 mb-3 my-3">
            <router-link :to="`/team/${away?.id}`" v-if="away">
              <img :src="away.logo_url" alt="" />
            </router-link>
            <div class="d-flex flex-column justify-content-center">
              <h6>{{ away?.name }}</h6>
              <span class="text-muted">{{ team2Record }}</span>
            </div>
          </div>
        </template>
      </div>

      <!-- Regular stats (only for fixtures) -->
      <template v-if="!isResult()">
        <div class="list-group-item">
          <div class="d-flex justify-content-between align-items-center my-3">
            <img :src="home?.logo_url" width="32" height="32" />
            <div class="d-flex flex-column text-center">
              <strong>Record</strong>
              <span class="text-muted">TOTAL</span>
            </div>
            <img :src="away?.logo_url" width="32" height="32" />
          </div>

          <div v-for="stat in regular_stats" :key="stat.key" class="mb-3">
            <div class="d-flex justify-content-between mb-1">
              <small class="text-body-primary">{{
                getStatValue(team1, stat.key)
              }}</small>
              <small class="text-body-secondary">{{ stat.label }}</small>
              <small class="text-body-primary">{{
                getStatValue(team2, stat.key)
              }}</small>
            </div>
            <div class="progress-stacked">
              <div class="progress" :style="{ width: leftWidth(stat) + '%' }">
                <div class="progress-bar bg-primary"></div>
              </div>
              <div class="progress" :style="{ width: rightWidth(stat) + '%' }">
                <div class="progress-bar bg-warning"></div>
              </div>
            </div>
          </div>
        </div>

        <!-- Per Game Stats -->
        <div class="list-group-item">
          <div class="d-flex justify-content-between align-items-center my-3">
            <img :src="home?.logo_url" width="32" height="32" />
            <div class="d-flex flex-column text-center">
              <strong>Stats</strong>
              <span class="text-muted">PER GAME</span>
            </div>
            <img :src="away?.logo_url" width="32" height="32" />
          </div>

          <div v-for="stat in perGameStats" :key="stat.key" class="mb-3">
            <div class="d-flex justify-content-between mb-1">
              <small class="text-body-primary">
                {{ stat.team1.toFixed(1) }}
                <small class="text-body-secondary fw-light"
                  >({{ getOrdinalSuffix(stat.team1Rank) }})</small
                >
              </small>
              <small class="text-body-secondary">{{ stat.label }}</small>
              <small class="text-body-primary">
                <small class="text-body-secondary fw-light"
                  >({{ getOrdinalSuffix(stat.team2Rank) }})</small
                >
                {{ stat.team2.toFixed(1) }}
              </small>
            </div>
            <div class="progress-stacked">
              <div
                class="progress"
                :style="{ width: perGameLeftWidth(stat) + '%' }"
              >
                <div class="progress-bar bg-primary"></div>
              </div>
              <div
                class="progress"
                :style="{ width: perGameRightWidth(stat) + '%' }"
              >
                <div class="progress-bar bg-warning"></div>
              </div>
            </div>
          </div>
        </div>
      </template>

      <!-- Game Details -->
      <div class="list-group-item">
        <div class="d-flex flex-column mt-3">
          <h6>Game Details</h6>
          <span class="text-muted">Date</span>
          <p>{{ formatDate(match?.date) }}, {{ formatTime(match?.time) }}</p>

          <template v-if="!isResult()">
            <span class="text-muted">Venue</span>
            <p>{{ match?.venue }}</p>
          </template>
        </div>
      </div>
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
  import { computed, toRef } from 'vue';
  import { formatDate, formatTime } from '../../utils/data';
  import {
    getOrdinalSuffix,
    getLeagueName,
    useMatchClubs,
  } from '../../composables/utils';
  import type {
    Fixture,
    Result,
    Standing,
    Club,
    League,
  } from '../../utils/types';
  import EventScore from '../../components/vue/event/EventScore.vue';

  const route = useRoute();

  const props = defineProps<{
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
    standings: Record<string, Standing[]>;
    fixtures: Record<string, Record<string, Fixture[]>>;
    results: Record<string, Record<string, Result[]>>;
  }>();

  // Parse event_id into leagueId, homeId, awayId, date
  const eventParts = computed(
    () => (route.params.event_id as string)?.split('-') || []
  );

  const leagueId = computed(() => eventParts.value[0]);
  const homeId = computed(() => eventParts.value[1]);
  const awayId = computed(() => eventParts.value[2]);
  const date = computed(() => eventParts.value.slice(3).join('-')); // captures full date

  // Find match from fixtures or results
  const match = computed(() => {
    if (!leagueId.value || !homeId.value || !awayId.value || !date.value) {
      return null;
    }

    const fixturesOnDate = props.fixtures[date.value];
    if (fixturesOnDate) {
      const dayFixtures = fixturesOnDate[leagueId.value];
      if (dayFixtures) {
        const found = dayFixtures.find(
          (f) =>
            f.home_id.toString() === homeId.value &&
            f.away_id.toString() === awayId.value
        );
        if (found) {
          return found;
        }
      }
    }

    const resultsOnDate = props.results[date.value];
    if (resultsOnDate) {
      const dayResults = resultsOnDate[leagueId.value];
      if (dayResults) {
        const found = dayResults.find(
          (r) =>
            r.home_id.toString() === homeId.value &&
            r.away_id.toString() === awayId.value
        );
        if (found) {
          return found;
        }
      }
    }

    return null;
  });

  function isResult(): match is Result {
    const m = match.value;
    return !!m && 'home_score' in m && 'away_score' in m;
  }

  const league_name = computed(() =>
    getLeagueName(leagueId.value, props.leagues)
  );

  const { home, away } = useMatchClubs(match, props.clubs);

  const team1 = computed(() =>
    props.standings[leagueId.value]?.find((s) => s.team_id === home.value?.id)
  );
  const team2 = computed(() =>
    props.standings[leagueId.value]?.find((s) => s.team_id === away.value?.id)
  );

  const team1Record = computed(() => getRecordString(team1.value));
  const team2Record = computed(() => getRecordString(team2.value));

  function getRecordString(team?: Standing): string {
    const w = Number(team?.w ?? 0);
    const d = Number(team?.d ?? 0);
    const l = Number(team?.l ?? 0);
    return `${w}-${d}-${l}`;
  }

  const regular_stats = [
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
    return Number(team?.[key]);
  }

  function leftWidth(stat: { key: keyof Standing }): number {
    const t1 = getStatValue(team1.value, stat.key);
    const t2 = getStatValue(team2.value, stat.key);
    const total = t1 + t2;
    return total ? (t1 / total) * 100 : 50;
  }

  function rightWidth(stat: { key: keyof Standing }): number {
    return 100 - leftWidth(stat);
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

  function perGameLeftWidth(stat: { team1: number; team2: number }): number {
    const total = stat.team1 + stat.team2;
    return total ? (stat.team1 / total) * 100 : 50;
  }

  function perGameRightWidth(stat: { team1: number; team2: number }): number {
    return 100 - perGameLeftWidth(stat);
  }
</script>

<style scoped>
  .progress-stacked {
    height: 8px;
  }

  .sticky-match-header {
    position: sticky;
    top: 88px; /* adjust based on your navbar height */
    z-index: 10;
  }

  img {
    width: 64px;
    height: 64px;
    object-fit: contain;
  }
</style>
