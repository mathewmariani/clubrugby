// composables/useFixtureFilters.ts
import { computed } from 'vue';
import type { Fixture } from '@/utils/types';
import { groupFixtures } from '@/utils/fixtures';

/**
 * Provides filtered and grouped fixtures for use in components
 */
export function useFixtureFilters(
  fixtures: Record<string, Fixture[]>,
  options?: {
    clubId?: string;
    savedLeagues?: string[];
    leagueId?: string;
  }
) {
  const filteredFixtures = computed(() => {
    let source = fixtures;

    // single league filter (highest priority)
    if (options?.leagueId) {
      return {
        [options.leagueId]: fixtures[options.leagueId] ?? [],
      };
    }

    // saved leagues filter
    if (options?.savedLeagues?.length) {
      return Object.fromEntries(
        Object.entries(fixtures).filter(([id]) =>
          options.savedLeagues!.includes(id)
        )
      );
    }

    return source;
  });

  // --- basic league filters ---
  const leaguesWithFixtures = computed(() =>
    Object.fromEntries(
      Object.entries(filteredFixtures.value)
        .map(([leagueId, list]) => [
          leagueId,
          list.filter((f) => f.fixtureStatus === 'fixture'),
        ])
        .filter(([_, list]) => list.length > 0)
    )
  );

  const leaguesWithResults = computed(() =>
    Object.fromEntries(
      Object.entries(filteredFixtures.value)
        .map(([leagueId, list]) => [
          leagueId,
          list.filter((f) => f.fixtureStatus === 'result'),
        ])
        .filter(([_, list]) => list.length > 0)
    )
  );

  // --- grouped by month/day/league ---
  const fixturesByMonthDay = computed(() =>
    groupFixtures(leaguesWithFixtures.value, { status: 'fixture' })
  );

  const resultsByMonthDay = computed(() =>
    groupFixtures(leaguesWithResults.value, { status: 'result' })
  );

  // --- club-specific ---
  const clubFixturesByMonthDay = computed(() => {
    if (!options?.clubId) return {};
    return groupFixtures(filteredFixtures.value, {
      clubId: options.clubId,
      status: 'fixture',
    });
  });

  const clubResultsByMonthDay = computed(() => {
    if (!options?.clubId) return {};
    return groupFixtures(filteredFixtures.value, {
      clubId: options.clubId,
      status: 'result',
    });
  });

  // --- checks ---
  const hasFixtures = computed(
    () => Object.keys(leaguesWithFixtures.value).length > 0
  );
  const hasResults = computed(
    () => Object.keys(leaguesWithResults.value).length > 0
  );
  const clubHasFixtures = computed(
    () => Object.keys(clubFixturesByMonthDay.value).length > 0
  );
  const clubHasResults = computed(
    () => Object.keys(clubResultsByMonthDay.value).length > 0
  );

  // --- lookup a fixture by its ID across all leagues ---
  function useFixtureById(fixtureId: string | undefined) {
    const result = computed<{ fixture: Fixture; league_id: string } | null>(
      () => {
        if (!fixtureId) return null;

        for (const [league_id, list] of Object.entries(
          filteredFixtures.value
        )) {
          const fixture = list.find((f) => `${f.fixtureId}` === fixtureId);
          if (fixture) return { fixture, league_id };
        }

        return null;
      }
    );

    return {
      fixture: computed(() => result.value?.fixture ?? null),
      league_id: computed(() => result.value?.league_id ?? null),
    };
  }

  return {
    filteredFixtures,

    // league filters
    leaguesWithFixtures,
    leaguesWithResults,
    hasFixtures,
    hasResults,

    // grouped
    fixturesByMonthDay,
    resultsByMonthDay,

    // club-specific
    clubFixturesByMonthDay,
    clubResultsByMonthDay,
    clubHasFixtures,
    clubHasResults,

    // fixture lookup
    useFixtureById,
  };
}
