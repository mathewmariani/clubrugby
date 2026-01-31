import { computed, type Ref } from 'vue';
import type { Fixture } from '@/utils/types';
import { flattenFixturesForClub, groupByMonthDay } from './utils';

/**
 * Composable for filtering and organizing fixtures
 * Provides multiple filtering patterns commonly used across components
 */
export function useFixtureFilters(
  fixtures: Ref<Record<string, Fixture[]>>,
  options?: {
    clubId?: string;
    savedLeagues?: Ref<string[]>;
  }
) {
  // ========== Basic Status Filters ==========

  /**
   * Group fixtures by league, filtering to only upcoming matches
   */
  const leaguesWithFixtures = computed(() =>
    Object.fromEntries(
      Object.entries(fixtures.value)
        .map(([leagueId, fixtureList]) => [
          leagueId,
          fixtureList.filter((f) => f.fixtureStatus === 'fixture'),
        ])
        .filter(([_, fixtureList]) => fixtureList.length > 0)
    )
  );

  /**
   * Check if there are any upcoming fixtures
   */
  const hasFixtures = computed(
    () => Object.keys(leaguesWithFixtures.value).length > 0
  );

  /**
   * Group fixtures by league, filtering to only results
   */
  const leaguesWithResults = computed(() =>
    Object.fromEntries(
      Object.entries(fixtures.value)
        .map(([leagueId, fixtureList]) => [
          leagueId,
          fixtureList.filter((f) => f.fixtureStatus === 'result'),
        ])
        .filter(([_, fixtureList]) => fixtureList.length > 0)
    )
  );

  /**
   * Check if there are any results
   */
  const hasResults = computed(
    () => Object.keys(leaguesWithResults.value).length > 0
  );

  // ========== Club-Specific Filters ==========

  /**
   * Upcoming matches for a specific club, grouped by month/day
   */
  const upcomingByMonthDay = computed(() => {
    if (!options?.clubId) return {};
    return groupByMonthDay(
      flattenFixturesForClub(fixtures.value, options.clubId, 'fixture')
    );
  });

  /**
   * Results for a specific club, grouped by month/day
   */
  const resultsByMonthDay = computed(() => {
    if (!options?.clubId) return {};
    return groupByMonthDay(
      flattenFixturesForClub(fixtures.value, options.clubId, 'result')
    );
  });

  /**
   * Check if club has upcoming fixtures
   */
  const clubHasFixtures = computed(
    () => Object.keys(upcomingByMonthDay.value).length > 0
  );

  /**
   * Check if club has results
   */
  const clubHasResults = computed(
    () => Object.keys(resultsByMonthDay.value).length > 0
  );

  // ========== Saved Leagues Filter ==========

  /**
   * Fixtures filtered by saved leagues
   */
  const filteredByLeagues = computed(() => {
    if (!options?.savedLeagues) return fixtures.value;

    const result: Record<string, Fixture[]> = {};
    for (const [leagueId, fixtureList] of Object.entries(fixtures.value)) {
      if (!options.savedLeagues.value.includes(leagueId)) {
        result[leagueId] = fixtureList;
      }
    }
    return result;
  });

  /**
   * Upcoming fixtures filtered by saved leagues
   */
  const filteredFixturesByLeagues = computed(() =>
    Object.fromEntries(
      Object.entries(filteredByLeagues.value)
        .map(([leagueId, fixtureList]) => [
          leagueId,
          fixtureList.filter((f) => f.fixtureStatus === 'fixture'),
        ])
        .filter(([_, fixtureList]) => fixtureList.length > 0)
    )
  );

  /**
   * Results filtered by saved leagues
   */
  const filteredResultsByLeagues = computed(() =>
    Object.fromEntries(
      Object.entries(filteredByLeagues.value)
        .map(([leagueId, fixtureList]) => [
          leagueId,
          fixtureList.filter((f) => f.fixtureStatus === 'result'),
        ])
        .filter(([_, fixtureList]) => fixtureList.length > 0)
    )
  );

  /**
   * Check if there are any filtered fixtures
   */
  const hasFilteredFixtures = computed(
    () => Object.keys(filteredFixturesByLeagues.value).length > 0
  );

  /**
   * Check if there are any filtered results
   */
  const hasFilteredResults = computed(
    () => Object.keys(filteredResultsByLeagues.value).length > 0
  );

  return {
    // Basic status filters
    leaguesWithFixtures,
    hasFixtures,
    leaguesWithResults,
    hasResults,

    // Club-specific filters
    upcomingByMonthDay,
    resultsByMonthDay,
    clubHasFixtures,
    clubHasResults,

    // Saved leagues filters
    filteredByLeagues,
    filteredFixturesByLeagues,
    filteredResultsByLeagues,
    hasFilteredFixtures,
    hasFilteredResults,
  };
}
