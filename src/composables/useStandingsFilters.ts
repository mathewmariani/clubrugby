import { computed } from 'vue';
import type { Standing } from '@/types/appData';

export function useStandingsFilters(
  standings: Readonly<Record<string, readonly Standing[]>>
) {
  // always work from plain object
  const allStandings = computed(() => standings);

  function getStandingsForLeague(leagueId: string) {
    return {
      [leagueId]: standings[leagueId] ?? [],
    };
  }

  function getStandingsWithClub(clubId: string) {
    const standings: Record<string, readonly Standing[]> = {};

    for (const [leagueId, list] of Object.entries(allStandings.value)) {
      if (list.some((s) => s.club_id === clubId)) {
        standings[leagueId] = list;
      }
    }

    return standings;
  }

  function getClubInLeague(leagueId: string, clubId: string) {
    return standings[leagueId]?.find((s) => s.club_id === clubId) ?? null;
  }

  const hasStandings = computed(
    () => Object.keys(allStandings.value).length > 0
  );

  return {
    getClubInLeague,
    getStandingsWithClub,
    getStandingsForLeague,
    hasStandings,
  };
}