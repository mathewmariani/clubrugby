<template>
  <div class="list-group-item">
    <div class="d-flex gap-2">
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
          :key="match.id"
          class="list-group-item-action text-decoration-none"
          role="button"
          @click.prevent="goToEvent(match)"
        >
          <div class="d-flex justify-content-between align-items-center">
            <!-- Opponent info -->
            <div
              class="d-flex align-items-center gap-2 flex-grow-1 min-width-0"
            >
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

              <!-- Opponent name container with truncate -->
              <div class="flex-grow-1 min-width-0">
                <span class="text-body-emphasis fw-normal">
                  {{ getOpponent(match)?.name || 'Unknown' }}
                </span>
                <small class="text-body-secondary d-block">
                  {{ getLeagueName(match?.league_id, leagues) || 'Unknown' }}
                </small>
              </div>
            </div>

            <!-- Right: badge/time -->
            <div
              class="d-flex align-items-center gap-1 flex-shrink-0 text-muted"
            >
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
                <div class="d-flex align-items-center gap-1">
                  <span class="text-body-secondary">{{ match.time }}</span>
                </div>
              </template>
            </div>
          </div>
        </a>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { toRef, computed } from 'vue';
  import { useRoute, useRouter } from 'vue-router';

  import type { Club, League, Fixture } from '@/utils/types';
  import { useMatchClubs, getLeagueName } from '@/composables/utils';
  import { parseISO, format } from 'date-fns';

  const route = useRoute();
  const router = useRouter();
  const clubId = route.params.club_id as string;

  const props = defineProps<{
    clubs: Record<string, Club>;
    leagues: Record<string, string>;
    matches?: Fixture[];
  }>();

  // Defensive fallback so matches is always an array
  const matches = computed(() => props.matches ?? []);

  const dateObj = computed(() => {
    if (matches.value.length === 0) return new Date();
    return parseISO(matches.value[0].date);
  });

  const dayName = computed(() => format(dateObj.value, 'EEE')); // e.g. Wed
  const dayNumber = computed(() => format(dateObj.value, 'd')); // e.g. 18

  function isResult(match: Fixture): boolean {
    return match.fixtureStatus === "result";
  }

  function isHome(match: Fixture): boolean {
    return String(match.homeClubId) === clubId;
  }

  function isAway(match: Fixture): boolean {
    return String(match.awayClubId) === clubId;
  }

  function getOpponent(match: Fixture) {
    // useMatchClubs expects a ref, so create a computed ref wrapping the match
    const matchRef = toRef({ value: match }, 'value');
    const { home, away } = useMatchClubs(matchRef, props.clubs);
    if (isHome(match)) return away?.value || null;
    if (isAway(match)) return home?.value || null;
    return null;
  }

  function didWin(match: Fixture): boolean {
    if (!isResult(match)) return false;
    const homeScore = Number(match.homeScore);
    const awayScore = Number(match.awayScore);
    return isHome(match)
      ? homeScore > awayScore
      : isAway(match)
        ? awayScore > homeScore
        : false;
  }

  function scoreDisplay(match: Fixture): string {
    if (!isResult(match)) return '';
    return `${match.homeScore} - ${match.awayScore}`;
  }

  function goToEvent(match: Fixture) {
    router.push({ path: `/event/${match.fixtureDate}` });
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
    background-color: var(--bs-secondary);
    color: white;

    /* center content */
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .capsule-shape {
    border-radius: 16px;
    padding-top: 16px;
    padding-bottom: 16px;
    height: auto;
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
