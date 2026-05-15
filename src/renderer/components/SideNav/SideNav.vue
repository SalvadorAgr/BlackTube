<template>
  <div class="sidebar">
    <div class="sidebar-top">
      <div class="sidebar-menu">
        <div class="sidebar-menu-item active">
          <LucideIcon name="home" class="sidebar-menu-icon" :size="24" />
          <div class="sidebar-menu-title">
            <span>Home</span>
          </div>
        </div>
      </div>
      <div class="sidebar-menu">
        <div class="sidebar-menu-item">
          <LucideIcon name="compass" class="sidebar-menu-icon" :size="24" />
          <div class="sidebar-menu-title">
            <span>Explore</span>
          </div>
        </div>
      </div>
      <div class="sidebar-menu">
        <div class="sidebar-menu-item">
          <LucideIcon name="radio" class="sidebar-menu-icon" :size="24" />
          <div class="sidebar-menu-title">
            <span>Subscriptions</span>
          </div>
        </div>
      </div>
    </div>
    
    <div class="sidebar-top-2">
      <div class="border"></div>
      <div class="frame-1">
        <div class="sidebar-menu">
          <div class="sidebar-menu-item">
            <LucideIcon name="layout-grid" class="sidebar-menu-icon" :size="24" />
            <div class="sidebar-menu-title">
              <span>Library</span>
            </div>
          </div>
        </div>
        <div class="sidebar-menu">
          <div class="sidebar-menu-item">
            <LucideIcon name="history" class="sidebar-menu-icon" :size="24" />
            <div class="sidebar-menu-title">
              <span>History</span>
            </div>
          </div>
        </div>
        <div class="sidebar-menu">
          <div class="sidebar-menu-item">
            <LucideIcon name="play-square" class="sidebar-menu-icon" :size="24" />
            <div class="sidebar-menu-title">
              <span>Your Videos</span>
            </div>
          </div>
        </div>
        <div class="sidebar-menu">
          <div class="sidebar-menu-item">
            <LucideIcon name="clock" class="sidebar-menu-icon" :size="24" />
            <div class="sidebar-menu-title">
              <span>Watch Later</span>
            </div>
          </div>
        </div>
        <div class="sidebar-menu">
          <div class="sidebar-menu-item">
            <LucideIcon name="thumbs-up" class="sidebar-menu-icon" :size="24" />
            <div class="sidebar-menu-title">
              <span>Liked Videos</span>
            </div>
          </div>
        </div>
        <div class="sidebar-menu">
          <div class="sidebar-menu-item">
            <LucideIcon name="chevron-down" class="sidebar-menu-icon" :size="24" />
            <div class="sidebar-menu-title">
              <span>Show More</span>
            </div>
          </div>
        </div>
      </div>
      <div class="border"></div>
    </div>
    
    <div class="sidebar-subscriptions">
      <div class="sidebar-menu-title-header">
        <span class="subscriptions-text">SUBSCRIPTIONS</span>
      </div>
      <div class="frame-2">
        <div class="sidebar-menu">
          <div class="sidebar-menu-item">
            <div class="user-avatar-container bg-red"></div>
            <div class="sidebar-menu-title">
              <span>James Gouse</span>
            </div>
          </div>
        </div>
        <div class="sidebar-menu">
          <div class="sidebar-menu-item">
            <div class="user-avatar-container bg-teal"></div>
            <div class="sidebar-menu-title">
              <span>Alan Cooper</span>
            </div>
          </div>
        </div>
        <div class="sidebar-menu">
          <div class="sidebar-menu-item">
            <div class="user-avatar-container bg-gray"></div>
            <div class="sidebar-menu-title">
              <span>Marcus Levin</span>
            </div>
          </div>
        </div>
        <div class="sidebar-menu">
          <div class="sidebar-menu-item">
            <div class="user-avatar-container bg-pink"></div>
            <div class="sidebar-menu-title">
              <span>Alexis Sears</span>
            </div>
          </div>
        </div>
        <div class="sidebar-menu">
          <div class="sidebar-menu-item">
            <div class="user-avatar-container bg-purple"></div>
            <div class="sidebar-menu-title">
              <span>Jesica Lambert</span>
            </div>
          </div>
        </div>
        <div class="sidebar-menu">
          <div class="sidebar-menu-item">
            <div class="user-avatar-container bg-blue"></div>
            <div class="sidebar-menu-title">
              <span>Anna White</span>
            </div>
          </div>
        </div>
        <div class="sidebar-menu">
          <div class="sidebar-menu-item">
            <div class="user-avatar-container bg-yellow"></div>
            <div class="sidebar-menu-title">
              <span>Skylar Dias</span>
            </div>
          </div>
        </div>
        <div class="sidebar-menu">
          <div class="sidebar-menu-item">
            <LucideIcon name="chevron-down" class="sidebar-menu-icon" :size="24" />
            <div class="sidebar-menu-title">
              <span>Show 13 more</span>
            </div>
          </div>
        </div>
      </div>
      <div class="border"></div>
    </div>
    
    <div class="sidebar-more-from">
      <div class="sidebar-menu-title-header">
        <span class="subscriptions-text">MORE FROM YOUTUBE</span>
      </div>
      <div class="frame-3">
        <div class="sidebar-menu">
          <div class="sidebar-menu-item">
            <LucideIcon name="award" class="sidebar-menu-icon" :size="24" />
            <div class="sidebar-menu-title">
              <span>YouTube Premium</span>
            </div>
          </div>
        </div>
        <div class="sidebar-menu">
          <div class="sidebar-menu-item">
            <LucideIcon name="gamepad-2" class="sidebar-menu-icon" :size="24" />
            <div class="sidebar-menu-title">
              <span>Gaming</span>
            </div>
          </div>
        </div>
        <div class="sidebar-menu">
          <div class="sidebar-menu-item">
            <LucideIcon name="radio-receiver" class="sidebar-menu-icon" :size="24" />
            <div class="sidebar-menu-title">
              <span>Live</span>
            </div>
          </div>
        </div>
        <div class="sidebar-menu">
          <div class="sidebar-menu-item">
            <LucideIcon name="trophy" class="sidebar-menu-icon" :size="24" />
            <div class="sidebar-menu-title">
              <span>Sports</span>
            </div>
          </div>
        </div>
      </div>
      <div class="border"></div>
    </div>
    
    <div class="sidebar-bottom">
      <div class="frame-4">
        <div class="sidebar-menu">
          <div class="sidebar-menu-item">
            <LucideIcon name="settings" class="sidebar-menu-icon" :size="24" />
            <div class="sidebar-menu-title">
              <span>Settings</span>
            </div>
          </div>
        </div>
        <div class="sidebar-menu">
          <div class="sidebar-menu-item">
            <LucideIcon name="flag" class="sidebar-menu-icon" :size="24" />
            <div class="sidebar-menu-title">
              <span>Report history</span>
            </div>
          </div>
        </div>
        <div class="sidebar-menu">
          <div class="sidebar-menu-item">
            <LucideIcon name="circle-help" class="sidebar-menu-icon" :size="24" />
            <div class="sidebar-menu-title">
              <span>Help</span>
            </div>
          </div>
        </div>
        <div class="sidebar-menu">
          <div class="sidebar-menu-item">
            <LucideIcon name="message-square" class="sidebar-menu-icon" :size="24" />
            <div class="sidebar-menu-title">
              <span>Send feedback</span>
            </div>
          </div>
        </div>
      </div>
      <div class="border"></div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from '../../composables/use-i18n-polyfill'

