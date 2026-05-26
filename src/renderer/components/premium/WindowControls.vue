<template>
  <div
    v-if="isElectron"
    class="window-controls-shell"
  >
    <div class="window-drag-region" />
    <div class="window-controls">
      <button
        v-for="control in controls"
        :key="control.action"
        type="button"
        :aria-label="control.label"
        :class="['window-control', control.className]"
        @click="handleControl(control.action)"
      />
    </div>
  </div>
</template>

<script setup>
const isElectron = process.env.IS_ELECTRON

const controls = [
  { action: 'close', label: 'Close window', className: 'close' },
  { action: 'minimize', label: 'Minimize window', className: 'minimize' },
  { action: 'toggle-maximize', label: 'Maximize window', className: 'maximize' }
]

function handleControl(action) {
  window.ftElectron.setWindowControlAction(action)
}
</script>

<style scoped>
.window-controls-shell {
  position: fixed;
  inset-block-start: 0;
  inset-inline-start: 0;
  z-index: 10000;
}

.window-drag-region {
  position: fixed;
  inset-block-start: 0;
  inset-inline: 0;
  block-size: 14px;
  -webkit-app-region: drag;
}

.window-controls {
  display: flex;
  gap: 8px;
  align-items: center;
  inline-size: 74px;
  block-size: 32px;
  padding-inline-start: 12px;
  -webkit-app-region: no-drag;
}

.window-control {
  inline-size: 12px;
  block-size: 12px;
  padding: 0;
  border: 0;
  border-radius: 50%;
  opacity: 0;
  transform: scale(0.72);
  transition:
    opacity 180ms ease,
    transform 180ms ease;
}

.window-controls:hover .window-control,
.window-controls:focus-within .window-control {
  opacity: 1;
  transform: scale(1);
}

.close {
  background: #ff5f57;
}

.minimize {
  background: #ffbd2e;
}

.maximize {
  background: #28c840;
}
</style>
