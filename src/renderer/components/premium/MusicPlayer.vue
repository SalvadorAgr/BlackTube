<template>
  <footer class="fixed bottom-0 left-0 right-0 h-24 glass-dark px-6 flex items-center gap-6 z-50">
    <!-- Song Info -->
    <div class="flex items-center gap-4 w-80">
      <div class="w-16 h-16 rounded-lg overflow-hidden bg-gradient-to-br from-red-950/30 to-black/50 flex-shrink-0">
        <div class="w-full h-full flex items-center justify-center text-red-900/50">
          <LucideIcon name="Music" :size="32" />
        </div>
      </div>
      <div class="flex-1 min-w-0">
        <h4 class="text-white text-sm truncate font-medium">Ecos de medianoche</h4>
        <p class="text-gray-400 text-xs truncate">Sombra de Luna</p>
      </div>
      <button 
        @click="isLiked = !isLiked"
        :class="['transition-colors', isLiked ? 'text-red-500' : 'text-gray-500 hover:text-white']"
      >
        <LucideIcon name="Heart" :size="20" :fill="isLiked ? 'currentColor' : 'none'" />
      </button>
    </div>

    <!-- Controls -->
    <div class="flex-1 flex flex-col items-center gap-2 max-w-2xl">
      <div class="flex items-center gap-6">
        <button class="text-gray-500 hover:text-white transition-colors"><LucideIcon name="Shuffle" :size="18" /></button>
        <button class="text-gray-300 hover:text-white transition-colors"><LucideIcon name="SkipBack" :size="22" /></button>
        <button class="w-10 h-10 rounded-full bg-white text-black flex items-center justify-center hover:scale-105 transition-transform">
          <LucideIcon name="Play" :size="20" fill="currentColor" />
        </button>
        <button class="text-gray-300 hover:text-white transition-colors"><LucideIcon name="SkipForward" :size="22" /></button>
        <button class="text-gray-500 hover:text-white transition-colors"><LucideIcon name="Repeat" :size="18" /></button>
      </div>
      <div class="w-full flex items-center gap-3">
        <span class="text-[10px] text-gray-500 w-10 text-right">1:24</span>
        <div class="flex-1 h-1 bg-white/10 rounded-full relative group cursor-pointer">
          <div class="absolute inset-0 bg-red-600 rounded-full w-[35%] group-hover:bg-red-500 transition-colors" />
          <div class="absolute top-1/2 -translate-y-1/2 left-[35%] w-3 h-3 bg-white rounded-full shadow-lg opacity-0 group-hover:opacity-100 transition-opacity" />
        </div>
        <span class="text-[10px] text-gray-500 w-10">3:45</span>
      </div>
    </div>

    <!-- Volume & Extras -->
    <div class="flex items-center justify-end gap-4 w-80">
      <button class="text-gray-500 hover:text-white transition-colors"><LucideIcon name="Mic2" :size="18" /></button>
      <button class="text-gray-500 hover:text-white transition-colors"><LucideIcon name="ListMusic" :size="18" /></button>
      <button class="text-gray-500 hover:text-white transition-colors"><LucideIcon name="Laptop2" :size="18" /></button>
      <div class="flex items-center gap-2 w-32">
        <LucideIcon name="Volume2" :size="18" class="text-gray-500" />
        <div class="flex-1 h-1 bg-white/10 rounded-full relative">
          <div class="absolute inset-0 bg-white/60 rounded-full w-[70%]" />
        </div>
      </div>
      <button class="text-gray-500 hover:text-white transition-colors"><LucideIcon name="Maximize2" :size="18" /></button>
    </div>
  </footer>
</template>

<script setup>
import { ref } from 'vue'
import LucideIcon from '../LucideIcon.vue'

const isLiked = ref(false)
</script>
