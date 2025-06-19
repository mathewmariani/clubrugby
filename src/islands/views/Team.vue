<template>
  <div class="container py-3" v-if="club">
    <div class="mb-4 text-center">
      <img
        v-if="club.logo_url"
        :src="club.logo_url"
        :alt="club.name"
        width="96"
        height="96"
        style="object-fit: contain"
        class="mb-2"
      />
      <h4>{{ club.name }}</h4>
    </div>

    <template v-if="teamFixtures.length">
      <strong class="list-group-item">Upcoming Fixtures</strong>
      <div class="list-group list-group-flush mb-4">
        <FixtureListItem
          v-for="match in teamFixtures"
          :key="`${match.date}-${match.home_id}-${match.away_id}`"
          :match="match"
          :clubs="clubs"
          :leagues="leagues"
        />
      </div>
    </template>

    <template v-if="teamResults.length">
      <strong class="list-group-item">Past Results</strong>
      <div class="list-group list-group-flush mb-4">
        <ResultListItem
          v-for="match in teamResults"
          :key="`${match.date}-${match.home_id}-${match.away_id}`"
          :match="match"
          :clubs="clubs"
          :leagues="leagues"
        />
      </div>
    </template>

    <template v-if="teamStandings.length">
      <strong class="list-group-item">Standings</strong>
      <div class="list-group list-group-flush">
        <div
          v-for="standing in teamStandings"
          :key="standing.team_id"
          class="list-group-item d-flex justify-content-between"
        >
          <div>
            <strong>{{ leagues[standing.league_id]?.name }}</strong
            ><br />
            {{ club.name }}
          </div>
          <div class="text-end">
            <div>Pos: {{ standing.pos }}</div>
            <div>Pts: {{ standing.pts }}</div>
            <div>W-D-L: {{ standing.w }}-{{ standing.d }}-{{ standing.l }}</div>
          </div>
        </div>
      </div>
    </template>

    <template
      v-if="
        !teamFixtures.length && !teamResults.length && !teamStandings.length
      "
    >
      <p class="text-center text-muted mt-4">
        No data available for this team.
      </p>
    </template>
  </div>
</template>

<script setup lang="ts">
  import { computed } from 'vue';
  import { useRoute } from 'vue-router';
  import FixtureListItem from '../../components/vue/items/FixtureListItem.vue';
  import ResultListItem from '../../components/vue/items/ResultListItem.vue';
  import type {
    Club,
    League,
    Fixture,
    Result,
    Standing,
  } from '../../utils/types';

  const props = defineProps<{
    clubs: Record<string, Club>;
    leagues: Record<string, League>;
    fixtures: Record<string, Record<string, Fixture[]>>;
    results: Record<string, Record<string, Result[]>>;
    standings: Record<string, Standing[]>;
  }>();

  const route = useRoute();
  const clubId = route.params.club_id as string;
  const club = computed(() => props.clubs[clubId]);

  function flattenMatches<T extends Fixture | Result>(
    data: Record<string, Record<string, T[]>>
  ): T[] {
    return Object.values(data).flatMap((byDate) =>
      Object.values(byDate).flat()
    );
  }

  const teamFixtures = computed(() =>
    flattenMatches(props.fixtures).filter(
      (m) => m.home_id === clubId || m.away_id === clubId
    )
  );

  const teamResults = computed(() =>
    flattenMatches(props.results).filter(
      (m) => m.home_id === clubId || m.away_id === clubId
    )
  );

  const teamStandings = computed(
    () =>
      Object.entries(props.standings)
        .map(([league_id, teams]) =>
          teams.find((s) => s.team_id === clubId && (s.league_id = league_id))
        )
        .filter(Boolean) as Standing[]
  );
</script>
