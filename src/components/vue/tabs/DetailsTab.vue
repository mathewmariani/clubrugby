<template>
  <template v-if="match">
    <div class="list-group list-group-flush">
      <div class="list-group-item">
        <!-- header home -->
        <div class="d-flex gap-3 mb-3 my-3">
          <img
            :src="home?.logo_url"
            alt=""
            width="64"
            height="64"
            style="object-fit: contain"
          />
          <div class="d-flex flex-column justify-content-center">
            <strong>{{ home?.name }}</strong>
            <p class="text-muted mb-0">{{ team1Record }}</p>
          </div>
        </div>
        <!-- header away -->
        <div class="d-flex gap-3 mb-3 my-3">
          <img
            :src="away?.logo_url"
            alt=""
            width="64"
            height="64"
            style="object-fit: contain"
          />
          <div class="d-flex flex-column justify-content-center">
            <strong>{{ away?.name }}</strong>
            <p class="text-muted mb-0">{{ team2Record }}</p>
          </div>
        </div>
      </div>

      <!-- stats -->
      <div class="list-group-item">
        <div class="d-flex justify-content-between my-3">
          <div class="d-flex flex-column justify-content-center">
            <img
              :src="home?.logo_url"
              alt=""
              width="32"
              height="32"
              style="object-fit: contain"
            />
          </div>
          <div class="d-flex flex-column justify-content-center text-center">
            <strong>Record</strong>
            <p class="text-muted mb-0">TOTAL</p>
          </div>
          <div class="d-flex flex-column justify-content-center">
            <img
              :src="away?.logo_url"
              alt=""
              width="32"
              height="32"
              style="object-fit: contain"
            />
          </div>
        </div>
        <div v-for="stat in regular_stats" :key="stat.key" class="mb-3">
          <div class="d-flex justify-content-between mb-1">
            <small>{{ getStatValue(team1, stat.key) }}</small>
            <small>{{ stat.label }}</small>
            <small>{{ getStatValue(team2, stat.key) }}</small>
          </div>
          <div class="progress-stacked">
            <div
              class="progress"
              role="progressbar"
              :style="{ width: leftWidth(stat) + '%' }"
            >
              <div class="progress-bar bg-primary"></div>
            </div>
            <div
              class="progress"
              role="progressbar"
              :style="{ width: rightWidth(stat) + '%' }"
            >
              <div class="progress-bar bg-warning"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- stats -->
      <div class="list-group-item">
        <div class="d-flex justify-content-between my-3">
          <div class="d-flex flex-column justify-content-center">
            <img :src="home?.logo_url" alt="" width="32" height="32" />
          </div>
          <div class="d-flex flex-column justify-content-center text-center">
            <strong>Stats</strong>
            <p class="text-muted mb-0">PER GAME</p>
          </div>
          <div class="d-flex flex-column justify-content-center">
            <img :src="away?.logo_url" alt="" width="32" height="32" />
          </div>
        </div>
        <div v-for="stat in perGameStats" :key="stat.key" class="mb-3">
          <div class="d-flex justify-content-between mb-1">
            <small
              >{{ stat.team1.toFixed(1) }}
              <small class="text-muted"
                >({{ getOrdinalSuffix(stat.team1Rank) }})</small
              ></small
            >
            <small>{{ stat.label }}</small>
            <small
              ><small class="text-muted"
                >({{ getOrdinalSuffix(stat.team2Rank) }})</small
              >
              {{ stat.team2.toFixed(1) }}</small
            >
          </div>
          <div class="progress-stacked">
            <div
              class="progress"
              role="progressbar"
              :style="{ width: perGameLeftWidth(stat) + '%' }"
            >
              <div class="progress-bar bg-primary"></div>
            </div>
            <div
              class="progress"
              role="progressbar"
              :style="{ width: perGameRightWidth(stat) + '%' }"
            >
              <div class="progress-bar bg-warning"></div>
            </div>
          </div>
        </div>
      </div>

      <!-- details -->
      <div class="list-group-item">
        <div class="mt-3">
          <h6><strong>Game Details</strong></h6>

          <strong>League:</strong>
          <p>{{ league_name }}</p>

          <strong>Date:</strong>
          <p>{{ formatDate(match?.date) }}, {{ formatTime(match?.time) }}</p>

          <strong>Venue:</strong>
          <p>{{ match?.venue }}</p>
        </div>
      </div>
    </div>
  </template>
  <template v-else class="text-center text-muted">
    <p>Please select a match from the Fixtures tab to compare teams.</p>
  </template>
