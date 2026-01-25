import type { Fixture, Standing, Club } from './types';

const jsonModules = import.meta.glob('/src/data/*/*/*.json', {
  eager: true,
}) as Record<string, any>;

function getJson<T>(slug: string, year: string, name: string): T {
  const key = `/src/data/${slug}/${year}/${name}.json`;
  const module = jsonModules[key];
  if (!module) throw new Error(`Missing JSON module: ${key}`);
  return module.default ?? module;
}

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