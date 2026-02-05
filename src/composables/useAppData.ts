import { inject } from 'vue';

export function useAppData() {
  const data = inject('appData');

  if (!data) {
    throw new Error('useAppData must be used inside App.vue');
  }

  return data;
}
