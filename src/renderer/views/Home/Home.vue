<template>
  <div class="home-page">
    <div class="home-grid">
      <div class="content-left">
        <!-- Hero Section -->
        <section class="hero-section">
          <img
            class="hero-img"
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
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
                  <path d="M5.51981 1.66697C5.93981 1.67975 6.34647 1.75308 6.74047 1.88708H6.77981C6.80647 1.89975 6.82647 1.91375 6.83981 1.92641C6.98714 1.97375 7.12647 2.02708 7.25981 2.10041L7.51314 2.21375C7.61314 2.26708 7.73314 2.36641 7.79981 2.40708C7.86647 2.44641 7.93981 2.48708 7.99981 2.53308C8.74047 1.96708 9.63981 1.66041 10.5665 1.66697C10.9871 1.66697 11.4071 1.72641 11.8065 1.86041C14.2671 2.66041 15.1538 5.36041 14.4131 7.72041C13.9931 8.92641 13.3065 10.0271 12.4071 10.9264C11.1198 12.1731 9.70714 13.2797 8.18647 14.2331L8.01981 14.3337L7.84647 14.2264C6.32047 13.2797 4.89981 12.1731 3.60047 10.9197C2.70714 10.0204 2.01981 8.92641 1.59314 7.72041C0.839808 5.36041 1.72647 2.66041 4.21381 1.84641C4.40714 1.77975 4.60647 1.73308 4.80647 1.70708H4.88647C5.07381 1.67975 5.25981 1.66697 5.44647 1.66697H5.51981Z" fill="white"/>
                </svg>
                <span class="likes-text">33k Likes</span>
              </div>
            </div>
          </div>
        </section>

        <!-- New Releases -->
        <section class="album-section">
          <h2 class="section-title">New releases.</h2>
          <div class="albums-scroll">
            <AlbumCard
              v-for="album in newReleases"
              :key="album.title"
              :thumbnail="album.thumbnail"
              :title="album.title"
              :subtitle="album.subtitle"
            />
          </div>
        </section>

        <!-- Popular in your area -->
        <section class="album-section">
          <h2 class="section-title">Popular in your area</h2>
          <div class="albums-scroll">
            <AlbumCard
              v-for="album in popularAlbums"
              :key="album.title"
              :thumbnail="album.thumbnail"
              :title="album.title"
              :subtitle="album.subtitle"
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
            :key="chart.title + chart.subtitle"
            :thumbnail="chart.thumbnail"
            :title="chart.title"
            :subtitle="chart.subtitle"
            :duration="chart.duration"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import AlbumCard from '../../components/AlbumCard/AlbumCard.vue'
import ChartCard from '../../components/ChartCard/ChartCard.vue'

const newReleases = [
  {
    thumbnail: 'https://api.builder.io/api/v1/image/assets/TEMP/7a5aa2d22c192bf624626488880ef0084abebec3?width=247',
    title: 'Life in a bubble',
    subtitle: 'The van'
  },
  {
    thumbnail: 'https://api.builder.io/api/v1/image/assets/TEMP/f858edc0e10e280d64773988478b1878f0a2c511?width=247',
    title: 'Mountain',
    subtitle: 'Atlas'
  },
  {
    thumbnail: 'https://api.builder.io/api/v1/image/assets/TEMP/a0aec7389b59c267fe9e6cb147a75e605ac97963?width=247',
    title: 'Blind',
    subtitle: 'Wiz zee'
  },
  {
    thumbnail: 'https://api.builder.io/api/v1/image/assets/TEMP/7a5aa2d22c192bf624626488880ef0084abebec3?width=247',
    title: 'Solo',
    subtitle: 'Horizon'
  },
  {
    thumbnail: 'https://api.builder.io/api/v1/image/assets/TEMP/f858edc0e10e280d64773988478b1878f0a2c511?width=247',
    title: 'Silhouette',
    subtitle: 'Melo'
  }
]

