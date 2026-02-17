import { computed } from 'vue';
import { useRoute, useRouter, type RouteLocationRaw } from 'vue-router';

export function useRouting() {
  const route = useRoute();
  const router = useRouter();

  /*
  --------------------------------------------------
  Route builders (objects, not strings)
  --------------------------------------------------
  */

  const union = (): RouteLocationRaw => ({
    name: 'fixtures',
  });

  const league = (leagueId: string): RouteLocationRaw => ({
    name: 'league-fixtures',
    params: { leagueId },
  });

  const club = (clubId: string): RouteLocationRaw => ({
    name: 'club-fixtures',
    params: { clubId },
  });

  const clubFixtures = (clubId: string): RouteLocationRaw => ({
    name: 'club-fixtures',
    params: { clubId },
  });

  const clubStats = (clubId: string): RouteLocationRaw => ({
    name: 'club-stats',
    params: { clubId },
  });

  const clubStandings = (clubId: string): RouteLocationRaw => ({
    name: 'club-standings',
    params: { clubId },
  });

  const fixture = (fixtureId: string): RouteLocationRaw => ({
    name: 'fixture-details',
    params: { fixtureId },
  });

  /*
  --------------------------------------------------
  Push helpers
  --------------------------------------------------
  */

  const go = {
    union: () => router.push(union()),
    league: (id: string) => router.push(league(id)),
    club: (id: string) => router.push(club(id)),
    fixtures: (id: string) => router.push(clubFixtures(id)),
    stats: (id: string) => router.push(clubStats(id)),
    standings: (id: string) => router.push(clubStandings(id)),
    fixture: (id: string) => router.push(fixture(id)),
  };

  /*
  --------------------------------------------------
  Current params
  --------------------------------------------------
  */

  const current = {
    clubId: computed(() => route.params.clubId as string | undefined),
    leagueId: computed(() => route.params.leagueId as string | undefined),
    fixtureId: computed(() => route.params.fixtureId as string | undefined),
  };

  return {
    // route builders
    union,
    league,
    club,
    clubFixtures,
    clubStats,
    clubStandings,
    fixture,

    // navigation
    go,

    // state
    current,
  };
}
