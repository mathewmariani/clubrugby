<template>
  <div class="card h-100">
    <div class="card-body">
      <h6><span class="badge text-bg-light">Final</span></h6>

      <!-- Home team -->
      <div class="d-flex justify-content-between align-items-center mb-2">
        <div class="d-flex align-items-center">
          <img :src="clubs[match.home_id]?.logo" alt="" width="32" height="32" class="me-2" />
          <span>
            <strong>{{ clubs[match.home_id]?.name || match.home_id }}</strong><br />
            <small class="text-muted">{{ getRecord(match.home_id) }}</small>
          </span>
        </div>
        <strong :class="scoreClass(match.home_score, match.away_score)">
          {{ match.home_score || '-' }}
        </strong>
      </div>

      <!-- Away team -->
      <div class="d-flex justify-content-between align-items-center mb-2">
        <div class="d-flex align-items-center">
          <img :src="clubs[match.away_id]?.logo" alt="" width="32" height="32" class="me-2" />
          <span>
            <strong>{{ clubs[match.away_id]?.name || match.away_id }}</strong><br />
            <small class="text-muted">{{ getRecord(match.away_id) }}</small>
          </span>
        </div>
        <strong :class="scoreClass(match.away_score, match.home_score)">
          {{ match.away_score || '-' }}
        </strong>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ResultCard',
  props: {
    match: { type: Object, required: true },
    clubs: { type: Object, required: true },
    standings: { type: Object, required: false }, // optional standings prop
  },
  methods: {
    scoreClass(score, opponentScore) {
      const s = parseInt(score, 10);
      const o = parseInt(opponentScore, 10);
      if (isNaN(s) || isNaN(o)) return '';
      return s > o ? 'text-success' : s < o ? 'text-danger' : '';
    },
    getRecord(teamId) {
      if (!this.standings) return '0-0-0';
      const record = this.standings[teamId];
      return record ? `${record.w}-${record.d}-${record.l}` : '0-0-0';
    },
  },
};
</script>
