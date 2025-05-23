<template>
  <div class="card fixture">
    <div
      class="card-body d-flex flex-column align-items-center justify-content-between"
    >
      <div class="my-auto d-flex align-items-center justify-content-between">
        <TeamBlock :club="clubs[match.home_id]" />
        <MatchScore
          :homeScore="Number(match.home_score)"
          :awayScore="Number(match.away_score)"
        />
        <TeamBlock :club="clubs[match.away_id]" />
      </div>
      <MatchVenue :venue="match.venue" />
    </div>
  </div>
</template>

<script>
  import MatchMetadata from './MatchMetadata.vue';
  import TeamBlock from './TeamBlock.vue';
  import MatchScore from './MatchScore.vue';
  import MatchVenue from './MatchVenue.vue';

  export default {
    name: 'ResultCard',
    components: {
      MatchMetadata,
      TeamBlock,
      MatchScore,
      MatchVenue,
    },
    props: {
      match: { type: Object, required: true },
      clubs: { type: Object, required: true },
    },
  };
</script>

<style scoped>
  .fixture {
    height: 255px !important;
  }
</style>
