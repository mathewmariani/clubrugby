<template>
  <div class="list-group-item">
    <div class="d-flex flex-column mt-3">
      <h6>Match Details</h6>
      <span class="text-muted">Date</span>
      <p>{{ date }}</p>
      <span class="text-muted">League</span>
      <p>{{ league }}</p>
      <template v-if="!isResult">
        <span class="text-muted">Venue</span>
        <p>{{ venue }}</p>
      </template>
      <a class="btn btn-danger"
       :href="getDefaultMaps()" target="_blank" rel="noopener noreferrer">
       <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-geo-alt" viewBox="0 0 16 16">
  <path d="M12.166 8.94c-.524 1.062-1.234 2.12-1.96 3.07A32 32 0 0 1 8 14.58a32 32 0 0 1-2.206-2.57c-.726-.95-1.436-2.008-1.96-3.07C3.304 7.867 3 6.862 3 6a5 5 0 0 1 10 0c0 .862-.305 1.867-.834 2.94M8 16s6-5.686 6-10A6 6 0 0 0 2 6c0 4.314 6 10 6 10"/>
  <path d="M8 8a2 2 0 1 1 0-4 2 2 0 0 1 0 4m0 1a3 3 0 1 0 0-6 3 3 0 0 0 0 6"/>
</svg> 
       Open in Maps
      </a>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { formattedDate } from '@/composables/utils';
  import { computed } from 'vue';

  const props = defineProps<{
    fixtureDate: number;
    league: string;
    venue: string;
    venueLong: string;
    venueLat: string;
    isResult: boolean;
  }>();

  const date = computed(() => formattedDate(props.fixtureDate));

function getDefaultMaps() {
  const ua = navigator.userAgent.toLowerCase();
  if (/iphone|ipad|ipod/.test(ua)) {
    return 'https://maps.apple.com/?ll=48.4697,-123.315&q=U%20Of%20Victoria';
  }
  return `https://www.google.com/maps/search/?api=1&query=48.4697,-123.315`;
}
</script>
