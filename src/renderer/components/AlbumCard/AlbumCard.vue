<template>
  <div class="album-card">
    <div class="album-thumbnail">
      <img :src="thumbnail" :alt="title" v-if="thumbnail" />
      <div class="thumbnail-placeholder" v-else></div>
      <div class="play-overlay">
        <LucideIcon name="play" :size="32" fill="white" />
      </div>
    </div>
    <div class="album-info">
      <h3 class="album-title">{{ title }}</h3>
      <p class="album-subtitle">{{ subtitle }}</p>
    </div>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'
import LucideIcon from '../LucideIcon.vue'

const props = defineProps({
  thumbnail: String,
  title: String,
  subtitle: String
})
</script>

<style scoped>
.album-card {
  width: 180px;
  cursor: pointer;
  transition: transform 0.3s;
}

.album-card:hover {
  transform: translateY(-5px);
}

.album-thumbnail {
  position: relative;
  width: 100%;
  aspect-ratio: 1;
  border-radius: 20px;
  overflow: hidden;
  background: #252525;
  margin-bottom: 12px;
}

.album-thumbnail img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.thumbnail-placeholder {
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #333, #222);
}

.play-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s;
}

.album-card:hover .play-overlay {
  opacity: 1;
}

.album-title {
  font-size: 16px;
  font-weight: 700;
  color: #fff;
  margin: 0 0 4px 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.album-subtitle {
  font-size: 14px;
  color: rgba(255,255,255,0.6);
  margin: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
