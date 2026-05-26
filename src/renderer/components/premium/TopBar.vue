<template>
  <header
    class="topbar-glass fixed top-0 left-0 right-0 h-16 z-40 px-8 flex items-center justify-between transition-all duration-300"
  >
    <nav class="header-nav">
      <RouterLink
        v-for="item in navItems"
        :key="item.route"
        :to="item.route"
        :aria-label="item.label"
        :class="[
          'header-nav-link',
          isActive(item.route) ? 'is-active' : ''
        ]"
      >
        <LucideIcon
          :name="item.icon"
          :size="21"
        />
      </RouterLink>
    </nav>

    <!-- Search Bar -->
    <div class="flex-1 max-w-xl mx-8">
      <div class="relative group">
        <LucideIcon
          name="Search"
          class="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-500 group-focus-within:text-red-400 transition-colors"
        />
        <input
          v-model="searchQuery"
          type="text"
          :aria-label="searchPlaceholder"
          :placeholder="searchPlaceholder"
          class="w-full bg-black/30 backdrop-blur-2xl border-none rounded-full py-2.5 pl-12 pr-6 text-sm text-white placeholder:text-gray-500 focus:outline-none focus:bg-black/40 transition-all duration-300 focus:shadow-[0_0_20px_rgba(220,20,60,0.2)]"
          @keyup.enter="handleSearch"
        >
      </div>
    </div>

    <!-- Profile -->
    <button
      class="ml-6 w-9 h-9 bg-gradient-to-br from-red-600 to-red-900 rounded-full flex items-center justify-center hover:shadow-[0_0_20px_rgba(220,20,60,0.6)] transition-all duration-300 hover:scale-105"
      @click="goToSettings"
    >
      <LucideIcon
        name="User"
        class="w-5 h-5 text-white"
      />
    </button>
  </header>
</template>

<script setup>
import { computed, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import LucideIcon from '../LucideIcon.vue'

const route = useRoute()
const router = useRouter()
const searchQuery = ref('')
const searchPlaceholder = 'Search for songs, artists, playlists...'

const navItems = computed(() => [
  { icon: 'Home', label: 'Inicio', route: '/' },
  { icon: 'Search', label: 'Buscar', route: '/search/trending' },
  { icon: 'Compass', label: 'Explorar', route: '/trending' },
  { icon: 'Library', label: 'Tu biblioteca', route: '/subscriptions' },
  { icon: 'Heart', label: 'Favoritos', route: '/history' },
  { icon: 'ListMusic', label: 'Playlists', route: '/userplaylists' }
])

function isActive(path) {
  if (path === '/') return route.path === '/'
  return route.path.startsWith(path)
}

function handleSearch() {
  if (searchQuery.value.trim()) {
    router.push(`/search/${encodeURIComponent(searchQuery.value.trim())}`)
  }
}

function goToSettings() {
  router.push('/settings')
}
</script>

<style scoped>
.topbar-glass {
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  box-shadow: none;
  border: none;
}

.header-nav {
  display: flex;
  gap: 8px;
  align-items: center;
  flex: 0 0 auto;
}

.header-nav-link {
  display: flex;
  align-items: center;
  justify-content: center;
  inline-size: 40px;
  block-size: 40px;
  color: rgb(156 163 175);
  border-radius: 12px;
  transition:
    color 180ms ease,
    background-color 180ms ease,
    filter 180ms ease;
}

.header-nav-link:hover,
.header-nav-link.is-active {
  color: #ff0040;
  background-color: rgba(0, 0, 0, 0.4);
  filter: drop-shadow(0 0 8px rgb(255 0 64 / 60%));
}
</style>
