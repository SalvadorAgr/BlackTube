<template>
  <canvas
    ref="canvasRef"
    class="ambient-aurora"
    aria-hidden="true"
  />
</template>

<script setup>
import { onBeforeUnmount, onMounted, useTemplateRef } from 'vue'

const canvasRef = useTemplateRef('canvasRef')
let animationFrameId
let removeResizeListener

onMounted(() => {
  const canvas = canvasRef.value
  const ctx = canvas.getContext('2d')
  let time = 0

  const setCanvasSize = () => {
    canvas.width = window.innerWidth
    canvas.height = window.innerHeight
  }

  setCanvasSize()
  window.addEventListener('resize', setCanvasSize)
  removeResizeListener = () => window.removeEventListener('resize', setCanvasSize)

  const colors = [
    { r: 45, g: 212, b: 191 },
    { r: 168, g: 85, b: 247 },
    { r: 59, g: 130, b: 246 },
    { r: 236, g: 72, b: 153 }
  ]

  class Orb {
    constructor() {
      this.reset()
      this.opacity = Math.random()
      this.isFadingOut = false
    }

    reset() {
      this.x = Math.random() * canvas.width
      this.y = Math.random() * canvas.height
      this.radius = Math.random() * 400 + 100
      this.color = colors[Math.floor(Math.random() * colors.length)]
      this.vx = (Math.random() - 0.5) * 0.5
      this.vy = (Math.random() - 0.5) * 0.5
      this.isFadingOut = false
    }

    draw() {
      const gradientRadius = this.radius * 1.7
      const gradient = ctx.createRadialGradient(this.x, this.y, 0, this.x, this.y, gradientRadius)
      gradient.addColorStop(0, `rgba(${this.color.r}, ${this.color.g}, ${this.color.b}, ${0.18 * this.opacity})`)
      gradient.addColorStop(0.45, `rgba(${this.color.r}, ${this.color.g}, ${this.color.b}, ${0.1 * this.opacity})`)
      gradient.addColorStop(1, `rgba(${this.color.r}, ${this.color.g}, ${this.color.b}, 0)`)

      ctx.fillStyle = gradient
      ctx.beginPath()
      ctx.arc(this.x, this.y, gradientRadius, 0, Math.PI * 2)
      ctx.fill()
    }

    update() {
      this.x += this.vx + Math.sin(time * 0.001) * 0.5
      this.y += this.vy + Math.cos(time * 0.001) * 0.5

      const isOutside =
        this.x < -this.radius ||
        this.x > canvas.width + this.radius ||
        this.y < -this.radius ||
        this.y > canvas.height + this.radius

      if (isOutside) {
        this.isFadingOut = true
      }

      if (this.isFadingOut) {
        this.opacity = Math.max(0, this.opacity - 0.01)
      } else {
        this.opacity = Math.min(1, this.opacity + 0.01)
      }

      if (this.opacity === 0) {
        this.reset()
      }
    }
  }

  const orbs = []
  for (let i = 0; i < 10; i++) {
    orbs.push(new Orb())
  }

  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height)
    time++

    orbs.forEach((orb) => {
      orb.update()
      orb.draw()
    })

    animationFrameId = requestAnimationFrame(animate)
  }

  animate()
})

onBeforeUnmount(() => {
  removeResizeListener?.()
  cancelAnimationFrame(animationFrameId)
})
</script>

<style scoped>
.ambient-aurora {
  position: fixed;
  inset: 0;
  z-index: 0;
  inline-size: 100vw;
  block-size: 100vh;
  opacity: 0.5;
  pointer-events: none;
}
</style>
