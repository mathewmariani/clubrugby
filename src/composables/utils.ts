import { computed, type Ref } from 'vue';
import type { Club, Fixture, Standing } from '@/utils/types';

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
    const id = fixture.value?.homeClubId;
    return id ? clubs[id] : undefined;
  });

  const away = computed(() => {
    const id = fixture.value?.awayClubId;
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
