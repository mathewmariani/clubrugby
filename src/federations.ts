export type FederationSlug =
  | 'ab'  // Alberta
  | 'bc'  // British Columbia
  | 'mb'  // Manitoba
  | 'nb'  // New Brunswick
  | 'nl'  // Newfoundland and Labrador
  | 'ns'  // Nova Scotia
  | 'nt'  // Northwest Territories
  | 'nu'  // Nunavut
  | 'on'  // Ontario
  | 'pe'  // Prince Edward Island
  | 'qc'  // Quebec
  | 'sk'  // Saskatchewan
  | 'yt'; // Yukon

export type Federation = {
    slug: FederationSlug;
    name: string;
    url: string;
  }
  
  export const federations: Federation[] = [
    {
      slug: 'qc',
      name: 'Rugby Quebec',
      url: 'https://www.rugbyquebec.com',
    },
    {
      slug: 'on',
      name: 'Rugby Ontario',
      url: 'https://rugbyontario.com',
    },
    // {
    //   slug: 'bc',
    //   name: 'Rugby BC',
    //   url: 'https://www.bcrugby.com',
    // },
    // {
    //   slug: 'ab',
    //   name: 'Rugby Alberta',
    //   url: 'https://rugbyalberta.com',
    // },
    // {
    //   slug: 'mb',
    //   name: 'Rugby Manitoba',
    //   url: 'https://rugbymanitoba.com',
    // },
    // {
    //   slug: 'sk',
    //   name: 'Rugby Saskatchewan',
    //   url: 'https://rugbysaskatchewan.com',
    // },
    // {
    //   slug: 'nb',
    //   name: 'Rugby New Brunswick',
    //   url: 'https://www.rugbynb.ca',
    // },
    // {
    //   slug: 'ns',
    //   name: 'Rugby Nova Scotia',
    //   url: 'https://rugbyns.ns.ca',
    // },
    // {
    //   slug: 'pe',
    //   name: 'Rugby PEI',
    //   url: 'https://rugtypei.com',
    // },
    // {
    //   slug: 'nl',
    //   name: 'Rugby Newfoundland and Labrador',
    //   url: 'https://sportnl.ca/member/rugby-nl/',
    // },
    // {
    //   slug: 'nt',
    //   name: 'Rugby North',
    //   url: 'https://rugbycanada.ca',
    // },
  ];
  
// src/data/loadFederationData.ts
import Papa from 'papaparse';

// Glob all .csv files under federation/year folders relative to this file
const csvModules = import.meta.glob('./*/*/*/*.csv', { query: '?raw', eager: true }) as Record<string, string>;

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
    // news: parseCsv(getCsv(slug, year, 'news')),
    info: parseCsv(getCsv(slug, year, 'info')),
    // vendor: parseCsv(getCsv(slug, 'vendor')), // if outside year folder, handle separately
  };
}
