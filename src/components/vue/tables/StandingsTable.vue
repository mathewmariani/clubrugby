<template>
  <div>
    <table class="table table-borderless table-fixed">
      <thead class="sticky-thead">
        <tr>
          <th>{{ title }}</th>
          <th v-for="col in columns" :key="col.key">
            <span class="fw-normal">{{ col.label }}</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="team in teams" :key="team.team_id">
          <td>
            <div class="d-flex align-items-center gap-2">
              <span class="text-body-secondary fw-light">{{ team.pos }}</span>
              <img
                v-if="clubs[team.club_id]?.logo"
                :src="clubs[team.club_id].logo"
                :alt="clubs[team.club_id].name"
                width="32"
                height="32"
                style="object-fit: contain"
              />
              <span class="text-body-emphasis text-truncate">
                {{ clubs[team.club_id]?.name || team.club_id }}
              </span>
            </div>
          </td>

          <td v-for="col in columns" :key="col.key" class="text-nowrap">
            <template v-if="col.key === 'w-d-l'">
              {{ team.gamesWon }}-{{ team.gamesDraw }}-{{ team.gameLost }}
            </template>
            <template v-else>
              {{ team[col.key] }}
            </template>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
  import type { Club, Standing } from '@/utils/types';
  import { useLayout } from '@/composables/useLayout';

  const { navbarHeight } = useLayout();

  defineProps<{
    title: string;
    teams: Standing[];
    clubs: Record<string, Club>;
    columns: { key: keyof Standing | 'w-d-l'; label: string }[];
  }>();
</script>

<style scoped>
  .table-fixed {
    table-layout: fixed;
    width: 100%;
    min-width: 700px;
    margin-bottom: 0px;
  }

  .table-fixed th,
  .table-fixed td {
    vertical-align: middle;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    background-color: var(--bs-body-bg);
  }

  tbody tr:not(:last-child) {
    border-bottom: var(--bs-border-width) solid var(--bs-border-color);
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
    z-index: 5;
    top: 88px;
    background: var(--bs-body-tertiary-bg, var(--bs-tertiary-bg));
  }
</style>
