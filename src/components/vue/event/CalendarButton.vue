<template>
  <a class="list-group-item d-flex flex-column py-2 bd-callout" 
     :href="link"
     target="_blank"
     rel="noopener noreferrer">
    <small>📆: {{ date }}</small>
    <small>⏰: {{ time }}</small>
    <small>📍: {{ fixture.venue }}</small>
  </a>
</template>

<script setup lang="ts">
import { computed } from 'vue';
import type { Fixture } from '@/utils/types';
import { formattedDate, formattedTime } from '@/composables/utils';
import { google, outlook, office365, yahoo, ics, type CalendarEvent } from 'calendar-link';

const props = defineProps<{
  fixture: Fixture;
  home: string;
  away: string;
}>();

const date = computed(() => formattedDate(props.fixture.fixtureDate));
const time = computed(() => formattedTime(props.fixture.fixtureDate));

type CalendarProvider = 'google' | 'outlook' | 'office365' | 'yahoo' | 'ics';

function getDefaultCalendar(): CalendarProvider {
  const ua = navigator.userAgent.toLowerCase();

  if (/iphone|ipad|ipod/.test(ua)) return 'ics';
  if (ua.includes('android')) return 'google';
  if (ua.includes('mac')) return 'ics';
  if (ua.includes('win')) return 'outlook';
  return 'google';
}

const calendarHandlers: Record<CalendarProvider, (event: CalendarEvent) => string> = {
  google,
  outlook,
  office365,
  yahoo,
  ics,
};

const event = computed<CalendarEvent>(() => ({
  uid: String(props.fixture.fixtureId),
  title: `${props.fixture.home} vs ${props.fixture.away}`,
  description: props.fixture.venue,
  start: new Date(props.fixture.fixtureDate),
  duration: [3, 'hour'],
}));

const link = computed(() => {
  const provider = getDefaultCalendar();
  return calendarHandlers[provider](event.value);
});
</script>

<style scoped>
.bd-callout {
    border-left: 0.25rem solid var(--bs-info);
    border-right: 0.25rem solid var(--bs-info);
}
</style>