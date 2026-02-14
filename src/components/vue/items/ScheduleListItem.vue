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
        <template
          v-for="(fixtures, leagueId) in fixturesByLeague"
          :key="leagueId"
        >
          <a
            v-for="fixture in fixtures"
            :key="fixture.fixtureId"
            :href="`/${union.slug}/fixture/${fixture.fixtureId}`"
            class="list-group-item-action text-decoration-none"
            role="button"
          >
            <div class="d-flex justify-content-between align-items-center">
              <!-- Opponent -->
              <div
                class="d-flex align-items-center gap-2 flex-grow-1 min-width-0"
              >
                <span class="fw-normal text-muted flex-shrink-0">
                  {{ isHome(fixture) ? 'vs' : 'at' }}
                </span>

                <img
                  v-if="getOpponent(fixture)?.logo"
                  :src="getOpponent(fixture)?.logo"
                  :alt="getOpponent(fixture)?.name || ''"
                  width="24"
                  height="24"
                  class="logo-img flex-shrink-0"
                />

                <div class="flex-grow-1 min-width-0">
                  <span class="text-body-emphasis fw-normal">
                    {{ getOpponent(fixture)?.name || 'Unknown' }}
                  </span>
                  <small class="text-body-secondary d-block">
                    {{ getLeagueName(leagueId, leagues) || 'Unknown league' }}
                  </small>
                </div>
              </div>

              <!-- Right side -->
              <div
                class="d-flex align-items-center gap-1 flex-shrink-0 text-muted"
              >
                <template v-if="isResult(fixture)">
                  <span
                    class="badge text-center"
                    :class="{
                      'text-bg-success': didWin(fixture),
                      'text-bg-danger': !didWin(fixture),
                    }"
                  >
                    {{ didWin(fixture) ? 'W' : 'L' }}
                  </span>
                </template>
                <template v-else>
                  <span class="text-body-secondary">
                    {{ timeLabel(fixture.fixtureDate) }}
                  </span>
                </template>
              </div>
            </div>
          </a>
        </template>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { computed, toRef } from 'vue';
  import { format } from 'date-fns';
  import type { Fixture } from '@/utils/types';
  import { useMatchClubs, getLeagueName } from '@/composables/utils';
  import { useAppData } from '@/composables/useAppData';

  const { union, clubs, leagues } = useAppData();

  const props = defineProps<{
    clubId: string;
    fixturesByLeague: Record<string, Fixture[]>;
  }>();

  const fixturesByLeague = computed(() => props.fixturesByLeague ?? {});

  /* --- Date helpers --- */

  const firstMatchDate = computed(() => {
    const allFixtures = Object.values(fixturesByLeague.value).flat();
    if (!allFixtures.length) return new Date();
    return new Date(allFixtures[0].fixtureDate * 1000);
  });

  const dayName = computed(() => format(firstMatchDate.value, 'EEE'));
  const dayNumber = computed(() => format(firstMatchDate.value, 'd'));

  function timeLabel(unixSeconds: number): string {
    return format(new Date(unixSeconds * 1000), 'HH:mm');
  }

  /* --- Match helpers --- */

  function isResult(fixture: Fixture) {
    return fixture.fixtureStatus === 'result';
  }

  function isHome(fixture: Fixture) {
    return fixture.home.club_id === props.clubId;
  }

  function isAway(fixture: Fixture) {
    return fixture.away.club_id === props.clubId;
  }

  function getOpponent(fixture: Fixture) {
    const fixtureRef = toRef({ value: fixture }, 'value');
    const { home, away } = useMatchClubs(fixtureRef, clubs);
    if (isHome(fixture)) return away?.value ?? null;
    if (isAway(fixture)) return home?.value ?? null;
    return null;
  }

  function didWin(fixture: Fixture): boolean {
    if (!isResult(fixture)) return false;
    const home = fixture.home.result;
    const away = fixture.away.result;
    return isHome(fixture) ? home === 'win' : away === 'win';
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
