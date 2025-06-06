import { startOfWeek, parseISO, format } from 'date-fns';

export interface Standing {
  league_id: string;
  team_id: string;
  pos: number;
  pld: number;
  w: number;
  d: number;
  l: number;
  pf: number;
  pa: number;
  diff: number;
  tf: number;
  ta: number;
  td: number;
  pts: number;
}

export interface Fixture {
  league_id: string;
  date: string;
  time: string;
  venue: string;
  home_id: string;
  away_id: string;
}

export interface Result {
  league_id: string;
  date: string;
  time: string;
  venue: string;
  home_id: string;
  home_score: string;
  away_id: string;
  away_score: string;
}

export type StandingsMap = Record<string, Standing[]>;
export type FixturesMap = Record<string, Fixture[]>;
export type ResultsMap = Record<string, Result[]>;

export function groupStandingsByLeague(standings: Standing[]): StandingsMap {
  return standings.reduce<StandingsMap>((acc, standing) => {
    if (!acc[standing.league_id]) {
      acc[standing.league_id] = [];
    }
    acc[standing.league_id].push(standing);
    return acc;
  }, {});
}

export function groupFixturesByLeague(fixtures: Fixture[]): FixturesMap {
  return fixtures.reduce<FixturesMap>((acc, fixture) => {
    if (!acc[fixture.league_id]) {
      acc[fixture.league_id] = [];
    }
    acc[fixture.league_id].push(fixture);
    return acc;
  }, {});
}

export function groupResultsByLeague(results: Result[]): ResultsMap {
  return results.reduce<ResultsMap>((acc, result) => {
    if (!acc[result.league_id]) {
      acc[result.league_id] = [];
    }
    acc[result.league_id].push(result);
    return acc;
  }, {});
}

export function groupFixturesByDay(fixturesMap: FixturesMap): FixturesMap {
  const allFixtures = Object.values(fixturesMap).flat();
  const groupedByDay: FixturesMap = {};

  for (const fixture of allFixtures) {
    const dayKey = format(parseISO(fixture.date), 'yyyy-MM-dd');

    if (!groupedByDay[dayKey]) {
      groupedByDay[dayKey] = [];
    }

    groupedByDay[dayKey].push(fixture);
  }

  // Sort fixtures within each day by time (if time field exists and is meaningful)
  for (const day in groupedByDay) {
    groupedByDay[day].sort((a, b) => +new Date(a.time) - +new Date(b.time));
  }

  return Object.fromEntries(
    Object.entries(groupedByDay).sort(([a], [b]) => a.localeCompare(b))
  );
}

export function groupResultsByDay(resultsMap: ResultsMap): ResultsMap {
  const allResults = Object.values(resultsMap).flat();
  const groupedByDay: ResultsMap = {};

  for (const results of allResults) {
    const dayKey = format(parseISO(results.date), 'yyyy-MM-dd');

    if (!groupedByDay[dayKey]) {
      groupedByDay[dayKey] = [];
    }

    groupedByDay[dayKey].push(results);
  }

  for (const day in groupedByDay) {
    groupedByDay[day].sort((a, b) => +new Date(a.time) - +new Date(b.time));
  }

  return Object.fromEntries(
    Object.entries(groupedByDay).sort(([a], [b]) => a.localeCompare(b))
  );
}

export function formatDate(iso: string): string {
  const [year, month, day] = iso.split('-').map(Number);
  const date = new Date(year, month - 1, day);
  return date.toLocaleDateString('en-US', {
    weekday: 'short',
    month: 'short',
    day: '2-digit',
  });
}

export function filterGroupedBySavedLeagues(
  grouped: FixturesMap,
  saved: string[]
): FixturesMap {
  const result: FixturesMap = {};
  for (const leagueId of saved) {
    if (grouped[leagueId]?.length) {
      result[leagueId] = grouped[leagueId];
    }
  }
  return result;
}

import { useSavedLeagues } from './composables/useSavedLeagues';
import { computed } from 'vue';

export function useFilteredFixtures(fixtures: Ref<Fixture[]>) {
  const { savedLeagues } = useSavedLeagues();

  const groupedFixtures = computed(() => groupFixturesByLeague(fixtures.value));

  const filteredGroupedFixtures = computed<FixturesMap>(() => {
    const result: FixturesMap = {};
    for (const leagueId of savedLeagues.value) {
      if (groupedFixtures.value[leagueId]?.length) {
        result[leagueId] = groupedFixtures.value[leagueId];
      }
    }
    return result;
  });

  return {
    groupedFixtures,
    filteredGroupedFixtures,
    savedLeagues,
  };
}
