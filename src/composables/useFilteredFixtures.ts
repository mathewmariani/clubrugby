import { computed, type Ref } from 'vue';
import { useSavedLeagues } from './useSavedLeagues';

export function useFilteredFixtures(
  fixtures: Ref<Record<string, Record<string, any[]>>>
) {
  const { savedLeagues } = useSavedLeagues();

  const filteredFixtures = computed(() => {
    const filtered: Record<string, Record<string, any[]>> = {};

    for (const [day, leaguesForDay] of Object.entries(fixtures.value)) {
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

  return filteredFixtures;
}
