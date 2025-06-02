<template>
  <div class="table-responsive-wrapper">
    <div v-for="leagueGroup in groupedStandings" :key="leagueGroup.leagueId">
      <table class="table table-fixed table-striped align-middle text-center">
        <thead>
          <tr>
            <th class="text-start">
              {{ leagues[leagueGroup.leagueId].name || leagueGroup.leagueId }}
            </th>
            <th
              v-for="col in sortableColumns"
              :key="col.key"
              :class="['sortable', { 'has-border': sortColumn === col.key }]"
              style="white-space: nowrap"
            >
              <button
                @click.prevent="sortBy(col.key)"
                class="w-100 bg-transparent border-0 text-dark p-0 m-0"
                style="cursor: pointer"
              >
                <div>
                  <strong>{{ col.label }}</strong>
                </div>
                <div
                  class="caret"
                  :class="{
                    'text-primary': sortColumn === col.key,
                    'text-light': sortColumn !== col.key,
                  }"
                >
                  {{
                    sortColumn === col.key
                      ? sortDirection === 'asc'
                        ? '▲'
                        : '▼'
                      : '▼'
                  }}
                </div>
              </button>
            </th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="team in leagueGroup.teams"
            :key="leagueGroup.leagueId + '-' + team.team_id"
          >
            <td class="text-start">
              <div class="d-flex align-items-center gap-2">
                <span
                  :class="
                    team.pos <= 4 ? 'badge bg-primary' : 'badge bg-secondary'
                  "
                >
                  {{ team.pos }}
                </span>
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
            <td :class="{ 'has-border': sortColumn === 'gp' }">
              {{ team.gp }}
            </td>
            <td :class="{ 'has-border': sortColumn === 'w' }">{{ team.w }}</td>
            <td :class="{ 'has-border': sortColumn === 'l' }">{{ team.l }}</td>
            <td :class="{ 'has-border': sortColumn === 'd' }">{{ team.d }}</td>
            <td :class="{ 'has-border': sortColumn === 'pts' }">
              <strong>{{ team.pts }}</strong>
            </td>
            <td :class="{ 'has-border': sortColumn === 'pf' }">
              {{ team.pf }}
            </td>
            <td :class="{ 'has-border': sortColumn === 'pa' }">
              {{ team.pa }}
            </td>
            <td :class="{ 'has-border': sortColumn === 'diff' }">
              {{ team.diff }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
  import { ref, computed } from 'vue';

  defineProps({
    standings: Object,
    clubs: Object,
    leagues: Object,
    lastModified: String,
  });

  const sortColumn = ref('pts');
  const sortDirection = ref('desc');

  const sortableColumns = [
    { key: 'gp', label: 'P' },
    { key: 'w', label: 'W' },
    { key: 'l', label: 'L' },
    { key: 'd', label: 'D' },
    { key: 'pts', label: 'PTS' },
    { key: 'pf', label: 'PF' },
    { key: 'pa', label: 'PA' },
    { key: 'diff', label: 'PD' },
  ];

  function sortBy(column) {
    if (sortColumn.value === column) {
      sortDirection.value = sortDirection.value === 'asc' ? 'desc' : 'asc';
    } else {
      sortColumn.value = column;
      sortDirection.value = 'desc';
    }
  }

  const groupedStandings = computed(() => {
    return Object.entries(__props.standings).map(([leagueId, teams]) => {
      const sorted = Object.values(teams)
        .slice()
        .sort((a, b) => {
          const valA = a[sortColumn.value];
          const valB = b[sortColumn.value];

          if (valA === valB) {
            if (sortColumn.value !== 'pts') {
              const ptsDiff = b.pts - a.pts;
              if (ptsDiff !== 0) return ptsDiff;
              return b.diff - a.diff;
            }
            return b.diff - a.diff;
          }

          return sortDirection.value === 'asc' ? valA - valB : valB - valA;
        });

      return { leagueId, teams: sorted };
    });
  });
</script>

<style scoped>
  .table-responsive-wrapper {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    border: 1px solid #dee2e6;
  }

  .table-responsive-wrapper > div:not(:last-of-type) > .table-fixed {
    border-bottom: 1px solid #dee2e6;
  }

  .table-fixed {
    table-layout: fixed;
    width: 100%;
    min-width: 700px;
    margin-bottom: 0;
  }

  /* Remove default borders and set base style */
  .table-fixed th,
  .table-fixed td {
    vertical-align: middle;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    border: none;
  }

  /* First column: fixed width and right border */
  .table-fixed th:first-child,
  .table-fixed td:first-child {
    width: 45%;
    text-align: left;
    border-right: 1px solid #dee2e6;
  }

  /* Other columns: equal width */
  .table-fixed th:nth-child(n + 2),
  .table-fixed td:nth-child(n + 2) {
    width: 8.75%;
    text-align: center;
  }

  /* Sorted column border rules */
  .table-fixed th.has-border,
  .table-fixed td.has-border {
    border-right: 1px solid #dee2e6;
  }

  /* Sorted column: left border unless it's the second column */
  .table-fixed th.has-border:not(:nth-child(2)),
  .table-fixed td.has-border:not(:nth-child(2)) {
    border-left: 1px solid #dee2e6;
  }

  /* Caret style */
  th .caret {
    font-size: 0.6rem;
    line-height: 1;
    margin-top: 0px;
  }
</style>
