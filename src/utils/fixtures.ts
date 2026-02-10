// utils/fixtures.ts
import type { Fixture } from '@/utils/types';
import { format } from 'date-fns';

/**
 * Group fixtures by month → day → league
 * Supports optional club and status filtering
 */
export function groupFixtures(
  fixturesByLeague: Record<string, Fixture[]>,
  options?: {
    clubId?: string;
    status?: 'fixture' | 'result';
  }
): Record<string, Record<string, Record<string, Fixture[]>>> {
  const grouped: Record<string, Record<string, Record<string, Fixture[]>>> = {};

  for (const [leagueId, fixtures] of Object.entries(fixturesByLeague)) {
    // Filter by status and club if provided
    const filtered = fixtures.filter((f) => {
      if (options?.status && f.fixtureStatus !== options.status) return false;
      if (
        options?.clubId &&
        f.home.club_id !== options.clubId &&
        f.away.club_id !== options.clubId
      )
        return false;
      return true;
    });

    // Sort by fixture date
    const sorted = filtered
      .slice()
      .sort((a, b) => a.fixtureDate - b.fixtureDate);

    for (const fixture of sorted) {
      const date = new Date(fixture.fixtureDate * 1000);
      const monthKey = format(date, 'yyyy-MM');
      const dayKey = format(date, 'yyyy-MM-dd');

      grouped[monthKey] ??= {};
      grouped[monthKey][dayKey] ??= {};
      grouped[monthKey][dayKey][leagueId] ??= [];

      grouped[monthKey][dayKey][leagueId].push(fixture);
    }
  }

  return grouped;
}
