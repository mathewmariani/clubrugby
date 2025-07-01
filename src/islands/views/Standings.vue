<template>
  <template v-if="hasStandings">
    <div>
      <template
        v-for="leagueGroup in groupedStandings"
        :key="leagueGroup.leagueId"
      >
        <!-- League with divisions -->
        <template v-if="leagueGroup.divisions">
          <template
            v-for="division in leagueGroup.divisions"
            :key="division.division"
          >
            <table class="table table-fixed align-middle text-center">
              <thead class="sticky-thead">
                <tr>
                  <th class="text-start">{{ division.division }}</th>
                  <th v-for="col in sortableColumns" :key="col.key">
                    {{ col.label }}
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="team in division.teams" :key="team.team_id">
                  <td class="text-start">
                    <div class="d-flex align-items-center gap-2">
                      <span
                        :class="
                          team.pos <= 4
                            ? 'badge bg-primary'
                            : 'badge bg-secondary'
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
                        {{ clubs[team.team_id]?.name || team.team_id }}
                      </div>
                    </div>
                  </td>
                  <td
                    v-for="col in sortableColumns"
                    :key="col.key"
                    class="text-nowrap"
                  >
                    <template v-if="col.key === 'w'">
                      {{ team.w }}-{{ team.l }}-{{ team.d }}
                    </template>
                    <template v-else>
                      {{ team[col.key] }}
                    </template>
                  </td>
                </tr>
              </tbody>
            </table>
          </template>
        </template>

        <!-- League without divisions -->
        <template v-else>
          <table class="table table-fixed align-middle text-center">
            <thead class="sticky-thead">
              <tr>
                <th class="text-start">
                  {{
                    leagues[leagueGroup.leagueId]?.name || leagueGroup.leagueId
                  }}
                </th>
                <th v-for="col in sortableColumns" :key="col.key">
                  {{ col.label }}
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="team in leagueGroup.teams" :key="team.team_id">
                <td class="text-start">
                  <div class="d-flex align-items-center gap-2">
                    <span
                      :class="
                        team.pos <= 4
                          ? 'badge bg-primary'
                          : 'badge bg-secondary'
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
                      {{ clubs[team.team_id]?.name || team.team_id }}
                    </div>
                  </div>
                </td>
                <td
                  v-for="col in sortableColumns"
                  :key="col.key"
                  class="text-nowrap"
                >
                  <template v-if="col.key === 'w'">
                    {{ team.w }}-{{ team.l }}-{{ team.d }}
                  </template>
                  <template v-else>
                    {{ team[col.key] }}
                  </template>
                </td>
              </tr>
            </tbody>
          </table>
        </template>
      </template>
    </div>
  </template>

  <template v-else>
    <div class="container-fluid text-center text-muted pt-3">
      <p>No standings available.</p>
      <hr />
      <p>Ensure your preferences are set.</p>
    </div>
  </template>
</template>

<script setup lang="ts">
  import { ref, toRef } from 'vue';
  import type { Club, League, Standing } from '@/utils/types';
  import { useSavedLeagues } from '@/composables/useSavedLeagues';
  import { useFilteredStandings } from '@/composables/useFilteredStandings';

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

  const sortableColumns = [
    { key: 'pld', label: 'PLD' },
    { key: 'w', label: 'W-L-D' },
    { key: 'pts', label: 'PTS' },
    { key: 'pf', label: 'PF' },
    { key: 'pa', label: 'PA' },
    { key: 'diff', label: 'PD' },
  ];
</script>

<style scoped>
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
    background-color: var(--bs-body-bg);
  }

  .table-fixed th:first-child,
  .table-fixed td:first-child {
    width: 30%;
    text-align: left;
  }

  .table-fixed th:nth-child(n + 2),
  .table-fixed td:nth-child(n + 2) {
    width: 8.75%;
    text-align: center;
  }

  .sticky-thead th {
    position: sticky;
    top: 88px;
    z-index: 5;
    background: var(--bs-body-tertiary-bg, var(--bs-tertiary-bg));
  }
</style>
