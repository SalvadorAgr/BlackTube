<template>
  <footer
    class="player-glass fixed bottom-0 left-0 right-0 px-6 flex items-center gap-6 z-50"
    style="color: rgba(0, 0, 0, 0); flex-wrap: nowrap; overflow: hidden; box-shadow: rgba(0, 0, 0, 0.35) 0px -18px 48px 0px; height: 94px;"
  >
    <!-- Song Info -->
    <div class="flex items-center gap-4 w-80">
      <div class="w-16 h-16 rounded-lg overflow-hidden bg-gradient-to-br from-red-950/20 to-black/50 flex-shrink-0">
        <img
          v-if="currentTrack?.thumbnail"
          :src="currentTrack.thumbnail"
          :alt="currentTrack?.title || ''"
          class="w-full h-full object-cover"
        >
        <div
          v-else
          class="w-full h-full flex items-center justify-center text-red-900/50"
        >
          <LucideIcon
            name="Music"
            :size="32"
          />
        </div>
      </div>
      <div class="flex-1 min-w-0">
        <h4 class="text-white text-sm truncate">
          {{ currentTrack?.title || 'No hay canción' }}
        </h4>
        <p class="text-gray-400 text-xs truncate">
          {{ currentTrack?.author || 'Selecciona una pista' }}
        </p>
      </div>
      <button
        :class="['transition-all duration-300', isLiked ? 'text-[#ff0040] drop-shadow-[0_0_8px_rgba(255,0,64,0.6)]' : 'text-gray-400 hover:text-white']"
        @click="toggleLike"
      >
        <LucideIcon
          name="Heart"
          :size="20"
          :class="{ 'fill-current': isLiked }"
        />
      </button>
    </div>

    <!-- Player Controls -->
    <div class="flex-1 flex flex-col items-center gap-2">
      <!-- Buttons -->
      <div class="flex items-center gap-4">
        <button class="text-gray-400 hover:text-white transition-colors">
          <LucideIcon
            name="Shuffle"
            :size="18"
          />
        </button>
        <button
          class="text-gray-400 hover:text-white transition-all duration-300 hover:scale-110"
          @click="prevTrack"
        >
          <LucideIcon
            name="SkipBack"
            :size="20"
          />
        </button>
        <button
          class="w-10 h-10 bg-white rounded-full flex items-center justify-center hover:scale-105 transition-all duration-300 shadow-[0_0_20px_rgba(255,255,255,0.3)] hover:shadow-[0_0_30px_rgba(255,0,64,0.5)]"
          @click="togglePlay"
        >
          <LucideIcon
            :name="isPlaying ? 'Pause' : 'Play'"
            class="w-5 h-5 text-black fill-black ml-0.5"
          />
        </button>
        <button
          class="text-gray-400 hover:text-white transition-all duration-300 hover:scale-110"
          @click="nextTrack"
        >
          <LucideIcon
            name="SkipForward"
            :size="20"
          />
        </button>
        <button class="text-gray-400 hover:text-white transition-colors">
          <LucideIcon
            name="Repeat"
            :size="18"
          />
        </button>
      </div>

      <!-- Progress Bar -->
      <div class="flex items-center gap-3 w-full max-w-2xl">
        <span class="text-xs text-gray-400 w-10 text-right">{{ formatTime(currentTime) }}</span>
        <div class="flex-1 group relative flex items-center">
          <input
            v-model="currentTime"
            :aria-label="t('Progress')"
            type="range"
            min="0"
            :max="duration"
            class="w-full h-1 bg-red-950/30 rounded-full appearance-none cursor-pointer [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:w-3 [&::-webkit-slider-thumb]:h-3 [&::-webkit-slider-thumb]:rounded-full [&::-webkit-slider-thumb]:bg-white [&::-webkit-slider-thumb]:opacity-0 group-hover:[&::-webkit-slider-thumb]:opacity-100 [&::-webkit-slider-thumb]:transition-opacity [&::-webkit-slider-thumb]:shadow-[0_0_10px_rgba(255,0,64,0.5)] relative z-10"
            :style="progressStyle"
            @input="seek"
          >
        </div>
        <span class="text-xs text-gray-400 w-10">{{ formatTime(duration) }}</span>
      </div>
    </div>

    <!-- Volume Control -->
    <div class="flex items-center gap-3 w-40">
      <LucideIcon
        name="Volume2"
        class="w-5 h-5 text-gray-400"
      />
      <div class="flex-1 group flex items-center">
        <input
          v-model="volume"
          :aria-label="t('Volume')"
          type="range"
          min="0"
          max="100"
          class="w-full h-1 bg-red-950/30 rounded-full appearance-none cursor-pointer [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:w-3 [&::-webkit-slider-thumb]:h-3 [&::-webkit-slider-thumb]:rounded-full [&::-webkit-slider-thumb]:bg-white [&::-webkit-slider-thumb]:opacity-0 group-hover:[&::-webkit-slider-thumb]:opacity-100 [&::-webkit-slider-thumb]:transition-opacity [&::-webkit-slider-thumb]:shadow-[0_0_10px_rgba(255,0,64,0.5)]"
          :style="volumeStyle"
          @input="updateVolume"
        >
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useI18n } from '../../composables/use-i18n-polyfill'
import LucideIcon from '../LucideIcon.vue'
import store from '../../store/index'

const { t } = useI18n()

const isLiked = ref(false)
const volume = ref(70)
const currentTime = ref(0)
const duration = ref(300) // Mock duration

const isPlaying = computed(() => store.getters.getIsPlaying)
const currentTrack = computed(() => store.getters.getCurrentTrack)

const progressStyle = computed(() => {
  const percent = (currentTime.value / duration.value) * 100
  return {
    background: `linear-gradient(to right, #ff0040 0%, #ff0040 ${percent}%, rgba(74, 0, 0, 0.3) ${percent}%, rgba(74, 0, 0, 0.3) 100%)`
  }
})

const volumeStyle = computed(() => {
  return {
    background: `linear-gradient(to right, #ff0040 0%, #ff0040 ${volume.value}%, rgba(74, 0, 0, 0.3) ${volume.value}%, rgba(74, 0, 0, 0.3) 100%)`
  }
})

function formatTime(seconds) {
  const m = Math.floor(seconds / 60)
  const s = Math.floor(seconds % 60)
  return `${m}:${s.toString().padStart(2, '0')}`
}

function togglePlay() {
  store.dispatch('togglePlay')
}

function nextTrack() {
  store.dispatch('skipToNext')
}

function prevTrack() {
  store.dispatch('skipToPrevious')
}

function seek() {
  // Logic to seek in player
}

function updateVolume() {
  store.dispatch('updateVolume', volume.value)
}

function toggleLike() {
  isLiked.value = !isLiked.value
}
</script>

<style scoped>
.player-glass {
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  box-shadow: 0 -18px 48px rgb(0 0 0 / 36%);
  border: none;
  transform: translate3d(0, 0, 100px);
}
</style>
