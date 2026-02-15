import type { InjectionKey } from 'vue';

export type UnionSlug =
  | 'ab' // Alberta
  | 'bc' // British Columbia
  | 'mb' // Manitoba
  | 'nb' // New Brunswick
  | 'nl' // Newfoundland and Labrador
  | 'ns' // Nova Scotia
  | 'nt' // Northwest Territories
  | 'nu' // Nunavut
  | 'on' // Ontario
  | 'pe' // Prince Edward Island
  | 'qc' // Quebec
  | 'sk' // Saskatchewan
  | 'yt' // Yukon
  | 'rseq'; // RSEQ

export type Union = {
  slug: UnionSlug;
  name: string;
  url: string;
};

export const unions: Union[] = [
  {
    slug: 'ab',
    name: 'Rugby Alberta',
    url: 'https://rugbyalberta.com',
  },
  {
    slug: 'bc',
    name: 'British Columbia Rugby',
    url: 'https://www.bcrugby.com',
  },
  {
    slug: 'mb',
    name: 'Rugby Manitoba',
    url: 'https://rugbymanitoba.com',
  },
  {
    slug: 'nb',
    name: 'New Brunswick Rugby Union',
    url: 'https://www.rugbynb.ca',
  },
  // {
  //   slug: 'nl',
  //   name: 'Newfoundland Rugby Union',
  //   url: 'https://sportnl.ca/member/rugby-nl/',
  // },
  {
    slug: 'ns',
    name: 'Rugby Nova Scotia',
    url: 'https://rugbyns.ns.ca',
  },
  // {
  //   slug: 'nt',
  //   name: 'Rugby North',
  //   url: 'https://rugbycanada.ca',
  // },
  {
    slug: 'on',
    name: 'Rugby Ontario',
    url: 'https://rugbyontario.com',
  },
  // {
  //   slug: 'pe',
  //   name: 'PEI Rugby Union',
  //   url: 'https://rugtypei.com',
  // },
  {
    slug: 'qc',
    name: 'Rugby Quebec',
    url: 'https://www.rugbyquebec.com',
  },
  {
    slug: 'sk',
    name: 'Saskatchewan Rugby',
    url: 'https://rugbysaskatchewan.com',
  },
  // {
  //   slug: 'rseq',
  //   name: 'RSEQ',
  //   url: 'https://rugbysaskatchewan.com',
  // },
];

export interface Club {
  name: string;
  logo: string;
}

export interface Standing {
  league_id: string;
  club_id: string;
  team_id: string;
  pos: string;
  played: string;
  gamesWon: string;
  gamesDraw: string;
  gameLost: string;
  pointsFor: string;
  pointsAgainst: string;
  pointsDifference: string;
  bonusPoints: string;
  bonusPointsW: string;
  bonusPointsL: string;
  points: string;
  triesFor: string;
  triesAgainst: string;
  triesDifference: string;
  Pen: string;
  Conv: string;
  Drop: string;
}

export interface MatchOfficial {
  role: string;
  name: string;
}

export interface FixtureResultSummary {
  team_id: string;
  club_id: string;
  score: string;
  drop: string;
  pen: string;
  conv: string;
  result: 'win' | 'lose' | 'draw' | null;
}

export interface Fixture {
  fixtureId: string;
  fixtureDate: number;
  fixtureStatus: 'fixture' | 'result';
  seasonId: string;
  compYear: string;
  venue: string;
  venuePostalCode: string;
  venuelat: string;
  venuelng: string;
  home: FixtureResultSummary;
  away: FixtureResultSummary;
  matchOfficials: MatchOfficial[];
}

export interface AppData {
  readonly union: Union;
  readonly clubs: Readonly<Record<string, Club>>;
  readonly leagues: Readonly<Record<string, string>>;
  readonly fixtures: Readonly<Record<string, readonly Fixture[]>>;
  readonly standings: Readonly<Record<string, readonly Standing[]>>;
}

export const appDataKey: InjectionKey<AppData> = Symbol('appData');
