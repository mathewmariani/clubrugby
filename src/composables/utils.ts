import { computed, type Ref } from 'vue';
import type { Club, Fixture, Standing } from '@/utils/types';
import { format } from 'date-fns';

// Convert unix timestamp to human-readable "h:mm a"
export function formattedTime(timestamp: number): string {
  const date = new Date(timestamp * 1000);
  return date.toLocaleTimeString([], {
    hour: '2-digit',
    minute: '2-digit'
  });
};

export function formattedDate(timestamp: number): string {
  const date = new Date(timestamp * 1000);
  return date.toLocaleDateString([], {
    year: 'numeric',
    month: 'short',
    day: '2-digit',
  });
}

export function useMatchClubs(fixture: Ref<Fixture | null>, clubs: Record<string, Club>) {
  const home = computed(() => {
    const id = fixture.value?.home.club_id;
    return id ? clubs[id] : undefined;
  });

  const away = computed(() => {
    const id = fixture.value?.away.club_id;
    return id ? clubs[id] : undefined;
  });

  return { home, away };
}

export function useFixtureById(fixtureId: Ref<string | undefined>, fixturesByLeague: Record<string, Fixture[]>) {
  const result = computed<{ fixture: Fixture; league_id: string; } | null>(() => {
    if (!fixtureId.value) {
      return null;
    }
    for (const [league_id, fixtures] of Object.entries(fixturesByLeague)) {
      const fixture = fixtures.find(f => f.fixtureId === fixtureId.value);
      if (fixture) {
        return { fixture, league_id };
      }
    }
    return null;
  });

  const fixture = computed<Fixture | null>(() => result.value?.fixture ?? null);
  const league_id = computed<string | null>(() => result.value?.league_id ?? null);

  return {
    fixture,
    league_id,
  };
}

export function getRecordString(table?: Standing): string {
  return `${table?.gamesWon ?? 0}-${table?.gamesDraw ?? 0}-${table?.gameLost ?? 0}`;
}

export function getLeagueName(league_id: string, leagues: Record<string, string>): string {
  return league_id && leagues[league_id] ? leagues[league_id] : 'Unknown League';
}

export function getOrdinalSuffix(n: number): string {
  const j = n % 10, k = n % 100;
  if (k >= 11 && k <= 13) {
    return n + 'th';
  }
  switch (j) {
    case 1:
      return n + 'st';
    case 2:
      return n + 'nd';
    case 3:
      return n + 'rd';
    default:
      return n + 'th';
  }
}

export function flattenFixturesForClub(fixtures: Record<string, Fixture[]>, club_id: string, status: 'fixture' | 'result') {
  const all: Fixture[] = [];
  for (const [leagueId, schedule] of Object.entries(fixtures)) {
    for (const fixture of schedule) {
      if (
        fixture.home.club_id === club_id ||
        fixture.away.club_id === club_id
      ) {
        if (fixture.fixtureStatus === status) {
          all.push(fixture);
        }
      }
    }
  }
  return all;
}

// --- Group by month/day ---
export function groupByMonthDay(matches: Fixture[]) {
  const grouped: Record<string, Record<string, Fixture[]>> = {};
  const sorted = [...matches].sort((a, b) => a.fixtureDate - b.fixtureDate);

  for (const match of sorted) {
    const date = new Date(match.fixtureDate * 1000);
    const monthKey = format(date, 'yyyy-MM');
    const dayKey = format(date, 'yyyy-MM-dd');

    if (!grouped[monthKey]) grouped[monthKey] = {};
    if (!grouped[monthKey][dayKey]) grouped[monthKey][dayKey] = [];

    grouped[monthKey][dayKey].push(match);
  }

  return grouped;
}

// Group by month/day/league, preserving league information
export function groupByMonthDayLeague(fixturesByLeague: Record<string, Fixture[]>, club_id: string, status: 'fixture' | 'result') {
  const grouped: Record<string, Record<string, Record<string, Fixture[]>>> = {};

  for (const [leagueId, fixtures] of Object.entries(fixturesByLeague)) {
    // Filter fixtures for the club and status
    const filtered = fixtures.filter(f => {
      return (f.home.club_id === club_id || f.away.club_id === club_id) && f.fixtureStatus === status;
    });

    // Sort by date
    const sorted = [...filtered].sort((a, b) => a.fixtureDate - b.fixtureDate);

    for (const fixture of sorted) {
      const date = new Date(fixture.fixtureDate * 1000);
      const monthKey = format(date, 'yyyy-MM');
      const dayKey = format(date, 'yyyy-MM-dd');

      if (!grouped[monthKey]) grouped[monthKey] = {};
      if (!grouped[monthKey][dayKey]) grouped[monthKey][dayKey] = {};
      if (!grouped[monthKey][dayKey][leagueId]) grouped[monthKey][dayKey][leagueId] = [];

      grouped[monthKey][dayKey][leagueId].push(fixture);
    }
  }

  return grouped;
}

// Extract the main score from format like "36;6" -> "36"
export function extractMainScore(score: string | undefined): number {
  if (!score) return 0;
  return parseInt(score.split(';')[0], 10);
}