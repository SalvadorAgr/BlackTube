<template>
  <div class="home-page font-sans">
    <div class="home-grid">
      <div class="content-left">
        <!-- Hero Section -->
        <section class="hero-section group">
          <img
            class="hero-img transition-transform duration-700 group-hover:scale-105"
            src="https://api.builder.io/api/v1/image/assets/TEMP/1b46568147c1aeb3a7496a7b4b84b4c5e2f77cc8?width=1374"
            alt="R&B Hits"
          />
          <div class="hero-overlay" />
          <div class="hero-content">
            <span class="category-tag">Curated playlist</span>
            <div class="hero-text-group">
              <h1 class="hero-title">R &amp; B Hits</h1>
              <p class="hero-description">
                All mine, Lie again, Petty call me everyday,<br />
                Out of time, No love, Bad habit,<br />
                and so much more
              </p>
            </div>
            <div class="hero-footer">
              <div class="user-stack">
                <div class="user-av" style="background:#E15A5A" />
                <div class="user-av" style="background:#5A9BE1" />
                <div class="user-av" style="background:#5AE19B" />
                <div class="user-av" style="background:#E1C45A" />
                <div class="user-av" style="background:#BE5AE1" />
              </div>
              <div class="likes-row">
                <LucideIcon name="Heart" class="text-white fill-white" :size="16" />
                <span class="likes-text">33k Likes</span>
              </div>
            </div>
          </div>
        </section>

        <!-- New Releases -->
        <section class="album-section">
          <h2 class="section-title">New releases</h2>
          <div class="albums-scroll custom-scrollbar">
            <AlbumCard
              v-for="album in newReleases"
              :key="album.title"
              :thumbnail="album.thumbnail"
              :title="album.title"
              :artist="album.artist"
            />
          </div>
        </section>

        <!-- Popular in your area -->
        <section class="album-section">
          <h2 class="section-title">Popular in your area</h2>
          <div class="albums-scroll custom-scrollbar">
            <AlbumCard
              v-for="album in popularAlbums"
              :key="album.title"
              :thumbnail="album.thumbnail"
              :title="album.title"
              :artist="album.artist"
            />
          </div>
        </section>
      </div>

      <!-- Top Charts -->
      <div class="content-right">
        <h2 class="section-title">Top charts</h2>
        <div class="charts-list">
          <ChartCard
            v-for="chart in topCharts"
            :key="chart.title"
            :thumbnail="chart.thumbnail"
            :title="chart.title"
            :artist="chart.artist"
            :duration="chart.duration"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import LucideIcon from '../../components/LucideIcon.vue'
import AlbumCard from '../../components/AlbumCard/AlbumCard.vue'
import ChartCard from '../../components/ChartCard/ChartCard.vue'

const newReleases = [
  { thumbnail: 'https://images.unsplash.com/photo-1614613535308-eb5fbd3d2c17?w=300&h=300&fit=crop', title: 'Life in a bubble', artist: 'The van' },
  { thumbnail: 'https://images.unsplash.com/photo-1493225255756-d9584f8606e9?w=300&h=300&fit=crop', title: 'Mountain', artist: 'Atlas' },
  { thumbnail: 'https://images.unsplash.com/photo-1470225620780-dba8ba36b745?w=300&h=300&fit=crop', title: 'Blind', artist: 'Wiz zee' },
  { thumbnail: 'https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=300&h=300&fit=crop', title: 'Solo', artist: 'Horizon' },
  { thumbnail: 'https://images.unsplash.com/photo-1459749411177-042180ce6742?w=300&h=300&fit=crop', title: 'Silhouette', artist: 'Melo' }
]

const popularAlbums = [
  { thumbnail: 'https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=300&h=300&fit=crop', title: 'Neon Nights', artist: 'Synthwave' },
  { thumbnail: 'https://images.unsplash.com/photo-1453090927415-5f45085b6aee?w=300&h=300&fit=crop', title: 'Vinyl Tales', artist: 'The Collector' },
  { thumbnail: 'https://images.unsplash.com/photo-1514525253361-bee871871771?w=300&h=300&fit=crop', title: 'Stadium Anthems', artist: 'Pulse' },
  { thumbnail: 'https://images.unsplash.com/photo-1420181910702-05573426e274?w=300&h=300&fit=crop', title: 'Electronic Dreams', artist: 'Future' },
  { thumbnail: 'https://images.unsplash.com/photo-1510915361894-db8b60106cb1?w=300&h=300&fit=crop', title: 'Dark Pulse', artist: 'Shadow' }
]

const topCharts = [
  { thumbnail: 'https://images.unsplash.com/photo-1619983081563-430f63602796?w=100&h=100&fit=crop', title: 'Golden age of 80s', artist: 'Sean swadder', duration: '2:34:45' },
  { thumbnail: 'https://images.unsplash.com/photo-1498038432885-c6f3f1b912ee?w=100&h=100&fit=crop', title: 'Reggae "n" blues', artist: 'Dj YK mule', duration: '1:02:42' },
  { thumbnail: 'https://images.unsplash.com/photo-1516280440614-37939bbacd81?w=100&h=100&fit=crop', title: "Tomorrow's tunes", artist: 'Obi Datti', duration: '2:01:25' }
]
</script>

<style scoped>
.home-page {
  padding: 0;
  color: #fff;
  min-height: 100%;
}

.home-grid {
  display: grid;
  grid-template-columns: 1fr 440px;
  gap: 40px;
  align-items: start;
}

/* Hero */
.hero-section {
  position: relative;
  width: 100%;
  height: 373px;
  border-radius: 15px;
  overflow: hidden;
  margin-bottom: 40px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}

.hero-img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to right, rgba(0,0,0,0.72) 0%, rgba(0,0,0,0.1) 70%, transparent 100%);
}

.hero-content {
  position: relative;
  z-index: 2;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 38px 45px;
}

.category-tag {
  font-size: 12px;
  font-weight: 400;
  color: #fff;
}

.hero-text-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.hero-title {
  font-size: 35px;
  font-weight: 700;
  color: #fff;
  margin: 0;
  line-height: 1.2;
}

.hero-description {
  font-size: 14px;
  font-weight: 400;
  color: #fff;
  margin: 0;
  line-height: 1.2;
}

.hero-footer {
  display: flex;
  align-items: center;
  gap: 11px;
}

.user-stack {
  display: flex;
}

.user-av {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: 2px solid rgba(255,255,255,0.3);
  margin-right: -6px;
}

.likes-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-left: 14px;
}

.likes-text {
  font-size: 14px;
  font-weight: 400;
  color: #fff;
}

/* Album sections */
.album-section {
  margin-bottom: 40px;
}

.section-title {
  font-size: 24px;
  font-weight: 700;
  background: linear-gradient(to right, #ffffff, #fca5a5); /* White to red-300 */
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  margin: 0 0 20px 0;
}


.albums-scroll {
  display: flex;
  gap: 24px;
  overflow-x: auto;
  padding-bottom: 12px;
}

.custom-scrollbar::-webkit-scrollbar {
  height: 4px;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background: rgba(255, 0, 64, 0.3);
  border-radius: 2px;
}

/* Right column */
.content-right {
  position: sticky;
  top: 0;
}

.charts-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

@media (max-width: 1200px) {
  .home-grid {
    grid-template-columns: 1fr;
  }
  .content-right {
    position: static;
  }
}
</style>
