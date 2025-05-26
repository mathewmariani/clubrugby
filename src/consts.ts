export const SITE_TITLE = 'Club Rugby';
export const SITE_DESCRIPTION = '';

import Papa from 'papaparse';
import clubsCsv from './data/qc/2025/clubs.csv?raw';
import standingsCsv from './data/qc/2025/standings.csv?raw';
import resultsCsv from './data/qc/2025/results.csv?raw';
import scheduleCsv from './data/qc/2025/fixtures.csv?raw';
import leaguesCsv from './data/qc/2025/leagues.csv?raw';
import newsCsv from './data/qc/2025/news.csv?raw';

export const clubs = Papa.parse(clubsCsv, {
  header: true,
  skipEmptyLines: true,
}).data.reduce((acc, club) => {
  acc[club.id] = {
    id: club.id,
    name: club.name,
    logo: club.logo_url,
  };
  return acc;
}, {});

export const standings = Papa.parse(standingsCsv, {
  header: true,
  skipEmptyLines: true,
}).data.reduce((acc, row) => {
  const leagueId = row.league_id;
  const teamId = row.team_id;
  if (!acc[leagueId]) acc[leagueId] = {};
  acc[leagueId][teamId] = row;
  return acc;
}, {});

export const results = Papa.parse(resultsCsv, {
  header: true,
  skipEmptyLines: true,
}).data;

export const news = Papa.parse(newsCsv, {
  header: true,
  skipEmptyLines: true,
}).data;

export const schedule = Papa.parse(scheduleCsv, {
  header: true,
  skipEmptyLines: true,
}).data;

export const leagues = Papa.parse(leaguesCsv, {
  header: true,
  skipEmptyLines: true,
}).data.reduce((acc, row) => {
  acc[row.id] = row.name;
  return acc;
}, {});
