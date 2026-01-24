<template>
  <div class="list-group-item">
    <div class="d-flex gap-2">
      <!-- Date capsule -->
      <div
        class="capsule-shape capsule-date d-flex flex-column align-items-center justify-content-center bg-body-tertiary"
      >
        <span class="fw-bold text-body-emphasis lh-1">{{ dayNumber }}</span>
        <small class="text-uppercase text-body-secondary lh-1">
          {{ dayName }}
        </small>
      </div>

      <!-- Matches list -->
      <div class="flex-grow-1 d-flex flex-column justify-content-center gap-3">
        <a
          v-for="match in matches"
          :key="match.fixtureId"
          class="list-group-item-action text-decoration-none"
          role="button"
          @click.prevent="goToEvent(match)"
        >
          <div class="d-flex justify-content-between align-items-center">
            <!-- Opponent -->
            <div class="d-flex align-items-center gap-2 flex-grow-1 min-width-0">
              <span class="fw-normal text-muted flex-shrink-0">
                {{ isHome(match) ? 'vs' : 'at' }}
              </span>

              <img
                v-if="getOpponent(match)?.logo"
                :src="getOpponent(match)?.logo"
                :alt="getOpponent(match)?.name || ''"
                width="24"
                height="24"
                class="logo-img flex-shrink-0"
              />

              <div class="flex-grow-1 min-width-0">
                <span class="text-body-emphasis fw-normal">
                  {{ getOpponent(match)?.name || 'Unknown' }}
                </span>
                <small class="text-body-secondary d-block">
                  {{ getLeagueName(match.leagueId, leagues) || 'Unknown league' }}
                </small>
              </div>
            </div>

            <!-- Right side -->
            <div class="d-flex align-items-center gap-1 flex-shrink-0 text-muted">
              <template v-if="isResult(match)">
                <span
                  class="badge text-center"
                  :class="{
                    'text-bg-success': didWin(match),
                    'text-bg-danger': !didWin(match),
                  }"
                >
                  {{ didWin(match) ? 'W' : 'L' }}
                </span>
              </template>
              <template v-else>
                <span class="text-body-secondary">
                  {{ timeLabel(match.fixtureDate) }}
                </span>
              </template>
            </div>
          </div>
        </a>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, toRef } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { format } from 'date-fns';

import type { Club, Fixture } from '@/utils/types';
import { useMatchClubs, getLeagueName } from '@/composables/utils';

const route = useRoute();
const router = useRouter();
const clubId = route.params.club_id as string;

const props = defineProps<{
  clubs: Record<string, Club>;
  leagues: Record<string, string>;
  fixtures: Fixture[];
}>();

const matches = computed(() => props.fixtures ?? []);

/* --- Date helpers --- */

const firstMatchDate = computed(() => {
  if (!matches.value.length) return new Date();
  return new Date(matches.value[0].fixtureDate * 1000);
});

const dayName = computed(() => format(firstMatchDate.value, 'EEE'));
const dayNumber = computed(() => format(firstMatchDate.value, 'd'));

function timeLabel(unixSeconds: number): string {
  return format(new Date(unixSeconds * 1000), 'HH:mm');
}

/* --- Match helpers --- */

function isResult(match: Fixture) {
  return match.fixtureStatus === 'result';
}

function isHome(match: Fixture) {
  return match.homeClubId === clubId;
}

function isAway(match: Fixture) {
  return match.awayClubId === clubId;
}

function getOpponent(match: Fixture) {
  const matchRef = toRef({ value: match }, 'value');
  const { home, away } = useMatchClubs(matchRef, props.clubs);
  if (isHome(match)) return away?.value ?? null;
  if (isAway(match)) return home?.value ?? null;
  return null;
}

function didWin(match: Fixture): boolean {
  if (!isResult(match)) return false;
  const home = Number(match.homeScore);
  const away = Number(match.awayScore);
  return isHome(match) ? home > away : away > home;
}

function goToEvent(match: Fixture) {
  router.push({ path: `/event/${match.fixtureId}` });
}
</script>

<style scoped>
.capsule-date {
  width: 32px;
  user-select: none;
  cursor: default;
  padding: 8px 0;
  min-width: 32px;
  flex-shrink: 0;
}

.capsule-shape {
  border-radius: 16px;
  padding-top: 16px;
  padding-bottom: 16px;
  align-self: stretch;
}

small {
  font-size: 0.75em;
}

.logo-img {
  object-fit: contain;
  display: block;
}
</style>
