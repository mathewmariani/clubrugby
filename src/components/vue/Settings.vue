<template>
  <div class="mt-3">
    <div v-if="!Object.keys(leagues).length">No leagues available.</div>
    <ul v-else class="list-group">
      <li class="list-group-item">
        <strong>Choose leagues to display</strong>
      </li>
      <li
        v-for="(league, index) in leagues"
        :key="index"
        class="list-group-item"
      >
        <div class="form-check">
          <input
            @change="saveSettings"
            :value="league.id"
            v-model="selectedLeagues"
            class="form-check-input"
            type="checkbox"
            :id="`league-${index}`"
          />
          <label class="form-check-label" :for="`league-${index}`">
            {{ league.name }}
          </label>
        </div>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
  import { useSavedLeagues } from '../../composables/useSavedLeagues';
  import { type League } from '../../utils/types';
  const props = defineProps<{
    leagues: Record<string, League>;
  }>();

  const emit = defineEmits(['update-leagues']);
  const { savedLeagues: selectedLeagues, setSavedLeagues } = useSavedLeagues();

  // Emit when user manually saves (if needed)
  const saveSettings = () => {
    emit('update-leagues', selectedLeagues.value);
    console.log('Saved:', JSON.stringify(selectedLeagues.value));
  };
</script>
