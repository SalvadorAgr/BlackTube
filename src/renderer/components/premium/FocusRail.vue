<template>
  <div
    tabindex="0"
    class="group relative flex h-full w-full flex-col overflow-hidden bg-black/10 backdrop-blur-2xl text-white outline-none select-none overflow-x-hidden border-none focus-rail"
    @mouseenter="isHovering = true"
    @mouseleave="isHovering = false"
    @focusin="isHovering = true"
    @focusout="isHovering = false"
    @keydown="onKeyDown"
    @wheel.prevent="onWheel"
  >
    <!-- Background Ambience -->
    <div class="absolute inset-0 z-0 pointer-events-none">
      <transition name="fade">
        <div
          :key="activeItem.id"
          class="absolute inset-0"
        >
          <img
            :src="activeItem.imageSrc"
            alt=""
            class="h-full w-full object-cover blur-3xl saturate-200 opacity-40"
          >
          <div class="absolute inset-0 bg-gradient-to-t from-black via-black/50 to-transparent" />
        </div>
      </transition>
    </div>

    <!-- Main Stage -->
    <div class="relative z-10 flex flex-1 flex-col justify-center px-4 md:px-8">
      <div
        class="relative mx-auto flex h-[340px] w-full max-w-6xl items-center justify-center perspective-[1200px]"
        @mousedown="onDragStart"
        @touchstart="onDragStart"
      >
        <div
          v-for="offset in visibleIndices"
          :key="getAbsIndex(offset)"
          role="button"
          tabindex="0"
          :class="[
            'absolute aspect-[3/4] w-[240px] md:w-[280px] rounded-2xl bg-black/40 backdrop-blur-md shadow-2xl transition-all duration-500 ease-out cursor-pointer focus:outline-none focus:ring-2 focus:ring-[#ff0040]',
            offset === 0 ? 'z-20 shadow-black/60' : 'z-10'
          ]"
          :style="getTransform(offset)"
          @click="offset !== 0 ? setActiveOffset(offset) : handleListen()"
          @keydown.enter="offset !== 0 ? setActiveOffset(offset) : handleListen()"
          @keydown.space.prevent="offset !== 0 ? setActiveOffset(offset) : handleListen()"
        >
          <img
            :src="getItem(offset).imageSrc"
            :alt="getItem(offset).title"
            class="h-full w-full rounded-2xl object-cover pointer-events-none"
          >
          <!-- Lighting layers -->
          <div class="absolute inset-0 rounded-2xl bg-gradient-to-b from-black/20 to-transparent pointer-events-none" />
          <div class="absolute inset-0 rounded-2xl bg-black/20 pointer-events-none mix-blend-multiply" />
        </div>
      </div>

      <!-- Info & Controls -->
      <div class="mx-auto mt-6 flex w-full max-w-4xl flex-col items-center justify-between gap-6 md:flex-row pointer-events-auto">
        <div class="flex flex-1 flex-col items-center text-center md:items-start md:text-left h-28 justify-center">
          <transition
            name="slide-up"
            mode="out-in"
          >
            <div
              :key="activeItem.id"
              class="space-y-2"
            >
              <span
                v-if="activeItem.meta"
                class="text-xs font-medium uppercase tracking-wider text-[#ff0040] drop-shadow-[0_0_8px_rgba(255,0,64,0.4)]"
              >
                {{ activeItem.meta }}
              </span>
              <h2 class="text-2xl font-bold tracking-tight md:text-3xl text-white">
                {{ activeItem.title }}
              </h2>
              <p
                v-if="activeItem.description"
                class="max-w-md text-neutral-400 truncate"
              >
                {{ activeItem.description }}
              </p>
            </div>
          </transition>
        </div>

        <div class="flex items-center gap-4">
          <div class="flex items-center gap-1 rounded-full bg-black/40 p-1 backdrop-blur-2xl">
            <button
              :aria-label="t('Video.Previous')"
              class="rounded-full p-3 text-neutral-400 transition hover:bg-black/50 hover:text-white active:scale-95 cursor-pointer"
              @click.stop="handlePrev"
            >
              <LucideIcon
                name="ChevronLeft"
                class="h-5 w-5"
              />
            </button>
            <button
              :aria-label="t('Video.Next')"
              class="rounded-full p-3 text-neutral-400 transition hover:bg-black/50 hover:text-white active:scale-95 cursor-pointer"
              @click.stop="handleNext"
            >
              <LucideIcon
                name="ChevronRight"
                class="h-5 w-5"
              />
            </button>
          </div>

          <a
            :href="activeItem.href"
            class="group flex items-center gap-2 rounded-full bg-[#ff0040] hover:bg-[#ff1a53] px-5 py-3 text-sm font-semibold text-white transition-all duration-300 hover:scale-105 active:scale-95 shadow-[0_0_20px_rgba(255,0,64,0.4)] cursor-pointer"
            @click.prevent="handleListen"
          >
            {{ t('Escuchar') }}
            <LucideIcon
              name="ArrowUpRight"
              class="h-4 w-4 transition-transform group-hover:-translate-y-0.5 group-hover:translate-x-0.5"
            />
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, watch, onBeforeUnmount, defineProps } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from '../../composables/use-i18n-polyfill'
import LucideIcon from '../LucideIcon.vue'

