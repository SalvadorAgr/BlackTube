<template>
  <div
    class="group relative bg-black/30 backdrop-blur-2xl rounded-xl p-4 hover:bg-black/40 transition-all duration-300 cursor-pointer border-none shadow-lg"
    role="button"
    tabindex="0"
    @click="handleClick"
    @keydown.enter="handleClick"
    @keydown.space.prevent="handleClick"
  >
    <!-- Album Art -->
    <div class="relative aspect-square rounded-lg overflow-hidden mb-4 bg-gradient-to-br from-red-950/20 to-black/50">
      <img
        :src="thumbnail"
        :alt="title"
        class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
      >

      <!-- Play Button Overlay -->
      <div class="absolute inset-0 bg-black/0 group-hover:bg-black/40 transition-all duration-300 flex items-center justify-center">
        <button
          class="w-12 h-12 bg-[#ff0040] rounded-full flex items-center justify-center opacity-0 group-hover:opacity-100 transform translate-y-2 group-hover:translate-y-0 transition-all duration-300 shadow-[0_0_20px_rgba(255,0,64,0.6)] hover:scale-110 cursor-pointer"
        >
          <LucideIcon
            name="Play"
            class="w-6 h-6 text-white fill-white ml-0.5"
          />
        </button>
      </div>
    </div>

    <!-- Info -->
    <div class="min-w-0">
      <h3 class="text-white text-sm mb-1 truncate group-hover:text-[#ff0040] transition-colors font-medium">
        {{ title }}
      </h3>
      <p class="text-gray-400 text-[11px] truncate">
        {{ artist }}
      </p>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'
import LucideIcon from '../LucideIcon.vue'

defineProps({
  thumbnail: {
    type: String,
    default: ''
  },
  title: {
    type: String,
    default: ''
  },
  artist: {
    type: String,
    default: ''
  }
})

function handleClick() {
  // Logic to open album/playlist
}
</script>
