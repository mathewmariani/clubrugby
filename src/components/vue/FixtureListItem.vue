<template>
  <!-- make this an href to a stats page -->
  <a class="list-group-item">
    <div class="d-flex justify-content-between w-100 mb-2">
      <small class="text-muted">{{ match.venue }}</small>
      <span class="badge text-bg-danger">
        {{ match.time }}
      </span>
    </div>
    <div class="d-flex align-items-center gap-2 mb-1">
      <img
        v-if="clubs[match.home_id]?.logo"
        :src="clubs[match.home_id].logo"
        :alt="clubs[match.home_id].name"
        width="32"
        height="32"
        style="object-fit: contain"
      />
      <small>{{ clubs[match.home_id].name || 'Unknown' }}</small>
      <!-- <small class="ms-auto">{{ getRecord(match.home_id) }}</small> -->
    </div>
    <div class="d-flex align-items-center gap-2 mb-1">
      <img
        v-if="clubs[match.away_id]?.logo"
        :src="clubs[match.away_id].logo"
        :alt="clubs[match.away_id].name"
        width="32"
        height="32"
        style="object-fit: contain"
      />
      <small>{{ clubs[match.away_id].name || 'Unknown' }}</small>
      <!-- <small class="ms-auto">{{ getRecord(match.away_id) }}</small> -->
    </div>
  </a>
</template>

<script setup>
  const props = defineProps({
    match: { type: Object, required: true },
    clubs: { type: Object, required: true },
    leagues: { type: Object, required: true },
  });

  function getRecord(club_id) {
    return '0-0-0';
  }
</script>

<style scoped></style>