const { t } = useI18n()

const props = defineProps({
  items: {
    type: Array,
    required: true
  },
  initialIndex: {
    type: Number,
    default: 0
  },
  loop: {
    type: Boolean,
    default: true
  },
  autoPlay: {
    type: Boolean,
    default: true
  },
  interval: {
    type: Number,
    default: 5000
  }
})

const router = useRouter()
const active = ref(props.initialIndex)
const isHovering = ref(false)
const lastWheelTime = ref(0)
const visibleIndices = [-2, -1, 0, 1, 2]

const count = computed(() => props.items.length)

function wrap(min, max, v) {
  if (max === 0) return 0
  const rangeSize = max - min
  return ((((v - min) % rangeSize) + rangeSize) % rangeSize) + min
}

const activeIndex = computed(() => wrap(0, count.value, active.value))
const activeItem = computed(() => props.items[activeIndex.value] || {})

function getAbsIndex(offset) {
  return active.value + offset
}

function getItem(offset) {
  const absIndex = active.value + offset
  const index = wrap(0, count.value, absIndex)
  return props.items[index] || {}
}

function setActiveOffset(offset) {
  active.value += offset
  resetTimer()
}

function handlePrev() {
  if (!props.loop && active.value === 0) return
  active.value -= 1
  resetTimer()
}

function handleNext() {
  if (!props.loop && active.value === count.value - 1) return
  active.value += 1
  resetTimer()
}

function handleListen() {
  if (activeItem.value.href) {
    router.push(activeItem.value.href)
  }
}

function onWheel(e) {
  const now = Date.now()
  if (now - lastWheelTime.value < 400) return

  const isHorizontal = Math.abs(e.deltaX) > Math.abs(e.deltaY)
  const delta = isHorizontal ? e.deltaX : e.deltaY

  if (Math.abs(delta) > 20) {
    if (delta > 0) {
      handleNext()
    } else {
      handlePrev()
    }
    lastWheelTime.value = now
  }
}

function onKeyDown(e) {
  if (e.key === 'ArrowLeft') handlePrev()
  if (e.key === 'ArrowRight') handleNext()
}

// Transform calculations for the 3D rail effect
function getTransform(offset) {
  const isCenter = offset === 0
  const dist = Math.abs(offset)

  const xOffset = offset * 320
  const zOffset = -dist * 180
  const scale = isCenter ? 1 : 0.85
  const rotateY = offset * -20

  const opacity = isCenter ? 1 : Math.max(0.1, 1 - dist * 0.5)
  const blur = isCenter ? 0 : dist * 6
  const brightness = isCenter ? 1 : 0.5

  return {
    transform: `translateX(${xOffset}px) translateZ(${zOffset}px) scale(${scale}) rotateY(${rotateY}deg)`,
    opacity,
    filter: `blur(${blur}px) brightness(${brightness})`,
    transformStyle: 'preserve-3d',
    zIndex: isCenter ? 20 : 10
  }
}

// Drag logic
let startX = 0
function onDragStart(e) {
  startX = e.type.includes('mouse') ? e.pageX : e.touches[0].pageX
  document.addEventListener('mousemove', onDragMove)
  document.addEventListener('mouseup', onDragEnd)
  document.addEventListener('touchmove', onDragMove)
  document.addEventListener('touchend', onDragEnd)
}

function onDragMove(e) {
  // Can implement dynamic visual drag if needed, but for now just wait for end to swipe
}

function onDragEnd(e) {
  const endX = e.type.includes('mouse') ? e.pageX : e.changedTouches[0].pageX
  const diff = startX - endX

  if (diff > 50) {
    handleNext()
  } else if (diff < -50) {
    handlePrev()
  }

  document.removeEventListener('mousemove', onDragMove)
  document.removeEventListener('mouseup', onDragEnd)
  document.removeEventListener('touchmove', onDragMove)
  document.removeEventListener('touchend', onDragEnd)
}

// Autoplay
let timer
function startTimer() {
  clearInterval(timer)
  if (props.autoPlay && !isHovering.value) {
    timer = setInterval(() => {
      handleNext()
      resetTimer()
    }, props.interval)
  }
}

function resetTimer() {
  startTimer()
}

watch([() => props.autoPlay, isHovering], ([auto, hovering]) => {
  startTimer()
}, { immediate: true })

onBeforeUnmount(() => {
  clearInterval(timer)
})
</script>

<style scoped>
.perspective-\[1200px\] {
  perspective: 1200px;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.8s ease-out;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.slide-up-enter-active,
.slide-up-leave-active {
  transition: all 0.3s ease;
}
.slide-up-enter-from {
  opacity: 0;
  transform: translateY(10px);
  filter: blur(4px);
}
.slide-up-leave-to {
  opacity: 0;
  transform: translateY(-10px);
  filter: blur(4px);
}
</style>
