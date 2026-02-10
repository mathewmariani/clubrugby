<template>
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
      <tr v-for="standing in standings" :key="standing.team_id">
        <td>
          <div class="d-flex align-items-center gap-2">
            <span class="text-body-secondary fw-light">{{ standing.pos }}</span>

            <img
              v-if="clubs[standing.club_id]?.logo"
              :src="clubs[standing.club_id].logo"
              :alt="clubs[standing.club_id].name"
              width="32"
              height="32"
              style="object-fit: contain"
            />

            <span class="text-body-emphasis text-truncate">
              {{ clubs[standing.club_id]?.name || standing.club_id }}
            </span>
          </div>
        </td>

        <td v-for="col in columns" :key="col.key" class="text-nowrap">
          <template v-if="col.key === 'w-d-l'">
            {{ standing.gamesWon }}-{{ standing.gamesDraw }}-{{
              standing.gameLost
            }}
          </template>
          <template v-else>
            {{ standing[col.key] }}
          </template>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup lang="ts">
  import type { Standing } from '@/utils/types';
  import { useAppData } from '@/composables/useAppData';

  const { clubs } = useAppData();

  const props = defineProps<{
    title: string;
    standings: Standing[];
    columns: { key: keyof Standing | 'w-d-l'; label: string }[];
  }>();
</script>

<style scoped>
  .text-truncate {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
</style>
