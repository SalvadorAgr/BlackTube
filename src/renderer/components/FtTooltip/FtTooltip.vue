<template>
  <div class="tooltip">
    <button
      :aria-labelledby="id"
      class="button"
      type="button"
    >
      <LucideIcon name="question-circle" :size="18" />
    </button>
    <p
      :id="id"
      class="text"
      :class="{
        [position]: true,
        allowNewlines,
      }"
      role="tooltip"
    >
      {{ tooltip }}
    </p>
  </div>
</template>

<script setup>
import { useId } from 'vue'

defineProps({
  position: {
    type: String,
    default: 'bottom',
    validator: (value) => value === 'bottom' || value === 'left' || value === 'right' || value === 'top' || value === 'bottom-left'
  },
  tooltip: {
    type: String,
    required: true
  },
  allowNewlines: {
    type: Boolean,
    default: false,
  },
})

const id = useId()
</script>

<style scoped src="./FtTooltip.css" />
