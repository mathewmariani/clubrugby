<template>
  <h1 class="mb-0">
    <span :class="scoreClass(home, away)">
      {{ home ?? '-' }}
    </span>
    <span> - </span>
    <span :class="scoreClass(away, home)">
      {{ away ?? '-' }}
    </span>
  </h1>
</template>

<script setup>
  const props = defineProps({
    home: String,
    away: String,
  });

  function scoreClass(score, opponentScore) {
    if (score == null || opponentScore == null) return '';
    if (score === opponentScore) return ''; // tie no color
    return score > opponentScore ? 'text-success' : 'text-danger';
  }
</script>
