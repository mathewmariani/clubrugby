<template>
  <template v-if="hasStandings">
    <div class="table-responsive-wrapper">
      <template
        v-for="leagueGroup in groupedStandings"
        :key="leagueGroup.leagueId"
      >
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
                  class="w-100 bg-transparent border-0 p-0 m-0"
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
                    v-if="clubs[team.team_id]?.logo_url"
                    :src="clubs[team.team_id].logo_url"
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
              <td :class="{ 'has-border': sortColumn === 'w' }">
                {{ team.w }}
              </td>
              <td :class="{ 'has-border': sortColumn === 'l' }">
                {{ team.l }}
              </td>
              <td :class="{ 'has-border': sortColumn === 'd' }">
                {{ team.d }}
              </td>
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
      </template>
    </div>
  </template>
  <template v-else>
    <div class="container mt-3 text-center text-muted">
      <p>No standings available.</p>
      <p>Ensure your preferences are set.</p>
    </div>
  </template>
</template>

<script setup lang="ts">
  import { ref, toRef } from 'vue';
  import type { Club, League, Standing } from '../../../utils/types';
  import { useSavedLeagues } from '../../../composables/useSavedLeagues';
  import { useFilteredStandings } from '../../../composables/useFilteredStandings';

  const props = defineProps<{
    standings: Record<string, Standing[]>;
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
  }>();

  const sortColumn = ref<keyof Standing>('pts');
  const sortDirection = ref<'asc' | 'desc'>('desc');

  const { savedLeagues } = useSavedLeagues();

  const { groupedStandings, hasStandings } = useFilteredStandings(
    toRef(props, 'standings'),
    savedLeagues,
    sortColumn,
    sortDirection
  );

  function sortBy(column: keyof Standing) {
    if (sortColumn.value === column) {
      sortDirection.value = sortDirection.value === 'asc' ? 'desc' : 'asc';
    } else {
      sortColumn.value = column;
      sortDirection.value = 'desc';
    }
  }

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
</script>

<style scoped>
  .table-responsive-wrapper {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
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

  .table-fixed th,
  .table-fixed td {
    vertical-align: middle;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    border: none;
  }

  .table-fixed th:first-child,
  .table-fixed td:first-child {
    width: 45%;
    text-align: left;
    border-right: 1px solid #dee2e6;
  }

  .table-fixed th:nth-child(n + 2),
  .table-fixed td:nth-child(n + 2) {
    width: 8.75%;
    text-align: center;
  }

  .table-fixed th.has-border,
  .table-fixed td.has-border {
    border-right: 1px solid #dee2e6;
  }

  .table-fixed th.has-border:not(:nth-child(2)),
  .table-fixed td.has-border:not(:nth-child(2)) {
    border-left: 1px solid #dee2e6;
  }

  th .caret {
    font-size: 0.6rem;
    line-height: 1;
    margin-top: 0px;
  }
</style>
