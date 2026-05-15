<template>
  <div 
    class="flex items-center gap-4 p-4 bg-white/5 rounded-xl hover:bg-white/10 transition-all duration-300 group cursor-pointer border border-transparent hover:border-red-950/30"
    @click="handleClick"
  >
    <!-- Rank/Index -->
    <div v-if="index !== undefined" class="text-gray-500 font-medium text-sm w-4">
      {{ index + 1 }}
    </div>

    <!-- Thumbnail -->
    <div class="w-14 h-14 rounded-lg overflow-hidden bg-gradient-to-br from-red-950/20 to-black/50 flex-shrink-0 relative">
      <img
        :src="thumbnail"
        :alt="title"
        class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
      />
      <div class="absolute inset-0 bg-black/0 group-hover:bg-black/40 transition-colors flex items-center justify-center">
        <LucideIcon name="Play" class="w-5 h-5 text-white opacity-0 group-hover:opacity-100 transition-opacity" fill="white" />
      </div>
    </div>

    <!-- Info -->
    <div class="flex-1 min-w-0">
      <h4 class="text-white text-sm truncate group-hover:text-[#ff0040] transition-colors font-medium mb-1">
        {{ title }}
      </h4>
      <p class="text-gray-400 text-[11px] truncate">{{ artist }}</p>
    </div>

    <!-- Extra Info -->
    <div class="flex items-center gap-4">
      <span class="text-gray-500 text-[11px] font-medium hidden sm:block">{{ duration }}</span>
      <button 
        class="w-8 h-8 rounded-full flex items-center justify-center text-gray-500 hover:text-red-500 hover:bg-red-500/10 transition-all"
        @click.stop="toggleLike"
      >
        <LucideIcon name="Heart" :size="16" />
      </button>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'
import LucideIcon from '../LucideIcon.vue'

const props = defineProps({
  index: Number,
  thumbnail: String,
  title: String,
  artist: String,
  duration: String
})

function handleClick() {
  // Logic to play song
}

function toggleLike() {
  // Logic to like song
}
</script>
