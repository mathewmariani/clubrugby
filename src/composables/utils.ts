import { computed, type Ref } from 'vue';
import type { Club, League, Fixture, Result } from '@/utils/types';

export function useMatchClubs(
  match: Ref<Fixture | Result | null>,
  clubs: Record<string, Club>
) {
  const home = computed(() => {
    const id = match.value?.home_id;
    return id ? clubs[id] : undefined;
  });

  const away = computed(() => {
    const id = match.value?.away_id;
    return id ? clubs[id] : undefined;
  });

  return { home, away };
}

export function getLeagueName(
  id: string | undefined,
  leagues: Record<string, League>
): string {
  return id && leagues[id]?.name ? leagues[id].name : 'Unknown League';
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
