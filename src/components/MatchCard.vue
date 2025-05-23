<template>
  <div class="card h-100 mb-3">
    <div class="card-body d-flex flex-column align-items-center">
      <!-- Teams and match metadata row -->
      <div
        class="d-flex justify-content-center align-items-center text-center w-100 mb-3 gap-5"
      >
        <!-- Home team -->
        <div class="team-block d-flex flex-column align-items-center">
          <img
            :src="clubs[match.home_id]?.logo"
            alt="Home team logo"
            width="64"
            height="64"
            class="team-logo"
          />
          <div class="team-name mt-1">
            {{ clubs[match.home_id]?.name || match.home_id }}<br />
            <small class="text-muted">{{ getRecord(match.home_id) }}</small>
          </div>
        </div>

        <!-- Match metadata (center column) -->
        <div
          class="d-flex flex-column align-items-center justify-content-center metadata"
        >
          <span class="badge text-bg-light mb-1">{{ match.time }}</span>
          <span class="badge text-bg-light">{{ match.date }}</span>
        </div>

        <!-- Away team -->
        <div class="team-block d-flex flex-column align-items-center">
          <img
            :src="clubs[match.away_id]?.logo"
            alt="Away team logo"
            width="64"
            height="64"
            class="team-logo"
          />
          <div class="team-name mt-1">
            {{ clubs[match.away_id]?.name || match.away_id }}<br />
            <small class="text-muted">{{ getRecord(match.away_id) }}</small>
          </div>
        </div>
      </div>

      <!-- Match venue -->
      <div>
        <span class="badge text-bg-light venue-badge">{{ match.venue }}</span>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'MatchCard',
    props: {
      match: { type: Object, required: true },
      clubs: { type: Object, required: true },
      standings: { type: Object, required: true },
    },
    methods: {
      getRecord(teamId) {
        const record = this.standings?.[teamId];
        return record ? `${record.w}-${record.d}-${record.l}` : '0-0-0';
      },
    },
  };
</script>

<style scoped>
  .card {
    border: 1px solid #ddd;
    border-radius: 4px;
  }

  .team-block {
    max-width: 140px;
    text-align: center;
  }

  .team-logo {
    object-fit: contain;
  }

  .team-name {
    font-size: 0.85rem;
    white-space: normal;
    word-wrap: break-word;
    overflow-wrap: break-word;
    max-width: 140px;
    margin-top: 0.25rem;
  }

  .metadata {
    font-size: 0.9rem;
  }

  .venue-badge {
    font-size: 0.8rem;
    padding: 0.3em 0.6em;
  }
</style>
