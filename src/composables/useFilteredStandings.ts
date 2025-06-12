import { computed, type Ref } from 'vue';
import type { Standing } from '../utils/types';

export function useFilteredStandings(
  standings: Ref<Record<string, Standing[]>>,
  savedLeagues: Ref<string[]>,
  sortColumn: Ref<keyof Standing>,
  sortDirection: Ref<'asc' | 'desc'>
) {
  const groupedStandings = computed(() => {
    return Object.entries(standings.value)
      .filter(
        ([leagueId]) =>
          savedLeagues.value.length === 0 ||
          !savedLeagues.value.includes(leagueId)
      )
      .map(([leagueId, teams]) => {
        const sorted = [...teams].sort((a, b) => {
          const valA = a[sortColumn.value];
          const valB = b[sortColumn.value];

          if (valA === valB) {
            if (sortColumn.value !== 'pts') {
              const ptsDiff = b.pts - a.pts;
              if (ptsDiff !== 0) return ptsDiff;
              return b.diff - a.diff;
            }
            return b.diff - a.diff;
          }

          return sortDirection.value === 'asc'
            ? Number(valA) - Number(valB)
            : Number(valB) - Number(valA);
        });

        return { leagueId, teams: sorted };
      });
  });

  const hasStandings = computed(() =>
    groupedStandings.value.some((group) => group.teams.length > 0)
  );

  return {
    groupedStandings,
    hasStandings,
  };
}
