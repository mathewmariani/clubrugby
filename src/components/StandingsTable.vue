<template>
  <div class="table-responsive-wrapper">
    <table class="table table-striped table-bordered align-middle text-center fixed-table">
      <thead class="table-light">
        <tr>
          <th class="text-start">Team</th>
          <th
            v-for="col in sortableColumns"
            :key="col.key"
            @click="sortBy(col.key)"
            :class="['sortable', { 'bg-info': sortColumn === col.key }]"
            style="cursor: pointer; white-space: nowrap"
          >
            <div>{{ col.label }}</div>
            <div
              class="caret"
              :class="{
                'text-primary': sortColumn === col.key,
                'text-muted': sortColumn !== col.key,
              }"
            >
              {{ sortColumn === col.key ? (sortDirection === 'asc' ? '▲' : '▼') : '▼' }}
            </div>
          </th>
        </tr>
      </thead>
      <tbody class="table-group-divider">
        <tr v-for="(team, index) in sortedStandings" :key="team.team_id">
          <td class="text-start">
            <div class="d-flex align-items-center gap-2">
              <span class="badge bg-secondary">{{ index + 1 }}</span>
              <img
                v-if="clubs[team.team_id]?.logo"
                :src="clubs[team.team_id].logo"
                :alt="clubs[team.team_id].name"
                width="32"
                height="32"
                style="object-fit: contain"
              />
              <div class="text-truncate">
                <b>{{ clubs[team.team_id]?.name || team.team_id }}</b>
              </div>
            </div>
          </td>
          <td :class="{ 'bg-info': sortColumn === 'gp' }">{{ team.gp }}</td>
          <td :class="{ 'bg-info': sortColumn === 'w' }">{{ team.w }}</td>
          <td :class="{ 'bg-info': sortColumn === 'l' }">{{ team.l }}</td>
          <td :class="{ 'bg-info': sortColumn === 'd' }">{{ team.d }}</td>
          <td :class="{ 'bg-info': sortColumn === 'pts' }"><strong>{{ team.pts }}</strong></td>
          <td :class="{ 'bg-info': sortColumn === 'pf' }">{{ team.pf }}</td>
          <td :class="{ 'bg-info': sortColumn === 'pa' }">{{ team.pa }}</td>
          <td :class="{ 'bg-info': sortColumn === 'diff' }">{{ team.diff }}</td>
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
  data() {
    return {
      sortColumn: 'pts',
      sortDirection: 'desc',
      sortableColumns: [
        { key: 'gp', label: 'P' },
        { key: 'w', label: 'W' },
        { key: 'l', label: 'L' },
        { key: 'd', label: 'D' },
        { key: 'pts', label: 'PTS' },
        { key: 'pf', label: 'PF' },
        { key: 'pa', label: 'PA' },
        { key: 'diff', label: 'PD' },
      ],
    };
  },
  computed: {
    sortedStandings() {
      return Object.values(this.standings)
        .slice()
        .sort((a, b) => {
          const valA = a[this.sortColumn];
          const valB = b[this.sortColumn];

          if (valA === valB) {
            if (this.sortColumn !== 'pts') {
              const ptsDiff = b.pts - a.pts;
              if (ptsDiff !== 0) return ptsDiff;
              return b.diff - a.diff;
            }
            return b.diff - a.diff;
          }

          return this.sortDirection === 'asc' ? valA - valB : valB - valA;
        });
    },
  },
  methods: {
    sortBy(column) {
      if (this.sortColumn === column) {
        this.sortDirection = this.sortDirection === 'asc' ? 'desc' : 'asc';
      } else {
        this.sortColumn = column;
        this.sortDirection = 'desc';
      }
    },
  },
};
</script>

<style scoped>
.table-responsive-wrapper {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

/* Fixed layout and widths */
.fixed-table {
  table-layout: fixed;
  width: 100%;
  min-width: 700px;
  border-collapse: collapse;
}

.fixed-table th,
.fixed-table td {
  vertical-align: middle;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/* Column widths */
.fixed-table th:first-child,
.fixed-table td:first-child {
  width: 45%;
  text-align: left;
}

.fixed-table th:nth-child(n+2),
.fixed-table td:nth-child(n+2) {
  width: 8.75%;
  text-align: center;
}

th.sortable {
  user-select: none;
}

th.sortable:hover {
  background-color: #f5f5f5;
  transition: background-color 0.2s;
}

th .caret {
  font-size: 0.6rem;
  line-height: 1;
  margin-top: 0px;
}
</style>
