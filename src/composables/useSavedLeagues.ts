import { ref, watch } from 'vue';

const savedLeagues = ref<string[]>([]);

let initialized = false;

export function useSavedLeagues(key = 'my_leagues') {
  if (!initialized) {
    initialized = true;

    try {
      const saved = localStorage.getItem(key);
      if (saved) {
        savedLeagues.value = JSON.parse(saved);
      }
    } catch (e) {
      console.error('Failed to parse saved leagues from localStorage:', e);
      savedLeagues.value = [];
    }

    // Watch once globally
    watch(
      savedLeagues,
      (newVal) => {
        localStorage.setItem(key, JSON.stringify(newVal));
      },
      { deep: true }
    );
  }

  return {
    savedLeagues,
    setSavedLeagues: (val: string[]) => (savedLeagues.value = val),
  };
}
