import { ref, onMounted, watch } from 'vue';

export function useSavedLeagues(key = 'my_leagues') {
  const savedLeagues = ref<string[]>([]);

  // Load from localStorage on mount
  onMounted(() => {
    try {
      const saved = localStorage.getItem(key);
      if (saved) {
        savedLeagues.value = JSON.parse(saved);
      }
    } catch (e) {
      console.error('Failed to parse saved leagues from localStorage:', e);
      savedLeagues.value = [];
    }
  });

  // Watch and save automatically whenever updated
  watch(
    savedLeagues,
    (newVal) => {
      localStorage.setItem(key, JSON.stringify(newVal));
    },
    { deep: true }
  );

  return {
    savedLeagues,
    setSavedLeagues: (val: string[]) => (savedLeagues.value = val),
  };
}
