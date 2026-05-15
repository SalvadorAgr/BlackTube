<template>
  <div class="space-y-12">
    <!-- Recently Played -->
    <section>
      <h2 class="text-2xl mb-6 bg-gradient-to-r from-white to-red-300 bg-clip-text text-transparent font-semibold">
        Reproducido recientemente
      </h2>
      <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-6 gap-4">
        <MusicCard
          v-for="item in recentlyPlayed"
          :key="item.id"
          :title="item.title"
          :artist="item.artist"
        />
      </div>
    </section>

    <!-- Trending Now -->
    <section>
      <h2 class="text-2xl mb-6 bg-gradient-to-r from-white to-red-300 bg-clip-text text-transparent font-semibold">
        Tendencias ahora
      </h2>
      <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-6 gap-4">
        <MusicCard
          v-for="item in trendingNow"
          :key="item.id"
          :title="item.title"
          :artist="item.artist"
        />
      </div>
    </section>

    <!-- Recommended -->
    <section>
      <h2 class="text-2xl mb-6 bg-gradient-to-r from-white to-red-300 bg-clip-text text-transparent font-semibold">
        Recomendado para ti
      </h2>
      <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-6 gap-4">
        <MusicCard
          v-for="item in recommended"
          :key="item.id"
          :title="item.title"
          :artist="item.artist"
        />
      </div>
    </section>
  </div>
</template>

<script setup>
import MusicCard from '../../components/premium/MusicCard.vue'

const recentlyPlayed = [
  { id: 1, title: 'Midnight Echoes', artist: 'Luna Shadow' },
  { id: 2, title: 'Neon Nights', artist: 'DJ Carmesí' },
  { id: 3, title: 'Synthwave Dreams', artist: 'Retro Future' },
  { id: 4, title: 'Vinyl Memories', artist: 'Studio Sessions' },
  { id: 5, title: 'The Analog Collective', artist: 'The Producers' },
  { id: 6, title: 'Stadium Anthems', artist: 'Live Energy' }
]

const trendingNow = [
  { id: 7, title: 'Electric Pulse', artist: 'Digital Waves' },
  { id: 8, title: 'Headphone Sessions', artist: 'Abstract Waves' },
  { id: 9, title: 'Lo-Fi Beats', artist: 'Sound Sculptor' },
  { id: 10, title: 'Turntable Tales', artist: 'Vinyl Classics' },
  { id: 11, title: 'Midnight Drive', artist: 'Neon Shadows' },
  { id: 12, title: 'Crimson Horizon', artist: 'Electronic Dreams' }
]

const recommended = [
  { id: 13, title: 'Future Bass', artist: 'Bass Frequencies' },
  { id: 14, title: 'Deep Sound', artist: 'Atmospheric Vibes' },
  { id: 15, title: 'Ambient Collective', artist: 'Dark Pulse' },
  { id: 16, title: 'Shadow Beats', artist: 'Wavelength' },
  { id: 17, title: 'Retro Collection', artist: 'Concert Series' },
  { id: 18, title: 'Frequency Modulation', artist: 'Red Alert' }
]
</script>

<style scoped>
/* Scoped styles kept minimal as we use Tailwind and global glass utilities */
</style>