const popularAlbums = [
  {
    thumbnail: 'https://api.builder.io/api/v1/image/assets/TEMP/a0aec7389b59c267fe9e6cb147a75e605ac97963?width=247',
    title: 'Blind',
    subtitle: 'Wiz zee'
  },
  {
    thumbnail: 'https://api.builder.io/api/v1/image/assets/TEMP/7a5aa2d22c192bf624626488880ef0084abebec3?width=247',
    title: 'Life in a bubble',
    subtitle: 'The van'
  },
  {
    thumbnail: 'https://api.builder.io/api/v1/image/assets/TEMP/f858edc0e10e280d64773988478b1878f0a2c511?width=247',
    title: 'Mountain',
    subtitle: 'Atlas'
  },
  {
    thumbnail: 'https://api.builder.io/api/v1/image/assets/TEMP/a0aec7389b59c267fe9e6cb147a75e605ac97963?width=247',
    title: 'Skyline',
    subtitle: 'Jay Waves'
  },
  {
    thumbnail: 'https://api.builder.io/api/v1/image/assets/TEMP/7a5aa2d22c192bf624626488880ef0084abebec3?width=247',
    title: 'Drift',
    subtitle: 'Cleo'
  }
]

const topCharts = [
  {
    thumbnail: 'https://api.builder.io/api/v1/image/assets/TEMP/af7702757e2b9acc3d3b60b26646e0695b72b414?width=126',
    title: 'Golden age of 80s',
    subtitle: 'Sean swadder',
    duration: '2:34:45'
  },
  {
    thumbnail: 'https://api.builder.io/api/v1/image/assets/TEMP/f145488e1f5722949886d8413bb203014c71f404?width=126',
    title: 'Reggae "n" blues',
    subtitle: 'Dj YK mule',
    duration: '1:02:42'
  },
  {
    thumbnail: 'https://api.builder.io/api/v1/image/assets/TEMP/55e95901fbaebef9b7a2102c0f4eb0c72bfd33cb?width=126',
    title: "Tomorrow's tunes",
    subtitle: 'Obi Datti',
    duration: '2:01:25'
  },
  {
    thumbnail: 'https://api.builder.io/api/v1/image/assets/TEMP/af7702757e2b9acc3d3b60b26646e0695b72b414?width=126',
    title: 'Golden age of 80s',
    subtitle: 'Sean swadder',
    duration: '2:34:45'
  },
  {
    thumbnail: 'https://api.builder.io/api/v1/image/assets/TEMP/f145488e1f5722949886d8413bb203014c71f404?width=126',
    title: 'Reggae "n" blues',
    subtitle: 'Dj YK mule',
    duration: '1:02:42'
  },
  {
    thumbnail: 'https://api.builder.io/api/v1/image/assets/TEMP/55e95901fbaebef9b7a2102c0f4eb0c72bfd33cb?width=126',
    title: "Tomorrow's tunes",
    subtitle: 'Obi Datti',
    duration: '2:01:25'
  }
]
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;700&display=swap');

.home-page {
  padding: 24px 24px 100px;
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
  font-family: 'Quicksand', sans-serif;
  font-size: 12px;
  font-weight: 400;
  color: #fff;
  line-height: 1.2;
}

.hero-text-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.hero-title {
  font-family: 'Quicksand', sans-serif;
  font-size: 35px;
  font-weight: 700;
  color: #fff;
  margin: 0;
  line-height: 1.2;
}

.hero-description {
  font-family: 'Quicksand', sans-serif;
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
  font-family: 'Quicksand', sans-serif;
  font-size: 14px;
  font-weight: 400;
  color: #fff;
  line-height: 1.2;
}

/* Album sections */
.album-section {
  margin-bottom: 40px;
}

.section-title {
  font-family: 'Quicksand', sans-serif;
  font-size: 24px;
  font-weight: 700;
  color: #EFEEE0;
  margin: 0 0 20px 0;
}

.albums-scroll {
  display: flex;
  gap: 24px;
  overflow-x: auto;
  padding-bottom: 12px;
}

.albums-scroll::-webkit-scrollbar {
  height: 4px;
}

.albums-scroll::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.12);
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
  gap: 8px;
}

@media (max-width: 1100px) {
  .home-grid {
    grid-template-columns: 1fr;
  }
}
</style>
