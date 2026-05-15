<template>
  <div class="chart-card">
    <div class="chart-thumbnail">
      <img :src="thumbnail" :alt="title" v-if="thumbnail" />
      <div class="thumbnail-placeholder" v-else></div>
    </div>
    <div class="chart-info">
      <h4 class="chart-title">{{ title }}</h4>
      <p class="chart-subtitle">{{ subtitle }}</p>
    </div>
    <div class="chart-duration">{{ duration }}</div>
    <button class="chart-action">
      <LucideIcon name="heart" :size="18" />
    </button>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'
import LucideIcon from '../LucideIcon.vue'

const props = defineProps({
  thumbnail: String,
  title: String,
  subtitle: String,
  duration: String
})
</script>

<style scoped>
.chart-card {
  display: flex;
  align-items: center;
  padding: 12px;
  background: rgba(255, 255, 255, 0.03);
  border-radius: 12px;
  margin-bottom: 8px;
  transition: background 0.2s;
  cursor: pointer;
}

.chart-card:hover {
  background: rgba(255, 255, 255, 0.07);
}

.chart-thumbnail {
  width: 50px;
  height: 50px;
  border-radius: 8px;
  overflow: hidden;
  margin-right: 16px;
  flex-shrink: 0;
}

.chart-thumbnail img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.thumbnail-placeholder {
  width: 100%;
  height: 100%;
  background: #333;
}

.chart-info {
  flex: 1;
  min-width: 0;
}

.chart-title {
  font-size: 14px;
  font-weight: 600;
  color: #fff;
  margin: 0 0 4px 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.chart-subtitle {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.5);
  margin: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.chart-duration {
  font-size: 12px;
  color: rgba(255, 255, 255, 0.5);
  margin: 0 16px;
}

.chart-action {
  background: transparent;
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: #fff;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: border-color 0.2s;
}

.chart-action:hover {
  border-color: #FF0000;
  color: #FF0000;
}
</style>
