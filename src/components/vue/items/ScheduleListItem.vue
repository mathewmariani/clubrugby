<template>
  <div class="list-group-item">
    <div class="d-flex gap-2">
      <div
        :class="[
          'date-circle d-flex flex-column align-items-center justify-content-center text-white',
          matches.length === 1 ? 'circle-shape' : 'capsule-shape',
        ]"
      >
        <small class="fw-bold lh-1">{{ dayNumber }}</small>
        <small class="text-uppercase lh-1 text-muted fw-light">{{
          dayName
        }}</small>
      </div>

      <!-- Matches list -->
      <div class="flex-grow-1 d-flex flex-column justify-content-center gap-3">
        <a
          v-for="match in matches"
          :key="match.id"
          @click="emit('click', match)"
        >
          <div class="d-flex justify-content-between align-items-center">
            <div class="d-flex align-items-center gap-2">
              <template v-if="isHome(match)">
                <small>vs</small>
              </template>
              <template v-else>
                <small>at</small>
              </template>

              <img
                v-if="getOpponent(match)?.logo_url"
                :src="getOpponent(match)?.logo_url"
                :alt="getOpponent(match)?.name"
                width="24"
                height="24"
                style="object-fit: contain"
              />
              <small>{{ getOpponent(match)?.name || 'Unknown' }}</small>
            </div>

            <template v-if="isResult(match)">
              <span
                class="badge"
                :class="{
                  'text-bg-success': didWin(match),
                  'text-bg-danger': !didWin(match),
                }"
              >
                {{ didWin(match) ? 'W' : 'L' }} {{ scoreDisplay(match) }}
              </span>
            </template>
            <template v-else>
              <span class="badge text-bg-danger">{{ match.time }}</span>
            </template>
          </div>
        </a>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { toRef, computed } from 'vue';
  import { useRoute } from 'vue-router';

  import type { Club, League, Fixture, Result } from '../../../utils/types';
  import { useMatchClubs } from '../../../composables/utils';
  import { parseISO, format } from 'date-fns';

  const route = useRoute();
  const clubId = route.params.club_id as string;

  const props = defineProps<{
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
    matches?: (Fixture | Result)[];
  }>();

  const emit = defineEmits<{
    (e: 'click', match: Fixture | Result): void;
  }>();

  // Defensive fallback so matches is always an array
  const matches = computed(() => props.matches ?? []);

  const dateObj = computed(() => {
    if (matches.value.length === 0) return new Date();
    return parseISO(matches.value[0].date);
  });

  const dayName = computed(() => format(dateObj.value, 'EEE')); // e.g. Wed
  const dayNumber = computed(() => format(dateObj.value, 'd')); // e.g. 18

  function isResult(match: Fixture | Result): match is Result {
    return 'home_score' in match && 'away_score' in match;
  }

  function isHome(match: Fixture | Result): boolean {
    return String(match.home_id) === clubId;
  }

  function isAway(match: Fixture | Result): boolean {
    return String(match.away_id) === clubId;
  }

  function getOpponent(match: Fixture | Result) {
    // useMatchClubs expects a ref, so create a computed ref wrapping the match
    const matchRef = toRef({ value: match }, 'value');
    const { home, away } = useMatchClubs(matchRef, props.clubs);
    if (isHome(match)) return away?.value || null;
    if (isAway(match)) return home?.value || null;
    return null;
  }

  function didWin(match: Result): boolean {
    if (!isResult(match)) return false;
    const homeScore = Number(match.home_score);
    const awayScore = Number(match.away_score);
    return isHome(match)
      ? homeScore > awayScore
      : isAway(match)
        ? awayScore > homeScore
        : false;
  }

  function scoreDisplay(match: Result): string {
    if (!isResult(match)) return '';
    return `${match.home_score} - ${match.away_score}`;
  }
</script>

<style scoped>
  .date-circle {
    width: 42px;
    user-select: none;
    cursor: default;
    padding: 8px 0;
    min-width: 42px;
    flex-shrink: 0;
    background-color: var(--bs-secondary);
    color: white;

    /* center content */
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  /* circle shape for single match */
  .circle-shape {
    height: 42px;
    border-radius: 50%;
  }

  /* capsule shape for multiple matches */
  .capsule-shape {
    border-radius: 21px; /* half width for pill shape */
    padding-top: 16px;
    padding-bottom: 16px;
    height: auto;
    /* stretch vertically to fill parent's height */
    align-self: stretch;
  }
</style>
