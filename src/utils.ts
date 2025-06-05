import { startOfWeek, format } from 'date-fns';

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
  date: Date;
  time: Date;
  venue: string;
  home_id: string;
  away_id: string;
}

export interface Result {
  league_id: string;
  date: Date;
  time: Date;
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

export function groupFixturesByWeek(fixturesMap: FixturesMap): FixturesMap {
  const allFixtures = Object.values(fixturesMap).flat();

  const groupedByWeek: FixturesMap = {};

  for (const fixture of allFixtures) {
    const weekStart = startOfWeek(new Date(fixture.date), { weekStartsOn: 1 }); // Monday
    const key = format(weekStart, 'yyyy-MM-dd');

    if (!groupedByWeek[key]) {
      groupedByWeek[key] = [];
    }

    groupedByWeek[key].push(fixture);
  }

  // Optional: Sort fixtures within each week by date/time
  for (const week in groupedByWeek) {
    groupedByWeek[week].sort((a, b) => +new Date(a.date) - +new Date(b.date));
  }

  return groupedByWeek;
}

export function groupFixturesByDay(fixturesMap: FixturesMap): FixturesMap {
  const allFixtures = Object.values(fixturesMap).flat();

  const groupedByDay: FixturesMap = {};

  for (const fixture of allFixtures) {
    const dayKey = format(new Date(fixture.date), 'yyyy-MM-dd');

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

  for (const result of allResults) {
    const dayKey = format(new Date(result.date), 'yyyy-MM-dd');

    if (!groupedByDay[dayKey]) {
      groupedByDay[dayKey] = [];
    }

    groupedByDay[dayKey].push(result);
  }

  // Sort fixtures within each day by time (if time field exists and is meaningful)
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
