import { computed, unref, type MaybeRef } from 'vue';
import type { Standing } from '@/utils/types';

export function useStandingsFilters(
  standings: Record<string, Standing[]>,
  options?: {
    leagueId?: MaybeRef<string | undefined>;
  }
) {
  const filteredStandings = computed(() => {
    const leagueId = unref(options?.leagueId);

    if (!leagueId) return standings;

    const leagueStandings = standings[leagueId];

    return leagueStandings ? { [leagueId]: leagueStandings } : {};
  });

  const hasStandings = computed(
    () => Object.keys(filteredStandings.value).length > 0
  );

  return {
    standings: filteredStandings,
    hasStandings,
  };
}
