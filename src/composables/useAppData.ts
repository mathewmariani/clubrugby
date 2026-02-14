import { inject } from 'vue';
import { appDataKey } from '@/types/appData';

export function useAppData() {
  const data = inject(appDataKey);

  if (!data) {
    throw new Error('useAppData must be used after appData is provided');
  }

  const getClub = (id: string) => data.clubs[id];
  const getLeague = (id: string) => data.leagues[id];

  return data;
}
