import { onMounted, onUnmounted } from 'vue';

export function useFixedOffset({
  selector = '.fixed-top',
  cssVar = '--navbar-height',
}: {
  selector?: string;
  cssVar?: string;
} = {}) {
  const update = () => {
    const el = document.querySelector<HTMLElement>(selector);
    if (el) {
      document.documentElement.style.setProperty(
        cssVar,
        `${el.offsetHeight}px`
      );
    }
  };

  onMounted(() => {
    update();
    window.addEventListener('resize', update);
  });

  onUnmounted(() => {
    window.removeEventListener('resize', update);
  });
}
