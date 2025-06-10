import { computed, type Ref } from 'vue';

export function useFilteredFixtures(
  fixtures: Ref<Record<string, Record<string, any[]>>>,
  savedLeagues: Ref<string[]>
) {
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
