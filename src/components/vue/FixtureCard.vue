<template>
  <div class="card fixture">
    <div
      class="card-body d-flex flex-column align-items-center justify-content-between"
    >
      <span class="badge text-bg-primary">
        {{ leagues[match.league_id].name }}
      </span>
      <div class="my-auto d-flex align-items-center justify-content-between">
        <FixtureTeam :club="clubs[match.home_id]" />
        <component :is="centerComponent" v-bind="centerProps" />
        <FixtureTeam :club="clubs[match.away_id]" />
      </div>
      <h6>
        <span class="badge text-bg-danger venue-badge">{{ match.venue }}</span>
      </h6>
    </div>
  </div>
</template>

<script setup>
  import { computed } from 'vue';
  import FixtureTeam from './FixtureTeam.vue';
  import MatchMetadata from './FixtureMetadata.vue';
  import MatchScore from './FixtureScore.vue';

  const props = defineProps({
    match: { type: Object, required: true },
    clubs: { type: Object, required: true },
    leagues: { type: Object, required: true },
    mode: { type: String, required: true },
  });

  const centerComponent = computed(() => {
    return props.mode === 'result' ? MatchScore : MatchMetadata;
  });

  const centerProps = computed(() => {
    if (props.mode === 'result') {
      return {
        homeScore: Number(props.match.home_score),
        awayScore: Number(props.match.away_score),
      };
    } else {
      return {
        date: props.match.date,
        time: props.match.time,
      };
    }
  });
</script>

<style scoped>
  .fixture {
    height: 255px !important;
  }

  .badge {
    align-self: flex-start;
  }
</style>
