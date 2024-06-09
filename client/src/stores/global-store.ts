import { defineStore } from 'pinia'
import { useColors } from 'vuestic-ui'

export const useGlobalStore = defineStore('global', {
  state: () => {
    useColors().applyPreset(localStorage.getItem('theme') || 'light')
    return {
      isSidebarMinimized: false,
    }
  },

  actions: {
    toggleSidebar() {
      this.isSidebarMinimized = !this.isSidebarMinimized
    },
  },
})
