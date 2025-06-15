import { computed, type Ref } from 'vue';
import { type Result } from '../utils/types';

export function useFilteredResults(
  results: Ref<Record<string, Record<string, Result[]>>>,
  savedLeagues: Ref<string[]>
) {
  const filteredResults = computed(() => {
    const filtered: Record<string, Record<string, Result[]>> = {};

    // Filter and sort matches within each league
    for (const [day, leaguesForDay] of Object.entries(results.value)) {
      const filteredLeagues: Record<string, Result[]> = {};

      // Sort matches by date (descending)
      for (const [leagueId, matches] of Object.entries(leaguesForDay)) {
        if (!savedLeagues.value.includes(leagueId)) {
          const sortedMatches = [...matches].sort((a, b) => {
            const aDate = new Date(`${a.date}T${a.time}`);
            const bDate = new Date(`${b.date}T${b.time}`);
            return bDate.getTime() - aDate.getTime();
          });

          filteredLeagues[leagueId] = sortedMatches;
        }
      }

      if (Object.keys(filteredLeagues).length > 0) {
        filtered[day] = filteredLeagues;
      }
    }

    // Sort outer keys (dates) in descending order
    const sorted: Record<string, Record<string, Result[]>> = {};
    const sortedDays = Object.keys(filtered).sort(
      (a, b) => new Date(b).getTime() - new Date(a).getTime()
    );

    for (const day of sortedDays) {
      sorted[day] = filtered[day];
    }

    return sorted;
  });

  return filteredResults;
}
