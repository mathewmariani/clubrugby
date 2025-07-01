import { ref } from 'vue';

export const navbarHeight = ref(0);

export function useLayout() {
  return {
    navbarHeight,
  };
}
