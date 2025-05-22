import { parseCsv, convertToISO } from './csvUtils';

async function fetchCsv(url, transform) {
  const text = await fetch(url).then((res) => res.text());
  return parseCsv(text, transform);
}

export async function loadClubs() {
  const clubs = await fetchCsv('/data/qc/2025/clubs.csv');
  return Object.fromEntries(
    clubs.map((club) => [club.id, { name: club.name, logo: club.logo_url }])
  );
}

export async function loadStandings() {
  const standings = await fetchCsv('/data/qc/2025/standings.csv');
  return Object.fromEntries(standings.map((row) => [row.team_id, row]));
}

export async function loadSchedule() {
  return fetchCsv('/data/qc/2025/schedule.csv', (m) => ({
    ...m,
    date_iso: convertToISO(m.date),
  }));
}

export async function loadResults() {
  return fetchCsv('/data/qc/2025/results.csv', (m) => ({
    ...m,
    date_iso: convertToISO(m.date),
  }));
}

export async function loadLeagues() {
  const leagues = await fetchCsv('/data/qc/2025/leagues.csv');
  return Object.fromEntries(leagues.map((l) => [l.id, l.name]));
}
*