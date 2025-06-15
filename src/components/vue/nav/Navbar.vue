<template>
  <nav class="navbar bg-body-tertiary fixed-top border-bottom">
    <div class="container-fluid">
      <a class="navbar-brand">
        {{ SITE_TITLE }} | {{ union.slug.toUpperCase() }}
      </a>
      <button
        class="btn"
        type="button"
        data-bs-toggle="offcanvas"
        data-bs-target="#settingsOffcanvas"
        aria-controls="settingsOffcanvas"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
    </div>

    <TabScroller
      :titles="titles"
      :selectedIndex="selectedIndex"
      @select="(index) => emit('select', index)"
    />

    <SettingsOffcanvas :leagues="leagues" />
  </nav>
</template>

<script setup lang="ts">
  import TabScroller from './TabScroller.vue';
  import SettingsOffcanvas from './SettingsOffcanvas.vue';
  import { SITE_TITLE } from '../../../consts.ts';
  import { type Union } from '../../../utils/unions.ts';
  import { type League } from '../../../utils/types.ts';

  const props = defineProps<{
    union: Union;
    titles: string[];
    selectedIndex: number;
    leagues: Record<string, League>;
  }>();

  const emit = defineEmits<{
    (e: 'select', index: number): void;
  }>();
</script>
