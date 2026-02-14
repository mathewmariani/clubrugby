<template>
  <template v-if="enrichedEntries.length">
    <div>
      <div
        v-for="entry in enrichedEntries"
        :key="entry.leagueId"
        class="list-group list-group-flush"
      >
        <!-- Sticky league header -->
        <div class="sticky-league-name" :style="{ top: navbarHeight + 'px' }">
          <div class="list-group-header list-group-item bg-body-tertiary">
            {{ entry.league }}
          </div>
        </div>

        <!-- Stats -->
        <div class="list-group-item">
          <div v-for="stat in entry.stats" :key="stat.key" class="mb-3">
            <div class="d-flex mb-1">
              <small>{{ stat.label }}</small>

              <small class="ms-auto">
                {{ stat.value.toFixed(1) }}
                <small class="text-body-secondary fw-light">
                  ({{ stat.rank ? getOrdinalSuffix(stat.rank) : '' }})
                </small>
              </small>
            </div>

            <div class="progress-stacked">
              <div
                class="progress"
                :style="{ width: stat.relativeWidth + '%' }"
              >
                <div class="progress-bar bg-primary"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
</template>

<script setup lang="ts">
  import { computed } from 'vue';

  import { getOrdinalSuffix } from '@/composables/utils';
  import { useSavedLeagues } from '@/composables/useSavedLeagues';
  import { useLayout } from '@/composables/useLayout';
  import { useAppData } from '@/composables/useAppData';

  import type { Standing } from '@/types/appData';

  /* ---------------- props ---------------- */

  const props = defineProps<{
    clubId: string;
  }>();

  /* ---------------- app data ---------------- */

  const { leagues, standings } = useAppData();

  const { navbarHeight } = useLayout();
  const { savedLeagues } = useSavedLeagues();

  /* ---------------- constants ---------------- */

  const PER_GAME_STATS = [
    { key: 'pointsFor', label: 'Points For' },
    { key: 'pointsAgainst', label: 'Points Against' },
    { key: 'triesFor', label: 'Tries For' },
    { key: 'triesAgainst', label: 'Tries Against' },
    { key: 'Pen', label: 'Penalty Kicks' },
    { key: 'Drop', label: 'Drop Kicks' },
    { key: 'Conv', label: 'Conversions' },
  ] as const;

  /* ---------------- helpers ---------------- */

  function perGame(team: Standing, key: keyof Standing): number {
    return team.played > 0 ? Number(team[key]) / team.played : 0;
  }

  function rankByPerGame(
    leagueStandings: Readonly<Standing[]>,
    teamId: string,
    key: keyof Standing
  ): number | null {
    const ranked = leagueStandings
      .map((s) => ({
        id: s.club_id,
        value: perGame(s, key),
      }))
      .sort((a, b) => b.value - a.value);

    const index = ranked.findIndex((t) => t.id === teamId);
    return index >= 0 ? index + 1 : null;
  }

  function relativeWidth(
    leagueStandings: Readonly<Standing[]>,
    team: Standing,
    key: keyof Standing
  ): number {
    const values = leagueStandings.map((s) => perGame(s, key));
    const min = Math.min(...values);
    const max = Math.max(...values);

    const range = max - min;

    return range > 0 ? ((perGame(team, key) - min) / range) * 100 : 100;
  }

  /* ---------------- types ---------------- */

  type EnrichedStat = {
    key: keyof Standing;
    label: string;
    value: number;
    rank: number | null;
    relativeWidth: number;
  };

  type EnrichedEntry = {
    leagueId: string;
    league: string;
    team: Standing;
    stats: EnrichedStat[];
  };

  /* ---------------- computed ---------------- */

  const enrichedEntries = computed<EnrichedEntry[]>(() => {
    return Object.entries(standings)
      .map(([leagueId, leagueStandings]) => {
        const leagueName = leagues[leagueId];
        if (!leagueName) return null;

        const team = leagueStandings.find((s) => s.club_id === props.clubId);
        if (!team) return null;

        const stats: EnrichedStat[] = PER_GAME_STATS.map((stat) => ({
          key: stat.key,
          label: stat.label,
          value: perGame(team, stat.key),
          rank: rankByPerGame(leagueStandings, team.club_id, stat.key),
          relativeWidth: relativeWidth(leagueStandings, team, stat.key),
        }));

        return {
          leagueId,
          league: leagueName,
          team,
          stats,
        };
      })
      .filter((e): e is EnrichedEntry => e !== null);
  });
</script>

<style scoped>
  .sticky-league-name {
    position: sticky;
    z-index: 10;
    background-color: var(--bs-body-bg);
  }
</style>
