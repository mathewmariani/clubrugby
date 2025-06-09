<template>
  <template v-if="match">
    <div class="list-group list-group-flush">
      <div class="list-group-item">
        <!-- header home -->
        <div class="d-flex gap-3 mb-3 my-3">
          <img :src="club1?.logo_url" alt="" width="64" height="64" />
          <div class="d-flex flex-column justify-content-center">
            <strong>{{ club1.name }}</strong>
            <p class="text-muted mb-0">{{ team1Record }}</p>
          </div>
        </div>
        <!-- header away -->
        <div class="d-flex gap-3 mb-3 my-3">
          <img :src="club2?.logo_url" alt="" width="64" height="64" />
          <div class="d-flex flex-column justify-content-center">
            <strong>{{ club2.name }}</strong>
            <p class="text-muted mb-0">{{ team2Record }}</p>
          </div>
        </div>
      </div>

      <!-- stats -->
      <div class="list-group-item">
        <div class="d-flex justify-content-between mb-3 my-3">
          <div class="d-flex flex-column justify-content-center">
            <img :src="club1?.logo_url" alt="" width="32" height="32" />
          </div>
          <div class="d-flex flex-column justify-content-center text-center">
            <strong>Record</strong>
            <p class="text-muted mb-0">TOTAL</p>
          </div>
          <div class="d-flex flex-column justify-content-center">
            <img :src="club2?.logo_url" alt="" width="32" height="32" />
          </div>
        </div>
        <div v-for="stat in regular_stats" :key="stat.key" class="mb-3">
          <div class="d-flex justify-content-between mb-1">
            <small>{{ team1?.[stat.key] ?? 0 }}</small>
            <small>{{ stat.label }}</small>
            <small>{{ team2?.[stat.key] ?? 0 }}</small>
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
        <div class="d-flex justify-content-between mb-3 my-3">
          <div class="d-flex flex-column justify-content-center">
            <img :src="club1?.logo_url" alt="" width="32" height="32" />
          </div>
          <div class="d-flex flex-column justify-content-center text-center">
            <strong>Stats</strong>
            <p class="text-muted mb-0">PER GAME</p>
          </div>
          <div class="d-flex flex-column justify-content-center">
            <img :src="club2?.logo_url" alt="" width="32" height="32" />
          </div>
        </div>
        <div v-for="stat in perGameStats" :key="stat.key" class="mb-3">
          <div class="d-flex justify-content-between mb-1">
            <small>{{ stat.team1.toFixed(1) }}</small>
            <small>{{ stat.label }}</small>
            <small>{{ stat.team2.toFixed(1) }}</small>
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
        <h6><strong>Game Details</strong></h6>

        <strong>League:</strong>
        <p>{{ league_name }}</p>

        <strong>Date:</strong>
        <p>{{ formatDate(match?.date) }} {{ formatTime(match?.time) }}</p>
        
        <strong>Venue:</strong>
        <p>{{ match?.venue }}</p>
      </div>
    </div>
  </template>
  <template v-else class="text-center text-muted">
    <p>Please select a match from the Fixtures tab to compare teams.</p>
  </template>
</template>

<script setup lang="ts">
  import { computed } from 'vue';
  import { formatDate, formatTime } from '../../../utils/data';
  import type { Fixture, Standing, Club, League } from '../../../utils/types';

  const props = defineProps<{
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
    standings: Standing;
    match: Fixture | null;
  }>();

  const team1 = computed(
    () =>
      props.standings[props.match.league_id].find(
        (s) => s.team_id === props.match?.home_id
      )!
  );
  const team2 = computed(
    () =>
      props.standings[props.match.league_id].find(
        (s) => s.team_id === props.match?.away_id
      )!
  );

  const club1 = computed(() => props.clubs[props.match?.home_id]);
  const club2 = computed(() => props.clubs[props.match?.away_id]);
  const league_name = computed(
    () => props.leagues[props.match?.league_id].name
  );

  const regular_stats = [
    { key: 'gp', label: 'Played' },
    { key: 'w', label: 'Wins' },
    { key: 'd', label: 'Draws' },
    { key: 'l', label: 'Losses' },
    { key: 'pts', label: 'Points' },
    // { key: 'pf', label: 'For' },
    // { key: 'pa', label: 'Against' },
    // { key: 'diff', label: 'Points Diff' },
    // { key: 'tf', label: 'Tries For' },
    // { key: 'ta', label: 'Tries Against' },
    // { key: 'td', label: 'Try Diff' },
  ];

  function getRecordString(team: Standing): string {
    const w = Number(team.w);
    const d = Number(team.d);
    const l = Number(team.l);
    return `${w}-${d}-${l}`;
  }

  const team1Record = computed(() => getRecordString(team1.value));
  const team2Record = computed(() => getRecordString(team2.value));

  function leftWidth(stat: { key: keyof Standing }) {
    const team1Value = Number(team1.value?.[stat.key] ?? 0);
    const team2Value = Number(team2.value?.[stat.key] ?? 0);
    const total = team1Value + team2Value;

    if (!total) return 50;

    const left = Math.round((team1Value / total) * 100);
    return left;
  }

  function rightWidth(stat: { key: keyof Standing }) {
    const left = leftWidth(stat); // use consistent logic
    return 100 - left;
  }

  // Per game utility
  function perGame(team: Standing, key: keyof Standing): number {
    const played = Number(team.gp);
    const value = Number(team[key]);
    return played > 0 ? value / played : 0;
  }

  // Per game stats
  const perGameStats = computed(() => {
    const keys = [
      { key: 'pf', label: 'Points For' },
      { key: 'pa', label: 'Points Against' },
      { key: 'tf', label: 'Tries For' },
      { key: 'ta', label: 'Tries Against' },
    ] as const;

    return keys.map(({ key, label }) => ({
      key,
      label,
      team1: perGame(team1.value, key),
      team2: perGame(team2.value, key),
    }));
  });

  function perGameLeftWidth(stat: { team1: number; team2: number }) {
    const total = stat.team1 + stat.team2;
    return total ? (stat.team1 / total) * 100 : 50;
  }

  function perGameRightWidth(stat: { team1: number; team2: number }) {
    const total = stat.team1 + stat.team2;
    return total ? (stat.team2 / total) * 100 : 50;
  }
</script>

<style scoped>
  .progress-stacked {
    height: 8px;
  }
</style>
