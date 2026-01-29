export interface Club {
  name: string;
  logo: string;
}

export interface Standing {
  league_id: string; // league the team belongs to
  club_id: string; // club identifier (maps to clubs)
  team_id: number; // team identifier (unique per league)
  pos: number; // rank / position
  played: number; // number of games played
  gamesWon: number; // games won
  gamesDraw: number; // games drawn
  gameLost: number; // games lost
  pointsFor: number; // total points scored
  pointsAgainst: number; // total points conceded
  pointsDifference: number; // pointsFor - pointsAgainst
  bonusPoints: number; // bonus points total
  points: number; // total points (used for ranking)
  triesFor: number; // total tries scored
  triesAgainst: number; // total tries conceded
  triesDifference: number; // triesFor - triesAgainst
  Pen: number; // penalty goals scored
  Conv: number; // conversions scored
  Drop: number; // drop goals scored
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
  fixtureId: string; // unique ID
  fixtureDate: number; // unix timestamp in seconds
  fixtureStatus: 'fixture' | 'result'; // result or upcoming

  seasonId: string; // optional for reference
  compYear: string;

  venue: string;
  venuePostalCode?: string;
  venuelat?: string;
  venuelng?: string;

  home: FixtureResultSummary;
  away: FixtureResultSummary;

  matchOfficials?: MatchOfficial[];
}
