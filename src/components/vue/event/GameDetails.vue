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
      <a
       class="btn btn-danger"
       :href="getDefaultMaps()"
                 target="_blank"
          rel="noopener noreferrer">
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
