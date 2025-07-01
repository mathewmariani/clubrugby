<template>
  <h1 class="mb-0">
    <span :class="scoreClass(homeScore, awayScore)">
      {{ homeScore ?? '-' }}
    </span>
    <span> - </span>
    <span :class="scoreClass(awayScore, homeScore)">
      {{ awayScore ?? '-' }}
    </span>
  </h1>
</template>

<script setup>
  const props = defineProps({
    homeScore: Number,
    awayScore: Number,
  });

  function scoreClass(score, opponentScore) {
    if (score == null || opponentScore == null) return '';
    if (score === opponentScore) return ''; // tie no color
    return score > opponentScore ? 'text-success' : 'text-danger';
  }
</script>
