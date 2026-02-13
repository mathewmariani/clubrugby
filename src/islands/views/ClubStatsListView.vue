<template>
  <template v-if="entries.length">
    <div>
      <div
        v-for="entry in entries"
        :key="entry.league"
        class="list-group list-group-flush"
      >
        <!-- Sticky league header -->
        <div class="sticky-league-name" :style="{ top: navbarHeight + 'px' }">
          <div class="list-group-header list-group-item bg-body-tertiary">
            {{ entry?.league }}
          </div>
        </div>

        <!-- Stats -->
        <div class="list-group-item">
          <div v-for="stat in PER_GAME_STATS" :key="stat.key" class="mb-3">
            <div class="d-flex mb-1">
              <small>{{ stat.label }}</small>
              <small class="ms-auto">
                {{ getStatValue(entry?.team, stat.key) }}
                <small class="text-body-secondary fw-light">
                  ()<!-- ({{ getOrdinalSuffix(stat.rank) }}) -->
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

  import type { Standing } from '@/utils/types';

  import { useAppData } from '@/composables/useAppData';
  const { leagues, standings } = useAppData();

  const { navbarHeight } = useLayout();
  const { savedLeagues } = useSavedLeagues();

  const props = defineProps<{
    clubId: string;
  }>();

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

  function getStatValue(
    team: Standing | undefined,
    key: keyof Standing
  ): number {
    return Number(team?.[key] ?? 0);
  }

  /* ---------------- helpers ---------------- */

  function perGame(team: Standing, key: keyof Standing): number {
    return team.pld > 0 ? Number(team[key]) / team.pld : 0;
  }

  function rankByPerGame(
    standings: Standing[],
    teamId: string,
    key: keyof Standing
  ): number | null {
    const ranked = standings
      .map((s) => ({ id: s.club_id, value: perGame(s, key) }))
      .sort((a, b) => b.value - a.value);

    const index = ranked.findIndex((t) => t.id === teamId);
    return index >= 0 ? index + 1 : null;
  }

  function relativeWidth(
    standings: Standing[],
    team: Standing,
    key: keyof Standing
  ): number {
    const values = standings.map((s) => perGame(s, key));
    const min = Math.min(...values);
    const max = Math.max(...values);
    const range = max - min;
    return range > 0 ? ((perGame(team, key) - min) / range) * 100 : 100;
  }

  /* ---------------- computed ---------------- */

  const entries = computed(() => {
    return Object.entries(standings)
      .map(([leagueId, standings]) => {
        const league = leagues[leagueId];
        const team = standings.find((s) => s.club_id === props.clubId);

        if (!league || !team) return null;

        return {
          league,
          team,
        };
      })
      .filter(Boolean);
  });
</script>

<style scoped>
  .sticky-league-name {
    position: sticky;
    z-index: 10;
    background-color: var(--bs-body-bg);
  }
</style>
