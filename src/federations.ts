export type FederationSlug =
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
  | 'yt'; // Yukon

export type Federation = {
  slug: FederationSlug;
  name: string;
  url: string;
};

export const federations: Federation[] = [
  // {
  //   slug: 'ab',
  //   name: 'Rugby Alberta',
  //   url: 'https://rugbyalberta.com',
  // },
  // {
  //   slug: 'bc',
  //   name: 'British Columbia Rugby',
  //   url: 'https://www.bcrugby.com',
  // },
  // {
  //   slug: 'mb',
  //   name: 'Rugby Manitoba',
  //   url: 'https://rugbymanitoba.com',
  // },
  // {
  //   slug: 'nb',
  //   name: 'New Brunswick Rugby Union',
  //   url: 'https://www.rugbynb.ca',
  // },
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
  // {
  //   slug: 'sk',
  //   name: 'Saskatchewan Rugby',
  //   url: 'https://rugbysaskatchewan.com',
  // },
];

//
// This can all be redone
//

import Papa from 'papaparse';

// Glob all .csv files under federation/year folders relative to this file
const csvModules = import.meta.glob('./*/*/*/*.csv', {
  query: '?raw',
  eager: true,
}) as Record<string, string>;

function getCsv(slug: string, year: string, name: string): string {
  const key = `./data/${slug}/${year}/${name}.csv`;
  const module = csvModules[key];
  if (!module) throw new Error(`Missing CSV module: ${key}`);

  // unwrap the default export if present
  const csv = typeof module === 'string' ? module : module.default;

  if (!csv) throw new Error(`CSV content is empty or invalid for ${key}`);

  return csv;
}

function parseCsv(raw: string) {
  return Papa.parse(raw, { header: true, skipEmptyLines: true }).data;
}

export function loadFederationData(slug: string, year = '2025') {
  return {
    clubs: parseCsv(getCsv(slug, year, 'clubs')),
    results: parseCsv(getCsv(slug, year, 'results')),
    standings: parseCsv(getCsv(slug, year, 'standings')),
    schedule: parseCsv(getCsv(slug, year, 'fixtures')),
    leagues: parseCsv(getCsv(slug, year, 'leagues')),
  };
}
