import { computed, type Ref } from 'vue';
import { type Fixture } from '../utils/types';

export function useFilteredFixtures(
  fixtures: Ref<Record<string, Record<string, Fixture[]>>>,
  savedLeagues: Ref<string[]>
) {
  const filteredFixtures = computed(() => {
    const filtered: Record<string, Record<string, Fixture[]>> = {};

    // Filter and sort matches within each league
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
