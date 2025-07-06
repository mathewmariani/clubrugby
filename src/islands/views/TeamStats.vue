<template>
  <template v-if="entries.length">
    <div>
      <template v-for="entry in entries" :key="entry.league.id">
        <!-- League wrapper to enable sticky league header to push -->
        <div class="list-group list-group-flush">
          <!-- Sticky league header -->
          <div class="sticky-league-name" :style="{ top: navbarHeight + 'px' }">
            <div class="list-group-header list-group-item bg-body-tertiary">
              {{ entry.league.name }}
            </div>
          </div>

          <!-- Stats section -->
          <div class="list-group-item">
            <div
              v-for="stat in entry.perGameStats"
              :key="stat.key"
              class="mb-3"
            >
              <div class="d-flex mb-1">
                <small>{{ stat.label }}</small>
                <small class="ms-auto">
                  {{ stat.team.toFixed(1) }}
                  <small class="text-body-secondary fw-light">
                    ({{ getOrdinalSuffix(stat.rank) }})
                  </small>
                </small>
              </div>
              <div class="progress-stacked">
                <div
                  class="progress"
                  :style="{
                    width: getPerGameRelativeWidth(stat, entry.standings) + '%',
                  }"
                >
                  <div class="progress-bar bg-primary"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </template>
    </div>
  </template>
</template>

<script setup lang="ts">
  import { computed } from 'vue';
  import { getOrdinalSuffix } from '@/composables/utils';
  import { useSavedLeagues } from '@/composables/useSavedLeagues';
  import type { Club, League, Standing } from '@/utils/types';
  import { useLayout } from '@/composables/useLayout';

  const { navbarHeight } = useLayout();

  const props = defineProps<{
    club_id: string;
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
    standings: Record<string, Standing[]>;
  }>();

  const { savedLeagues } = useSavedLeagues();

  const per_game_keys = [
    { key: 'pf', label: 'Points For' },
    { key: 'pa', label: 'Points Against' },
    { key: 'tf', label: 'Tries For' },
    { key: 'ta', label: 'Tries Against' },
  ] as const;

  function perGame(team: Standing, key: keyof Standing): number {
    return team.pld > 0 ? Number(team[key]) / team.pld : 0;
  }

  function averageOf(
    standings: Standing[],
    key: keyof Standing,
    excludeId: string
  ): number {
    const others = standings.filter((s) => s.team_id !== excludeId);
    const total = others.reduce((sum, s) => sum + Number(s[key] ?? 0), 0);
    return others.length ? total / others.length : 0;
  }

  function getPerGameRank(
    standings: Standing[],
    teamId: string,
    key: keyof Standing
  ): number | null {
    const ranked = standings
      .map((s) => ({ id: s.team_id, value: perGame(s, key) }))
      .sort((a, b) => b.value - a.value);
    const idx = ranked.findIndex((t) => t.id === teamId);
    return idx >= 0 ? idx + 1 : null;
  }

  const entries = computed(() => {
    const result = [];

    for (const [league_id, standings] of Object.entries(props.standings)) {
      // Filter by savedLeagues here
      if (savedLeagues.value.includes(league_id)) continue;

      const team = standings.find((s) => s.team_id === props.club_id);
      const league = props.leagues[league_id];
      if (!team || !league) continue;

      const avg: Partial<Record<keyof Standing, number>> = {};
      for (const { key } of per_game_keys) {
        avg[key] = averageOf(standings, key, team.team_id);
      }

      const perGameStats = per_game_keys.map(({ key, label }) => ({
        key,
        label,
        team: perGame(team, key),
        avg: avg[key] ?? 0,
        rank: getPerGameRank(standings, team.team_id, key),
      }));

      result.push({
        league,
        standings,
        team,
        perGameStats,
      });
    }

    return result;
  });

  function getPerGameRelativeWidth(
    stat: { team: number; key: keyof Standing },
    standings: Standing[]
  ): number {
    const values = standings.map((s) => perGame(s, stat.key));
    const min = Math.min(...values);
    const max = Math.max(...values);

    const range = max - min;
    const relative = stat.team - min;

    return range > 0 ? (relative / range) * 100 : 100;
  }
</script>

<style scoped>
  .sticky-league-name {
    position: sticky;
    top: 88px;
    z-index: 10;
    background-color: var(--bs-body-bg);
  }
</style>
