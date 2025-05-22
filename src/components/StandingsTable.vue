<template>
  <table class="table table-striped table-bordered">
    <caption>Last updated: {{ lastModified }}</caption>
    <thead>
      <tr>
        <th>Team</th>
        <th>GP</th>
        <th>W</th>
        <th>L</th>
        <th>T</th>
        <th>PTS</th>
        <th>PF</th>
        <th>PA</th>
        <th>Diff</th>
        <th>TF</th>
        <th>TA</th>
        <th>TD</th>
      </tr>
    </thead>
    <tbody class="table-group-divider">
      <tr v-for="team in teamStandingsArray" :key="team.team_id">
        <td class="d-flex align-items-center">
          <span class="badge me-2 text-bg-secondary">{{ team.pos }}</span>
          <img
            v-if="clubs[team.team_id]?.logo"
            :src="clubs[team.team_id].logo"
            :alt="clubs[team.team_id].name"
            width="32"
            height="32"
            class="me-2"
            style="object-fit: contain;"
          />
          <span><strong>{{ clubs[team.team_id]?.name || team.team_id }}</strong></span>
        </td>
        <td>{{ team.pld }}</td>
        <td>{{ team.w }}</td>
        <td>{{ team.l }}</td>
        <td>{{ team.d }}</td>
        <td>{{ team.pts }}</td>
        <td>{{ team.pf }}</td>
        <td>{{ team.pa }}</td>
        <td>{{ team.diff }}</td>
        <td>{{ team.tf }}</td>
        <td>{{ team.ta }}</td>
        <td>{{ team.td }}</td>
      </tr>
    </tbody>
  </table>
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
    teamStandingsArray() {
      return Object.values(this.standings);
    },
  },
};
</script>
