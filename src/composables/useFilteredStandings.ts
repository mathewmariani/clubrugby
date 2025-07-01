import { computed, type Ref } from 'vue';
import type { Standing } from '@/utils/types';

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
        const sortFn = (a: Standing, b: Standing) => {
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
        };

        const hasDivisions = teams.some((team) => team.division);

        if (hasDivisions) {
          // Group teams by division
          const divisions: Record<string, Standing[]> = {};
          for (const team of teams) {
            const division = team.division || 'Unspecified';
            if (!divisions[division]) divisions[division] = [];
            divisions[division].push(team);
          }

          // Sort teams within each division
          const sortedDivisions = Object.entries(divisions).map(
            ([division, divisionTeams]) => ({
              division,
              teams: [...divisionTeams].sort(sortFn),
            })
          );

          return { leagueId, divisions: sortedDivisions };
        }

        // No divisions: return flat list
        const sorted = [...teams].sort(sortFn);
        return { leagueId, teams: sorted };
      });
  });

  const hasStandings = computed(() =>
    groupedStandings.value.some((group) => {
      if ('divisions' in group) {
        return group.divisions.some((d) => d.teams.length > 0);
      }
      return group.teams.length > 0;
    })
  );

  return {
    groupedStandings,
    hasStandings,
  };
}
