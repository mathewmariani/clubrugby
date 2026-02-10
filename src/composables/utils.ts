import { computed, type Ref } from 'vue';
import type { Club, Fixture, Standing } from '@/utils/types';

// Convert unix timestamp to human-readable "h:mm a"
export function formattedTime(timestamp: number): string {
  const date = new Date(timestamp * 1000);
  return date.toLocaleTimeString([], {
    hour: '2-digit',
    minute: '2-digit',
  });
}

export function formattedDate(timestamp: number): string {
  const date = new Date(timestamp * 1000);
  return date.toLocaleDateString([], {
    year: 'numeric',
    month: 'short',
    day: '2-digit',
  });
}

export function useMatchClubs(
  fixture: Ref<Fixture | null>,
  clubs: Record<string, Club>
) {
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

export function getRecordString(table?: Standing): string {
  return `${table?.gamesWon ?? 0}-${table?.gamesDraw ?? 0}-${table?.gameLost ?? 0}`;
}

export function getLeagueName(
  league_id: string,
  leagues: Record<string, string>
): string {
  return league_id && leagues[league_id]
    ? leagues[league_id]
    : 'Unknown League';
}

export function getOrdinalSuffix(n: number): string {
  const j = n % 10,
    k = n % 100;
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
