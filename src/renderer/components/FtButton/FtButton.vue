<template>
  <button
    class="btn ripple"
    :style="{
      color: textColor,
      backgroundColor: backgroundColor,
      borderColor: backgroundColor
    }"
    @click="click"
  >
    <slot>
      <LucideIcon
        v-if="typeof icon === 'string'"
        :name="icon"
        :size="18"
        :stroke-width="1.2"
      />
      <FontAwesomeIcon
        v-else-if="icon"
        :icon="icon"
      />
      {{ label }}
    </slot>
  </button>
</template>

<script setup>

defineProps({
  label: {
    type: String,
    default: ''
  },
  textColor: {
    type: String,
    default: 'var(--text-with-accent-color)'
  },
  backgroundColor: {
    type: String,
    default: 'var(--accent-color)'
  },
  icon: {
    type: [Array, String],
    default: null
  }
})

const emit = defineEmits(['click'])

function click() {
  emit('click')
}
</script>

<style scoped src="./FtButton.css" />