import LucideIcon from '../LucideIcon.vue'
import SideNavMoreOptions from '../SideNavMoreOptions/SideNavMoreOptions.vue'

import store from '../../store/index'

import { youtubeImageUrlToInvidious } from '../../helpers/api/invidious'
import { deepCopy, localizeAndAddKeyboardShortcutToActionTitle } from '../../helpers/utils'
import { KeyboardShortcuts } from '../../../constants'

const { locale, t } = useI18n()

const SUPPORTS_LOCAL_API = process.env.SUPPORTS_LOCAL_API

/** @type {import('vue').ComputedRef<boolean>} */
const isOpen = computed(() => {
  return store.getters.getIsSideNavOpen
})

/** @type {import('vue').ComputedRef<boolean>} */
const backendFallback = computed(() => {
  return store.getters.getBackendFallback
})

/** @type {import('vue').ComputedRef<'local' | 'invidious'>} */
const backendPreference = computed(() => {
  return store.getters.getBackendPreference
})

/** @type {import('vue').ComputedRef<string>} */
const currentInvidiousInstanceUrl = computed(() => {
  return store.getters.getCurrentInvidiousInstanceUrl
})

/** @type {import('vue').ComputedRef<object>} */
const activeProfile = computed(() => {
  return store.getters.getActiveProfile
})

const activeSubscriptions = computed(() => {
  /** @type {any[]} */
  const subscriptions = deepCopy(activeProfile.value.subscriptions)

  subscriptions.forEach(channel => {
    // Change thumbnail size to 35x35, as that's the size we display it
    // so we don't need to download a bigger image (the default is 176x176)
    channel.thumbnail = channel.thumbnail?.replace(/=s\d+/, '=s35')
  })

  const locale_ = locale.value
  subscriptions.sort((a, b) => {
    return a.name?.toLowerCase().localeCompare(b.name?.toLowerCase(), locale_)
  })

  if (backendPreference.value === 'invidious') {
    const instanceUrl = currentInvidiousInstanceUrl.value

    subscriptions.forEach((channel) => {
      channel.thumbnail = youtubeImageUrlToInvidious(channel.thumbnail, instanceUrl)
    })
  }

  return subscriptions
})

/** @type {import('vue').ComputedRef<boolean>} */
const hidePopularVideos = computed(() => {
  return store.getters.getHidePopularVideos
})

/** @type {import('vue').ComputedRef<boolean>} */
const hidePlaylists = computed(() => {
  return store.getters.getHidePlaylists
})

/** @type {import('vue').ComputedRef<boolean>} */
const hideTrendingVideos = computed(() => {
  return store.getters.getHideTrendingVideos
})

/** @type {import('vue').ComputedRef<boolean>} */
const hideActiveSubscriptions = computed(() => {
  return store.getters.getHideActiveSubscriptions
})

/** @type {import('vue').ComputedRef<boolean>} */
const hideText = computed(() => {
  return !isOpen.value && store.getters.getHideLabelsSideBar
})

const applyNavIconExpand = computed(() => {
  return {
    navIconExpand: hideText.value
  }
})

const applyHiddenLabels = computed(() => {
  return {
    hiddenLabels: hideText.value
  }
})

const historyTitle = computed(() => {
  const shortcut = process.platform === 'darwin'
    ? KeyboardShortcuts.APP.GENERAL.NAVIGATE_TO_HISTORY_MAC
    : KeyboardShortcuts.APP.GENERAL.NAVIGATE_TO_HISTORY

  return localizeAndAddKeyboardShortcutToActionTitle(
    t('History.History'),
    shortcut
  )
})

const settingsTitle = computed(() => {
  return localizeAndAddKeyboardShortcutToActionTitle(
    t('Settings.Settings'),
    KeyboardShortcuts.APP.GENERAL.NAVIGATE_TO_SETTINGS
  )
})
</script>

<style scoped src="./SideNav.css" />
