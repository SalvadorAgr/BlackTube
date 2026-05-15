<template>
  <aside 
    :class="[
      'fixed left-0 top-0 h-screen glass-dark flex flex-col transition-all duration-300 z-50',
      isCollapsed ? 'w-20' : 'w-64'
    ]"
  >
    <!-- Logo & Toggle -->
    <div :class="['flex items-center px-6 py-8', isCollapsed ? 'justify-center' : 'justify-between']">
      <div v-if="!isCollapsed" class="flex items-center gap-2 overflow-hidden">
        <div class="w-10 h-10 bg-gradient-to-br from-red-600 to-red-900 rounded-lg flex items-center justify-center shadow-[0_0_20px_rgba(220,20,60,0.5)] flex-shrink-0">
          <LucideIcon name="ListMusic" class="w-6 h-6 text-white" />
        </div>
        <span class="text-xl font-semibold text-white truncate">BlackTube</span>
      </div>
      <button 
        @click="$emit('toggle-collapse')"
        class="p-2 hover:bg-white/5 rounded-lg text-gray-400 hover:text-white transition-colors"
      >
        <LucideIcon :name="isCollapsed ? 'Menu' : 'ChevronLeft'" :size="20" />
      </button>
    </div>

    <!-- Navigation -->
    <nav class="flex-1 overflow-y-auto">
      <div v-for="item in navItems" :key="item.label">
        <button
          :class="[
            'flex items-center gap-4 px-6 py-3 w-full transition-all duration-300 hover:bg-white/5 relative group',
            item.active ? 'text-[#ff0040] bg-white/5' : 'text-gray-400 hover:text-white'
          ]"
        >
          <span :class="['transition-all duration-300', item.active ? 'drop-shadow-[0_0_8px_rgba(255,0,64,0.6)]' : '']">
            <LucideIcon :name="item.icon" :size="22" />
          </span>
          <span v-if="!isCollapsed" class="text-sm truncate transition-opacity duration-300">{{ item.label }}</span>
          
          <div v-if="isCollapsed" class="absolute left-full ml-2 px-2 py-1 bg-red-950 text-white text-xs rounded opacity-0 group-hover:opacity-100 pointer-events-none transition-opacity whitespace-nowrap z-50">
            {{ item.label }}
          </div>
        </button>
        <div v-if="item.separator" :class="['h-px bg-gradient-to-r from-transparent via-red-950/50 to-transparent my-4', isCollapsed ? 'mx-4' : 'mx-6']" />
      </div>
    </nav>

    <!-- Bottom Gradient Fade -->
    <div class="h-20 bg-gradient-to-t from-black/80 to-transparent pointer-events-none" />
  </aside>
</template>

<script setup>
import LucideIcon from '../LucideIcon.vue'

defineProps({
  isCollapsed: Boolean
})

defineEmits(['toggle-collapse'])

const navItems = [
  { icon: 'Home', label: 'Inicio', active: true },
  { icon: 'Search', label: 'Buscar' },
  { icon: 'Compass', label: 'Explorar', separator: true },
  { icon: 'Library', label: 'Tu biblioteca' },
  { icon: 'Heart', label: 'Canciones favoritas' },
  { icon: 'ListMusic', label: 'Listas de reproducción' }
]
</script>
