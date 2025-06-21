import Papa from 'papaparse';
import type { Fixture, Result, Standing, Club, League } from './types';
import { format, parseISO } from 'date-fns';

export function formatDate(dateStr: string): string {
  return format(parseISO(dateStr), 'EEE MMM d');
}

export function formatMonth(monthStr: string): string {
  return format(parseISO(monthStr + '-01'), 'MMMM yyyy'); // e.g. "June 2025"
}

export function formatTime(timeStr: string): string {
  const [hours, minutes] = timeStr.split(':').map(Number);
  const date = new Date();
  date.setHours(hours, minutes);
  return format(date, 'h:mm a');
}

const csvModules = import.meta.glob('/src/data/*/*/*.csv', {
  query: '?raw',
  eager: true,
}) as Record<string, string>;

function getCsv(slug: string, year: string, name: string): string {
  const key = `/src/data/${slug}/${year}/${name}.csv`;
  const module = csvModules[key];
  if (!module) throw new Error(`Missing CSV module: ${key}`);
  return typeof module === 'string' ? module : module.default;
}

function parseCsv<T>(raw: string): T[] {
  return Papa.parse<T>(raw, { header: true, skipEmptyLines: true }).data;
}

export function sortByDateTime<T extends { date: string; time?: string }>(
  items: T[] = []
): T[] {
  return [...items].sort((a, b) => {
    const aDate = new Date(`${a.date}T${a.time || '00:00'}`);
    const bDate = new Date(`${b.date}T${b.time || '00:00'}`);
    return aDate.getTime() - bDate.getTime();
  });
}

export function groupByDay<T extends { date: string }>(
  items: T[]
): Record<string, T[]> {
  return items.reduce(
    (acc, item) => {
      const day = item.date;
      if (!acc[day]) acc[day] = [];
      acc[day].push(item);
      return acc;
    },
    {} as Record<string, T[]>
  );
}

export function groupByLeague<T extends { league_id: string }>(
  items: T[]
): Record<string, T[]> {
  return items.reduce(
    (acc, item) => {
      if (!acc[item.league_id]) acc[item.league_id] = [];
      acc[item.league_id].push(item);
      return acc;
    },
    {} as Record<string, T[]>
  );
}

type Match = {
  league_id: string;
  date: string;
  time?: string;
  [key: string]: any;
};

export function groupByDayThenLeague<
  T extends { date: string; league_id: string },
>(items: T[]): Record<string, Record<string, T[]>> {
  const sorted = [...items].sort((a, b) => {
    const aTime = new Date(`${a.date}T${(a as any).time || '00:00'}`);
    const bTime = new Date(`${b.date}T${(b as any).time || '00:00'}`);
    return aTime.getTime() - bTime.getTime();
  });

  const grouped: Record<string, Record<string, T[]>> = {};

  for (const item of sorted) {
    const dayKey = format(parseISO(item.date), 'yyyy-MM-dd');
    if (!grouped[dayKey]) grouped[dayKey] = {};
    if (!grouped[dayKey][item.league_id]) grouped[dayKey][item.league_id] = [];
    grouped[dayKey][item.league_id].push(item);
  }

  return grouped;
}

export async function loadUnionData(slug: string, year = '2025') {
  return {
    clubs: parseCsv<Club>(getCsv(slug, year, 'clubs')),
    leagues: parseCsv<League>(getCsv(slug, year, 'leagues')),
    fixtures: parseCsv<Fixture>(getCsv(slug, year, 'fixtures')),
    results: parseCsv<Result>(getCsv(slug, year, 'results')),
    standings: parseCsv<Standing>(getCsv(slug, year, 'standings')),
  };
}

export async function prepareUnionData(slug: string, year = '2025') {
  const raw = await loadUnionData(slug, year);

  const clubsMap = Object.fromEntries(raw.clubs.map((c) => [c.id, c]));
  const leaguesMap = Object.fromEntries(raw.leagues.map((l) => [l.id, l]));

  return {
    clubs: clubsMap,
    leagues: leaguesMap,
    fixturesByLeague: groupByDayThenLeague(raw.fixtures),
    resultsByLeague: groupByDayThenLeague(raw.results),
    standingsByLeague: groupByLeague(raw.standings),
  };
}

export function groupByMonthThenDay<T extends { date: string }>(
  items: T[]
): Record<string, Record<string, T[]>> {
  const sorted = [...items].sort((a, b) => {
    const aTime = new Date(`${a.date}T${(a as any).time || '00:00'}`);
    const bTime = new Date(`${b.date}T${(b as any).time || '00:00'}`);
    return aTime.getTime() - bTime.getTime();
  });

  const grouped: Record<string, Record<string, T[]>> = {};

  for (const item of sorted) {
    const date = parseISO(item.date);
    const monthKey = format(date, 'yyyy-MM'); // e.g. "2025-06"
    const dayKey = format(date, 'yyyy-MM-dd'); // e.g. "2025-06-18"

    if (!grouped[monthKey]) grouped[monthKey] = {};
    if (!grouped[monthKey][dayKey]) grouped[monthKey][dayKey] = [];

    grouped[monthKey][dayKey].push(item);
  }

  return grouped;
}
