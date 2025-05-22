<template>
  <div class="card h-100 mb-3">
    <div class="card-body">
      <!-- Match info: time and venue -->
      <div class="d-flex align-items-center mb-2">
        <h6 class="mb-0 me-2">
          <span class="badge text-bg-light">{{ match.time }}</span>
        </h6>
        <h6 class="mb-0">
          <span class="badge text-bg-light">{{ match.venue }}</span>
        </h6>
      </div>

      <!-- Home team -->
      <div class="d-flex justify-content-between align-items-center mb-2">
        <div class="d-flex align-items-center">
          <img
            :src="clubs[match.home_id]?.logo"
            alt=""
            width="32"
            height="32"
            class="me-2"
          />
          <div>
            <strong>{{ clubs[match.home_id]?.name || match.home_id }}</strong><br />
            <small class="text-muted">{{ getRecord(match.home_id) }}</small>
          </div>
        </div>
      </div>

      <!-- Away team -->
      <div class="d-flex justify-content-between align-items-center mb-2">
        <div class="d-flex align-items-center">
          <img
            :src="clubs[match.away_id]?.logo"
            alt=""
            width="32"
            height="32"
            class="me-2"
          />
          <div>
            <strong>{{ clubs[match.away_id]?.name || match.away_id }}</strong><br />
            <small class="text-muted">{{ getRecord(match.away_id) }}</small>
          </div>
        </div>
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
</style>
