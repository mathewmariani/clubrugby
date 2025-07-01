import { computed, type Ref } from 'vue';
import type { Fixture, Result } from '@/utils/types';

export function useFilteredMatches<T extends Fixture | Result>(
  matches: Ref<Record<string, Record<string, T[]>>>,
  savedLeagues: Ref<string[]>
) {
  return computed(() => {
    const filtered: Record<string, Record<string, T[]>> = {};

    for (const [day, leaguesForDay] of Object.entries(matches.value)) {
      const filteredLeagues = Object.fromEntries(
        Object.entries(leaguesForDay).filter(
          ([leagueId]) => !savedLeagues.value.includes(leagueId)
        )
      );
      if (Object.keys(filteredLeagues).length > 0) {
        filtered[day] = filteredLeagues;
      }
    }

    return filtered;
  });
}
