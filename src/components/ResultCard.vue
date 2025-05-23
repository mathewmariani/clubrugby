<template>
  <div class="card h-100 mb-3">
    <div class="card-body d-flex flex-column align-items-center">
      <!-- Metadata: Date and Time -->
      <div class="metadata mb-3 text-center">
        <span class="badge text-bg-light me-2">{{ match.date }}</span>
        <span class="badge text-bg-light">{{ match.time }}</span>
      </div>

      <!-- Center: Home logo, Score, Away logo -->
      <div
        class="score-row d-flex align-items-center justify-content-center mb-2 gap-5"
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
          <div
            class="team-name mt-1"
            :title="clubs[match.home_id]?.name || match.home_id"
          >
            {{ clubs[match.home_id]?.name || match.home_id }}
          </div>
        </div>

        <!-- Score -->
        <div
          class="score d-flex align-items-center justify-content-center fs-4 fw-bold"
        >
          <span
            :class="scoreClass(match.home_score, match.away_score)"
            class="score-number"
          >
            {{ match.home_score ?? '-' }}
          </span>
          <span class="score-dash mx-2">-</span>
          <span
            :class="scoreClass(match.away_score, match.home_score)"
            class="score-number"
          >
            {{ match.away_score ?? '-' }}
          </span>
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
          <div
            class="team-name mt-1"
            :title="clubs[match.away_id]?.name || match.away_id"
          >
            {{ clubs[match.away_id]?.name || match.away_id }}
          </div>
        </div>
      </div>

      <!-- Venue -->
      <div>
        <span class="badge text-bg-light venue-badge">{{ match.venue }}</span>
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
    },
    methods: {
      scoreClass(score, opponentScore) {
        const s = parseInt(score, 10);
        const o = parseInt(opponentScore, 10);
        if (isNaN(s) || isNaN(o)) return '';
        if (s > o) return 'text-success';
        if (s < o) return 'text-danger';
        return '';
      },
    },
  };
</script>

<style scoped>
  .card {
    border: 1px solid #ddd;
    border-radius: 4px;
  }

  .metadata {
    font-size: 0.9rem;
    color: #555;
  }

  .score-row {
    gap: 3rem;
    justify-content: center;
    align-items: center;
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
    color: #444;
    white-space: normal; /* allow wrapping */
    overflow-wrap: break-word;
    max-width: 140px;
    margin-top: 0.25rem;
  }

  .score {
    white-space: nowrap;
  }

  .score-number {
    min-width: 20px; /* consistent width for numbers */
    text-align: center;
    display: inline-block;
  }

  .score-dash {
    font-weight: normal;
    color: #666;
  }

  .venue-badge {
    font-size: 0.8rem;
    padding: 0.3em 0.6em;
  }

  /* Score colors */
  .text-success {
    color: #198754; /* bootstrap success green */
  }

  .text-danger {
    color: #dc3545; /* bootstrap danger red */
  }
</style>
