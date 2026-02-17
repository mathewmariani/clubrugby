<template>
  <div class="list-group-item">
    <div class="alert alert-light mb-0" role="alert">
      <div class="d-flex justify-content-between align-items-center">
        <section>
          <small class="d-block">📆: {{ date }}</small>
          <small class="d-block">⏰: {{ time }}</small>
          <small class="d-block">📍: {{ fixture.venue }}</small>
        </section>

        <a
          class="btn btn-link text-danger p-0"
          :href="calendarLink"
          target="_blank"
          rel="noopener noreferrer"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="2rem"
            height="2rem"
            fill="currentColor"
            class="bi bi-calendar-plus"
            viewBox="0 0 16 16"
          >
            <path
              d="M8 7a.5.5 0 0 1 .5.5V9H10a.5.5 0 0 1 0 1H8.5v1.5a.5.5 0 0 1-1 0V10H6a.5.5 0 0 1 0-1h1.5V7.5A.5.5 0 0 1 8 7"
            />
            <path
              d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5M1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4z"
            />
          </svg>
        </a>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { computed } from 'vue';
  import type { Fixture } from '@/types/appData';
  import { formattedDate, formattedTime } from '@/composables/utils';

  const props = defineProps<{
    fixture: Fixture;
  }>();

  const date = computed(() => formattedDate(props.fixture.fixtureDate));
  const time = computed(() => formattedTime(props.fixture.fixtureDate));

  const calendarLink = computed(() => {
    return `/calendar/${props.fixture.fixtureId}.ics`;
  });
</script>
