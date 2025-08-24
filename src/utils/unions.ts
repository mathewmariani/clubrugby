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
    {
    slug: 'rseq',
    name: 'RSEQ',
    url: 'https://rugbysaskatchewan.com',
  },
];
