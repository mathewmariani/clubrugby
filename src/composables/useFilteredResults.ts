import { computed, type Ref } from 'vue';
import { useSavedLeagues } from './useSavedLeagues';

export function useFilteredResults(
  results: Ref<Record<string, Record<string, any[]>>>
) {
  const { savedLeagues } = useSavedLeagues();

  const filteredResults = computed(() => {
    const filtered: Record<string, Record<string, any[]>> = {};

    // First: filter and sort matches within each league
    for (const [day, leaguesForDay] of Object.entries(results.value)) {
      const filteredLeagues: Record<string, any[]> = {};

      for (const [leagueId, matches] of Object.entries(leaguesForDay)) {
        if (savedLeagues.value.includes(leagueId)) {
          const sortedMatches = [...matches].sort((a, b) => {
            const aDate = new Date(`${a.date}T${a.time}`);
            const bDate = new Date(`${b.date}T${b.time}`);
            return bDate.getTime() - aDate.getTime(); // Descending
          });

          filteredLeagues[leagueId] = sortedMatches;
        }
      }

      if (Object.keys(filteredLeagues).length > 0) {
        filtered[day] = filteredLeagues;
      }
    }

    // Then: sort outer keys (dates) in descending order
    const sorted: Record<string, Record<string, any[]>> = {};
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
