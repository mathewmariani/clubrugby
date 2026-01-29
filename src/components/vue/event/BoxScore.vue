<template>
  <div class="list-group-item">
    <div class="d-flex flex-column mt-3">
      <h6>Box Score</h6>
      <MatchStatComparison
        v-for="stat in pointsTotalStats"
        :key="stat.key"
        :label="stat.label"
        :leftValue="getStatValue(home, stat.key)"
        :rightValue="getStatValue(away, stat.key)"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
  import MatchStatComparison from '@/components/vue/event/MatchStatComparison.vue';
  import type { FixtureResultSummary } from '@/utils/types';

  const props = defineProps<{
    home: FixtureResultSummary;
    away: FixtureResultSummary;
  }>();

  function getStatValue(
    team: FixtureResultSummary,
    key: keyof FixtureResultSummary
  ): number {
    return Number(team[key]);
  }

  const pointsTotalStats = [
    { key: 'score', label: 'Score' },
    { key: 'conv', label: 'Conversions' },
    { key: 'pen', label: 'Penalties' },
    { key: 'drop', label: 'Drop Kicks' },
  ] as const;
</script>
