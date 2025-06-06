<template>
  <a href="#" class="list-group-item">
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
      <strong
        :class="scoreClass(match.home_score, match.away_score)"
        class="ms-auto"
        >{{ match.home_score || 'Unknown' }}</strong
      >
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
      <strong
        :class="scoreClass(match.away_score, match.home_score)"
        class="ms-auto"
        >{{ match.away_score || 'Unknown' }}</strong
      >
    </div>
  </a>
</template>

<script setup>
  const props = defineProps({
    match: { type: Object, required: true },
    clubs: { type: Object, required: true },
    leagues: { type: Object, required: true },
  });

  function scoreClass(score, opponentScore) {
    if (score == null || opponentScore == null) return '';
    if (score === opponentScore) return ''; // tie no color
    return score > opponentScore ? 'text-success' : 'text-danger';
  }
</script>

<style scoped></style>
