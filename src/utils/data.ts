import type { Fixture, Standing, Club } from './types';
import { format } from 'date-fns';

/* -------------------------------------------------------------------------- */
/* Formatting helpers                                                         */
/* -------------------------------------------------------------------------- */

function fromUnixSeconds(ts: number): Date {
  return new Date(ts * 1000);
}

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

export async function getUnionData(slug: string, year = '2025') {
  const [clubs, leagues, fixtures, standings] = await Promise.all([
    getJson<Record<string, Club>>(slug, year, 'clubs'),
    getJson<Record<string, Record<string, string>>>(slug, year, 'leagues'),
    getJson<Record<string, Fixture[]>>(slug, year, 'fixtures'),
    getJson<Record<string, Standing[]>>(slug, year, 'standings'),
  ]);

  return {
    clubs,
    leagues,
    fixtures,
    standings,
  };
}