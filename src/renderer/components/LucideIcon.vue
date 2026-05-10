<template>
  <component
    :is="iconComponent"
    v-if="iconComponent"
    class="lucide-icon"
    :size="size"
    :stroke-width="strokeWidth"
    :color="color"
  />
</template>

<script setup>
import { computed } from 'vue'
import * as icons from 'lucide-vue-next'

const props = defineProps({
  name: {
    type: String,
    required: true
  },
  size: {
    type: [Number, String],
    default: 24
  },
  strokeWidth: {
    type: [Number, String],
    default: 1.2
  },
  color: {
    type: String,
    default: 'currentColor'
  }
})

const iconComponent = computed(() => {
  if (!props.name) return null
  // Convert kebab-case or snake_case to PascalCase for Lucide icons
  const pascalName = props.name
    .split(/[-_]/)
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join('')
  
  return icons[pascalName] || icons[props.name] || null
})
</script>

<style scoped>
.lucide-icon {
  display: inline-block;
  vertical-align: middle;
}
</style>
