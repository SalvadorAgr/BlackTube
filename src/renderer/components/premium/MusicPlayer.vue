<template>
  <footer class="fixed bottom-0 left-0 right-0 h-24 bg-gradient-to-t from-black via-black/95 to-black/90 border-t border-red-950/40 backdrop-blur-md px-6 flex items-center gap-6 z-50">
    <!-- Song Info -->
    <div class="flex items-center gap-4 w-80">
      <div class="w-16 h-16 rounded-lg overflow-hidden bg-gradient-to-br from-red-950/30 to-black/50 flex-shrink-0">
        <img
          v-if="currentTrack?.thumbnail"
          :src="currentTrack.thumbnail"
          class="w-full h-full object-cover"
        />
        <div v-else class="w-full h-full flex items-center justify-center text-red-900/50">
          <LucideIcon name="Music" :size="32" />
        </div>
      </div>
      <div class="flex-1 min-w-0">
        <h4 class="text-white text-sm truncate">{{ currentTrack?.title || 'No hay canción' }}</h4>
        <p class="text-gray-400 text-xs truncate">{{ currentTrack?.author || 'Selecciona una pista' }}</p>
      </div>
      <button
        @click="toggleLike"
        :class="['transition-all duration-300', isLiked ? 'text-[#ff0040] drop-shadow-[0_0_8px_rgba(255,0,64,0.6)]' : 'text-gray-400 hover:text-white']"
      >
        <LucideIcon name="Heart" :size="20" :class="{ 'fill-current': isLiked }" />
      </button>
    </div>

    <!-- Player Controls -->
    <div class="flex-1 flex flex-col items-center gap-2">
      <!-- Buttons -->
      <div class="flex items-center gap-4">
        <button class="text-gray-400 hover:text-white transition-colors">
          <LucideIcon name="Shuffle" :size="18" />
        </button>
        <button 
          @click="prevTrack"
          class="text-gray-400 hover:text-white transition-all duration-300 hover:scale-110"
        >
          <LucideIcon name="SkipBack" :size="20" />
        </button>
        <button 
          @click="togglePlay"
          class="w-10 h-10 bg-white rounded-full flex items-center justify-center hover:scale-105 transition-all duration-300 shadow-[0_0_20px_rgba(255,255,255,0.3)] hover:shadow-[0_0_30px_rgba(255,0,64,0.5)]"
        >
          <LucideIcon :name="isPlaying ? 'Pause' : 'Play'" class="w-5 h-5 text-black fill-black ml-0.5" />
        </button>
        <button 
          @click="nextTrack"
          class="text-gray-400 hover:text-white transition-all duration-300 hover:scale-110"
        >
          <LucideIcon name="SkipForward" :size="20" />
        </button>
        <button class="text-gray-400 hover:text-white transition-colors">
          <LucideIcon name="Repeat" :size="18" />
        </button>
      </div>

      <!-- Progress Bar -->
      <div class="flex items-center gap-3 w-full max-w-2xl">
        <span class="text-xs text-gray-400 w-10 text-right">{{ formatTime(currentTime) }}</span>
        <div class="flex-1 group relative flex items-center">
          <input
            type="range"
            min="0"
            :max="duration"
            v-model="currentTime"
            @input="seek"
            class="w-full h-1 bg-red-950/30 rounded-full appearance-none cursor-pointer [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:w-3 [&::-webkit-slider-thumb]:h-3 [&::-webkit-slider-thumb]:rounded-full [&::-webkit-slider-thumb]:bg-white [&::-webkit-slider-thumb]:opacity-0 group-hover:[&::-webkit-slider-thumb]:opacity-100 [&::-webkit-slider-thumb]:transition-opacity [&::-webkit-slider-thumb]:shadow-[0_0_10px_rgba(255,0,64,0.5)] relative z-10"
            :style="progressStyle"
          />
        </div>
        <span class="text-xs text-gray-400 w-10">{{ formatTime(duration) }}</span>
      </div>
    </div>

    <!-- Volume Control -->
    <div class="flex items-center gap-3 w-40">
      <LucideIcon name="Volume2" class="w-5 h-5 text-gray-400" />
      <div class="flex-1 group flex items-center">
        <input
          type="range"
          min="0"
          max="100"
          v-model="volume"
          @input="updateVolume"
          class="w-full h-1 bg-red-950/30 rounded-full appearance-none cursor-pointer [&::-webkit-slider-thumb]:appearance-none [&::-webkit-slider-thumb]:w-3 [&::-webkit-slider-thumb]:h-3 [&::-webkit-slider-thumb]:rounded-full [&::-webkit-slider-thumb]:bg-white [&::-webkit-slider-thumb]:opacity-0 group-hover:[&::-webkit-slider-thumb]:opacity-100 [&::-webkit-slider-thumb]:transition-opacity [&::-webkit-slider-thumb]:shadow-[0_0_10px_rgba(255,0,64,0.5)]"
          :style="volumeStyle"
        />
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
import LucideIcon from '../LucideIcon.vue'
import store from '../../store/index'

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
