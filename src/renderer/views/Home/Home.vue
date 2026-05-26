<template>
  <div class="home-page font-sans">
    <FocusRail :items="recentVideos" />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from '../../composables/use-i18n-polyfill'
import FocusRail from '../../components/premium/FocusRail.vue'
import store from '../../store'

const { t } = useI18n()

const recentVideos = computed(() => {
  const history = store.getters.getHistoryCacheSorted || []
  if (history.length > 0) {
    return history.slice(0, 10).map((video, index) => {
      let img = 'https://images.unsplash.com/photo-1614613535308-eb5fbd3d2c17?w=300&h=300&fit=crop'
      if (video.thumbnail) {
        img = video.thumbnail
      } else if (video.videoThumbnails && video.videoThumbnails.length > 0) {
        img = video.videoThumbnails[0].url
      }

      return {
        id: video.videoId || index.toString(),
        title: video.title || 'Untitled Video',
        description: video.author || 'Unknown Channel',
        imageSrc: img,
        meta: t('Reciente'),
        href: `/watch/${video.videoId}`
      }
    })
  } else {
    return [
      {
        id: 'dummy1',
        title: 'Neon Nights',
        description: 'Synthwave playlist',
        imageSrc: 'https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600&h=600&fit=crop',
        meta: t('Recomendado'),
        href: '#'
      },
      {
        id: 'dummy2',
        title: 'Blind',
        description: 'Wiz zee',
        imageSrc: 'https://images.unsplash.com/photo-1470225620780-dba8ba36b745?w=600&h=600&fit=crop',
        meta: t('Recomendado'),
        href: '#'
      },
      {
        id: 'dummy3',
        title: 'Solo',
        description: 'Horizon',
        imageSrc: 'https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=600&h=600&fit=crop',
        meta: t('Recomendado'),
        href: '#'
      }
    ]
  }
})
</script>

<style>
.premium-main:has(.home-page) {
  overflow: hidden !important;
  padding-block: 0 !important;
  padding-inline: 0 !important;
  height: 100vh !important;
  min-block-size: 100vh !important;
}
</style>

<style scoped>
.home-page {
  width: 100%;
  height: 100vh;
  color: #fff;
  overflow: hidden;
  position: relative;
  z-index: 10;
}
</style>