</template>

<script setup lang="ts">
  import { computed, toRef } from 'vue';
  import { getOrdinalSuffix, getLeagueName } from '../../../composables/utils';
  import { useMatchClubs } from '../../../composables/utils';
  import { formatDate, formatTime } from '../../../utils/data';
  import type { Fixture, Standing, Club, League } from '../../../utils/types';

  const props = defineProps<{
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
    standings: Record<string, Standing[]>;
    match: Fixture | null;
  }>();

  const leagueId = computed(() => props.match?.league_id);
  const { home, away } = useMatchClubs(toRef(props, 'match'), props.clubs);

  const league_name = computed(() =>
    getLeagueName(leagueId.value, props.leagues)
  );

  const team1 = computed(() => {
    if (!leagueId.value || !home.value) return undefined;
    return props.standings[leagueId.value]?.find(
      (s) => s.team_id === home.value?.id
    );
  });

  const team2 = computed(() => {
    if (!leagueId.value || !away.value) return undefined;
    return props.standings[leagueId.value]?.find(
      (s) => s.team_id === away.value?.id
    );
  });

  const regular_stats: { key: keyof Standing; label: string }[] = [
    { key: 'pld', label: 'Played' },
    { key: 'w', label: 'Wins' },
    { key: 'd', label: 'Draws' },
    { key: 'l', label: 'Losses' },
    { key: 'pts', label: 'Points' },
  ];

  function getRecordString(team?: Standing): string {
    const w = Number(team?.w ?? 0);
    const d = Number(team?.d ?? 0);
    const l = Number(team?.l ?? 0);
    return `${w}-${d}-${l}`;
  }

  const team1Record = computed(() => getRecordString(team1.value));
  const team2Record = computed(() => getRecordString(team2.value));

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
    return total ? Math.round((t1 / total) * 100) : 50;
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
    leagueStandings: Standing[] | undefined,
    teamId: string | undefined,
    key: keyof Standing
  ): number | null {
    if (!leagueStandings || !teamId) return null;

    // Calculate per game for each team
    const teamsWithStats = leagueStandings.map((team) => ({
      team_id: team.team_id,
      value: team.pld > 0 ? Number(team[key]) / Number(team.pld) : 0,
    }));

    // Sort descending (higher is better)
    teamsWithStats.sort((a, b) => b.value - a.value);

    // Find rank (1-based)
    const rank = teamsWithStats.findIndex((t) => t.team_id === teamId);
    return rank === -1 ? null : rank + 1;
  }

  const perGameStats = computed(() => {
    const keys = [
      { key: 'pf', label: 'Points For' },
      { key: 'pa', label: 'Points Against' },
      { key: 'tf', label: 'Tries For' },
      { key: 'ta', label: 'Tries Against' },
    ] as const;

    const leagueStandings = leagueId.value
      ? props.standings[leagueId.value]
      : undefined;

    return keys.map(({ key, label }) => {
      const team1Value = team1.value ? perGame(team1.value, key) : 0;
      const team2Value = team2.value ? perGame(team2.value, key) : 0;

      const team1Rank = team1.value
        ? getPerGameRank(leagueStandings, team1.value.team_id, key)
        : null;
      const team2Rank = team2.value
        ? getPerGameRank(leagueStandings, team2.value.team_id, key)
        : null;

      return {
        key,
        label,
        team1: team1Value,
        team2: team2Value,
        team1Rank,
        team2Rank,
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
</style>
