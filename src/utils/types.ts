export interface Club {
  id: string;
  name: string;
  logo_url: string;
}

export interface League {
  id: string;
  name: string;
}

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
