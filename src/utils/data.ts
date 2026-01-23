import type { Fixture, Standing, Club, League } from './types';
import { format } from 'date-fns';

/* -------------------------------------------------------------------------- */
/* Date helpers (unix seconds only)                                            */
/* -------------------------------------------------------------------------- */

function fromUnixSeconds(ts: number): Date {
  return new Date(ts * 1000);
}

/* -------------------------------------------------------------------------- */
/* Formatting helpers                                                         */
/* -------------------------------------------------------------------------- */

export function formatDate(ts: number): string {
  return format(fromUnixSeconds(ts), 'EEE MMM d');
}

export function formatMonth(ts: number): string {
  return format(fromUnixSeconds(ts), 'MMMM yyyy');
}

export function formatTime(ts: number): string {
  return format(fromUnixSeconds(ts), 'h:mm a');
}

/* -------------------------------------------------------------------------- */
/* Sorting helpers                                                            */
/* -------------------------------------------------------------------------- */

export function sortByFixtureDate<
  T extends { fixtureDate: number }
>(items: T[] = []): T[] {
  return [...items].sort((a, b) => a.fixtureDate - b.fixtureDate);
}

/* -------------------------------------------------------------------------- */
/* Grouping helpers                                                           */
/* -------------------------------------------------------------------------- */

export function groupByDay<
  T extends { fixtureDate: number }
>(items: T[]): Record<string, T[]> {
  return items.reduce((acc, item) => {
    const key = format(fromUnixSeconds(item.fixtureDate), 'yyyy-MM-dd');
    if (!acc[key]) acc[key] = [];
    acc[key].push(item);
    return acc;
  }, {} as Record<string, T[]>);
}

export function groupByLeague<
  T extends { league_id: string }
>(items: T[]): Record<string, T[]> {
  return items.reduce((acc, item) => {
    if (!acc[item.league_id]) acc[item.league_id] = [];
    acc[item.league_id].push(item);
    return acc;
  }, {} as Record<string, T[]>);
}

export function groupByDayThenLeague<
  T extends { fixtureDate: number; league_id: string }
>(items: T[]): Record<string, Record<string, T[]>> {
  const sorted = sortByFixtureDate(items);
  const grouped: Record<string, Record<string, T[]>> = {};

  for (const item of sorted) {
    const dayKey = format(
      fromUnixSeconds(item.fixtureDate),
      'yyyy-MM-dd'
    );

    if (!grouped[dayKey]) grouped[dayKey] = {};
    if (!grouped[dayKey][item.league_id]) {
      grouped[dayKey][item.league_id] = [];
    }

    grouped[dayKey][item.league_id].push(item);
  }

  return grouped;
}

export function groupByMonthThenDay<
  T extends { fixtureDate: number }
>(items: T[]): Record<string, Record<string, T[]>> {
  const sorted = sortByFixtureDate(items);
  const grouped: Record<string, Record<string, T[]>> = {};

  for (const item of sorted) {
    const date = fromUnixSeconds(item.fixtureDate);
    const monthKey = format(date, 'yyyy-MM');
    const dayKey = format(date, 'yyyy-MM-dd');

    if (!grouped[monthKey]) grouped[monthKey] = {};
    if (!grouped[monthKey][dayKey]) grouped[monthKey][dayKey] = [];

    grouped[monthKey][dayKey].push(item);
  }

  return grouped;
}

/* -------------------------------------------------------------------------- */
/* JSON loading                                                               */
/* -------------------------------------------------------------------------- */

const jsonModules = import.meta.glob('/src/data/*/*/*.json', {
  eager: true,
}) as Record<string, any>;

function getJson<T>(slug: string, year: string, name: string): T {
  const key = `/src/data/${slug}/${year}/${name}.json`;
  const module = jsonModules[key];
  if (!module) throw new Error(`Missing JSON module: ${key}`);
  return module.default ?? module;
}

/* -------------------------------------------------------------------------- */
/* Public API                                                                 */
/* -------------------------------------------------------------------------- */

export async function loadUnionData(slug: string, year = '2025') {
  return {
    clubs: getJson<Record<string, Club>>(slug, year, 'clubs'),
    leagues: getJson<Record<string, League>>(slug, year, 'leagues'),
    fixtures: getJson<Record<string, Fixture[]>>(slug, year, 'fixtures'),
    standings: getJson<Record<string, Standing[]>>(slug, year, 'standings'),
  };
}

export async function prepareUnionData(slug: string, year = '2025') {
  const raw = await loadUnionData(slug, year);

  return {
    clubs: raw.clubs,
    leagues: raw.leagues,
    fixturesByLeague: raw.fixtures,
    // fixturesByLeague: Object.fromEntries(
    //   Object.entries(raw.fixtures).map(([leagueId, items]) => [
    //     leagueId,
    //     groupByDayThenLeague(items),
    //   ])
    // ),
    standingsByLeague: raw.standings,
  };
}
