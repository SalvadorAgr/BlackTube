<template>
  <div class="group relative bg-black/30 backdrop-blur-2xl rounded-xl p-4 hover:bg-black/40 transition-all duration-300 cursor-pointer border-none shadow-lg">
    <!-- Album Art -->
    <div class="relative aspect-square rounded-lg overflow-hidden mb-4 bg-gradient-to-br from-red-950/20 to-black/50">
      <div class="w-full h-full flex items-center justify-center text-red-900/20">
        <LucideIcon
          name="Music"
          :size="48"
        />
      </div>

      <!-- Play Button Overlay -->
      <div class="absolute inset-0 bg-black/40 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-all duration-300 translate-y-4 group-hover:translate-y-0">
        <button class="w-12 h-12 rounded-full bg-[#ff0040] text-white flex items-center justify-center shadow-lg hover:scale-110 transition-transform active:scale-95">
          <LucideIcon
            name="Play"
            :size="24"
            fill="currentColor"
          />
        </button>
      </div>

      <!-- Type Badge -->
      <div class="absolute top-2 right-2 px-2 py-1 bg-black/60 backdrop-blur-md rounded text-[10px] font-bold text-white uppercase tracking-wider">
        {{ type === 'album' ? t('Album') : type === 'playlist' ? t('Playlist.Playlist') : t('Song') }}
      </div>
    </div>

    <!-- Info -->
    <div class="space-y-1">
      <h3 class="text-white font-medium text-sm truncate group-hover:glow-text-red transition-all duration-300">
        {{ title }}
      </h3>
      <p class="text-gray-500 text-xs truncate group-hover:text-gray-300 transition-colors">
        {{ artist }}
      </p>
    </div>
  </div>
</template>

<script setup>
import { useI18n } from '../../composables/use-i18n-polyfill'
import LucideIcon from '../LucideIcon.vue'

const { t } = useI18n()

defineProps({
  title: {
    type: String,
    default: ''
  },
  artist: {
    type: String,
    default: ''
  },
  type: {
    type: String,
    default: 'album'
  }
})
</script>
