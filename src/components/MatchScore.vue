<template>
  <div
    class="score d-flex align-items-center justify-content-center fs-4 fw-bold"
  >
    <span :class="scoreClass(homeScore, awayScore)" class="score-number">
      {{ homeScore ?? '-' }}
    </span>
    <span class="score-dash mx-2">-</span>
    <span :class="scoreClass(awayScore, homeScore)" class="score-number">
      {{ awayScore ?? '-' }}
    </span>
  </div>
</template>

<script setup>
  const props = defineProps({
    homeScore: Number,
    awayScore: Number,
  });

  function scoreClass(score, opponentScore) {
    if (score == null || opponentScore == null) return '';
    return score > opponentScore
      ? 'text-success'
      : score < opponentScore
        ? 'text-danger'
        : '';
  }
</script>
