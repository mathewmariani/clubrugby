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
  }
) {
  // --- basic league filters ---
  const leaguesWithFixtures = computed(() => {
    return Object.fromEntries(
      Object.entries(fixtures)
        .map(([leagueId, list]) => [
          leagueId,
          list.filter((f) => f.fixtureStatus === 'fixture'),
        ])
        .filter(([_, list]) => list.length > 0)
    );
  });

  const leaguesWithResults = computed(() => {
    return Object.fromEntries(
      Object.entries(fixtures)
        .map(([leagueId, list]) => [
          leagueId,
          list.filter((f) => f.fixtureStatus === 'result'),
        ])
        .filter(([_, list]) => list.length > 0)
    );
  });

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
    return groupFixtures(fixtures, {
      clubId: options.clubId,
      status: 'fixture',
    });
  });

  const clubResultsByMonthDay = computed(() => {
    if (!options?.clubId) return {};
    return groupFixtures(fixtures, {
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

  return {
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
  };
}
