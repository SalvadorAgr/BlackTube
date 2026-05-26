<template>
  <aside
    :class="[
      'fixed left-0 top-0 h-screen bg-black/30 backdrop-blur-2xl flex flex-col transition-all duration-300 z-50',
      isCollapsed ? 'w-20' : 'w-64'
    ]"
  >
    <!-- Logo -->
    <div class="px-6 py-8 flex items-center justify-between">
      <div
        v-if="!isCollapsed"
        class="flex items-center gap-2 overflow-hidden"
      >
        <div class="w-10 h-10 bg-gradient-to-br from-red-600 to-red-900 rounded-lg flex items-center justify-center shadow-[0_0_20px_rgba(220,20,60,0.5)] flex-shrink-0">
          <LucideIcon
            name="ListMusic"
            class="w-6 h-6 text-white"
          />
        </div>
        <span class="text-xl font-semibold text-white truncate">{{ t('App Name') }}</span>
      </div>
      <button
        class="p-2 hover:bg-black/40 rounded-lg text-gray-400 hover:text-white transition-all duration-200 cursor-pointer"
        @click="toggleSideNav"
      >
        <LucideIcon
          :name="isCollapsed ? 'Menu' : 'ChevronLeft'"
          :size="20"
        />
      </button>
    </div>

    <!-- Navigation -->
    <nav class="flex-1 overflow-y-auto">
      <div
        v-for="item in navItems"
        :key="item.route"
      >
        <RouterLink
          v-if="!item.hidden"
          :to="item.route"
          :class="[
            'flex items-center gap-4 px-6 py-3 w-full transition-all duration-300 hover:bg-black/40 relative group cursor-pointer no-underline',
            isActive(item.route) ? 'text-[#ff0040] bg-black/40 shadow-inner' : 'text-gray-400 hover:text-white'
          ]"
        >
          <span :class="['transition-all duration-300 flex-shrink-0', isActive(item.route) ? 'drop-shadow-[0_0_8px_rgba(255,0,64,0.6)]' : '']">
            <LucideIcon
              :name="item.icon"
              :size="22"
            />
          </span>
          <span
            v-if="!isCollapsed"
            class="text-sm truncate"
          >{{ item.label }}</span>

          <div
            v-if="isCollapsed"
            class="absolute left-full ml-2 px-2 py-1 bg-red-950 text-white text-xs rounded opacity-0 group-hover:opacity-100 pointer-events-none transition-opacity whitespace-nowrap z-50"
          >
            {{ item.label }}
          </div>
        </RouterLink>
        <div
          v-if="item.separator"
          :class="['h-px bg-gradient-to-r from-transparent via-red-950/50 to-transparent my-4', isCollapsed ? 'mx-4' : 'mx-6']"
        />
      </div>
    </nav>

    <!-- Bottom Gradient Fade -->
    <div class="h-20 bg-gradient-to-t from-black/80 to-transparent pointer-events-none" />
  </aside>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useI18n } from '../../composables/use-i18n-polyfill'
import LucideIcon from '../LucideIcon.vue'
import store from '../../store/index'

const { t } = useI18n()

const route = useRoute()

const isCollapsed = computed(() => !store.getters.getIsSideNavOpen)

function toggleSideNav() {
  store.commit('toggleSideNav')
}

function isActive(path) {
  if (path === '/') return route.path === '/'
  return route.path.startsWith(path)
}

const navItems = computed(() => [
  { icon: 'Home', label: 'Inicio', route: '/' },
  { icon: 'Search', label: 'Buscar', route: '/search/trending' },
  { icon: 'Compass', label: 'Explorar', route: '/trending', separator: true },
  { icon: 'Library', label: 'Tu biblioteca', route: '/subscriptions' },
  { icon: 'Heart', label: 'Favoritos', route: '/history' },
  { icon: 'ListMusic', label: 'Playlists', route: '/userplaylists' }
])
</script>

<style scoped>
.no-underline {
  text-decoration: none;
}
</style>
