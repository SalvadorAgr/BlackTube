<template>
  <header 
    :class="[
      'fixed top-0 right-0 h-16 glass z-40 px-8 flex items-center justify-between transition-all duration-300',
      isCollapsed ? 'left-20' : 'left-64'
    ]"
  >
    <!-- Search Bar -->
    <div class="flex-1 max-w-xl mx-auto">
      <div class="relative group">
        <LucideIcon 
          name="Search" 
          class="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-500 group-focus-within:text-red-400 transition-colors" 
        />
        <input
          type="text"
          placeholder="Buscar canciones, artistas, listas..."
          class="w-full bg-white/5 border border-white/10 rounded-full py-2 pl-12 pr-4 text-sm focus:outline-none focus:ring-2 focus:ring-red-500/50 focus:border-red-500/50 transition-all placeholder:text-gray-600"
        />
      </div>
    </div>

    <!-- User Profile -->
    <div class="flex items-center gap-4">
      <button class="p-2 hover:bg-white/5 rounded-full text-gray-400 hover:text-white transition-colors relative">
        <LucideIcon name="Bell" :size="20" />
        <span class="absolute top-2 right-2 w-2 h-2 bg-red-600 rounded-full border-2 border-black" />
      </button>
      <div class="flex items-center gap-3 pl-4 border-l border-white/10 cursor-pointer group">
        <div class="text-right hidden sm:block">
          <p class="text-sm font-medium text-white group-hover:text-red-400 transition-colors">Usuario Premium</p>
          <p class="text-xs text-gray-500">Plan Individual</p>
        </div>
        <div class="w-10 h-10 rounded-full bg-gradient-to-tr from-red-600 to-purple-600 p-[2px]">
          <div class="w-full h-full rounded-full bg-black flex items-center justify-center overflow-hidden">
            <LucideIcon name="User" class="text-white" :size="20" />
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
import LucideIcon from '../LucideIcon.vue'

defineProps({
  isCollapsed: Boolean
})
</script>
