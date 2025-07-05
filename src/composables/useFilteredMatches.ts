import { computed, type Ref } from 'vue';
import type { Fixture, Result } from '@/utils/types';

export function useFilteredMatches<T extends Fixture | Result>(
  matches: Ref<Record<string, Record<string, T[]>>>,
  savedLeagues: Ref<string[]>
) {
  const filtered = computed(() => {
    const result: Record<string, Record<string, T[]>> = {};

    for (const [day, leaguesForDay] of Object.entries(matches.value)) {
      const filteredLeagues = Object.fromEntries(
        Object.entries(leaguesForDay).filter(
          ([leagueId]) => !savedLeagues.value.includes(leagueId)
        )
      );
      if (Object.keys(filteredLeagues).length > 0) {
        result[day] = filteredLeagues;
      }
    }

    return result;
  });

  const has = computed(() =>
    Object.values(filtered.value).some(
      (leaguesForDay) => Object.values(leaguesForDay).flat().length > 0
    )
  );

  return { filtered, has };
}
