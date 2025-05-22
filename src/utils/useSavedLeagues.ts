import { ref, onMounted } from 'vue';

export function useSavedLeagues(key = 'my_leagues') {
  const savedLeagues = ref([]);

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

  return { savedLeagues };
}
