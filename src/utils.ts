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
