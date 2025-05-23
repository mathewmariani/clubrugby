<template>
  <div class="table-responsive-wrapper">
    <table class="table table-striped table-bordered align-middle">
      <thead class="table-light">
        <tr>
          <th class="text-start">Team</th>
          <th>P</th>
          <th>W</th>
          <th>L</th>
          <th>D</th>
          <th>PTS</th>
          <th>PF</th>
          <th>PA</th>
          <th>PD</th>
        </tr>
      </thead>
      <tbody class="table-group-divider">
        <tr v-for="(team, index) in sortedStandings" :key="team.team_id">
          <td class="d-flex align-items-center gap-2">
            <span class="badge bg-secondary">{{ index + 1 }}</span>
            <img
              v-if="clubs[team.team_id]?.logo"
              :src="clubs[team.team_id].logo"
              :alt="clubs[team.team_id].name"
              width="32"
              height="32"
              style="object-fit: contain"
            />
            <div class="text-truncate" style="max-width: 180px">
              {{ clubs[team.team_id]?.name || team.team_id }}
            </div>
          </td>
          <td>{{ team.pld }}</td>
          <td>{{ team.w }}</td>
          <td>{{ team.l }}</td>
          <td>{{ team.d }}</td>
          <td>
            <strong>{{ team.pts }}</strong>
          </td>
          <td>{{ team.pf }}</td>
          <td>{{ team.pa }}</td>
          <td>{{ team.diff }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  export default {
    name: 'StandingsTable',
    props: {
      standings: Object,
      clubs: Object,
      lastModified: String,
    },
    computed: {
      sortedStandings() {
        return Object.values(this.standings)
          .slice()
          .sort((a, b) => {
            const ptsDiff = b.pts - a.pts;
            return ptsDiff !== 0 ? ptsDiff : b.diff - a.diff;
          });
      },
    },
  };
</script>

<style scoped>
  .table-responsive-wrapper {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }

  .table {
    min-width: 700px;
  }

  .table td,
  .table th {
    vertical-align: middle;
  }
</style>
