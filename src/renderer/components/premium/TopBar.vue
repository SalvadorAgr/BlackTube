<template>
  <header 
    :class="[
      'fixed top-0 right-0 h-16 bg-black/40 backdrop-blur-md border-b border-red-950/30 z-40 px-8 flex items-center justify-between transition-all duration-300',
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
          v-model="searchQuery"
          @keyup.enter="handleSearch"
          placeholder="Search for songs, artists, playlists..."
          class="w-full bg-white/5 border border-red-950/30 rounded-full py-2.5 pl-12 pr-6 text-sm text-white placeholder:text-gray-500 focus:outline-none focus:border-red-600/50 focus:bg-white/10 transition-all duration-300 focus:shadow-[0_0_20px_rgba(220,20,60,0.2)]"
        />
      </div>
    </div>

    <!-- Profile -->
    <button 
      @click="goToSettings"
      class="ml-6 w-9 h-9 bg-gradient-to-br from-red-600 to-red-900 rounded-full flex items-center justify-center hover:shadow-[0_0_20px_rgba(220,20,60,0.6)] transition-all duration-300 hover:scale-105"
    >
      <LucideIcon name="User" class="w-5 h-5 text-white" />
    </button>
  </header>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import LucideIcon from '../LucideIcon.vue'
import store from '../../store/index'

const router = useRouter()
const searchQuery = ref('')

const isCollapsed = computed(() => !store.getters.getIsSideNavOpen)

function handleSearch() {
  if (searchQuery.value.trim()) {
    router.push(`/search/${encodeURIComponent(searchQuery.value.trim())}`)
  }
}

function goToSettings() {
  router.push('/settings')
}
</script>
