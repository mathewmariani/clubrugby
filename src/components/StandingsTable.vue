<!-- StandingsTable.vue -->
<template>
    <table class="table table-striped table-bordered">
      <thead>
        <tr>
          <th>Pos</th>
          <th>Team</th>
          <th>Pld</th>
          <th>W</th>
          <th>D</th>
          <th>L</th>
          <th class="border-end">PF</th>
          <th>PA</th>
          <th>Diff</th>
          <th>TF</th>
          <th>TA</th>
          <th>TD</th>
          <th>Pts</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="team in standings" :key="team.team_id">
          <td>{{ team.pos }}</td>
          <td class="d-flex align-items-center">
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
          <td>{{ team.d }}</td>
          <td>{{ team.l }}</td>
          <td class="border-end">{{ team.pf }}</td>
          <td>{{ team.pa }}</td>
          <td>{{ team.diff }}</td>
          <td>{{ team.tf }}</td>
          <td>{{ team.ta }}</td>
          <td>{{ team.td }}</td>
          <td>{{ team.pts }}</td>
        </tr>
      </tbody>
    </table>
  </template>
  
  <script>
  export default {
    name: 'StandingsTable',
    props: {
      standings: {
        type: Array,
        required: true,
      },
      clubs: {
        type: Object,
        required: true,
      },
    },
  };
  </script>
  