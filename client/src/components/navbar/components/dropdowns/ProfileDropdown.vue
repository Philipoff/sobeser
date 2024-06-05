<template>
  <div class="profile-dropdown-wrapper">
    <VaButton v-model="isShown" preset="secondary" color="textPrimary" @click="$router.push('/faq')">
      <svg viewBox="4 4 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M16 15.503A5.041 5.041 0 1 0 16 5.42a5.041 5.041 0 0 0 0 10.083zm0 2.215c-6.703 0-11 3.699-11 5.5v3.363h22v-3.363c0-2.178-4.068-5.5-11-5.5z"/></svg>
    </VaButton>
  </div>
</template>

<script lang="ts" setup>
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { useColors } from 'vuestic-ui'

const { colors, setHSLAColor } = useColors()
const hoverColor = computed(() => setHSLAColor(colors.focus, { a: 0.1 }))

const { t } = useI18n()

type ProfileListItem = {
  name: string
  to?: string
  href?: string
  icon: string
}

type ProfileOptions = {
  name: string
  separator: boolean
  list: ProfileListItem[]
}

withDefaults(
  defineProps<{
    options?: ProfileOptions[]
  }>(),
  {
    options: () => [
      {
        name: 'account',
        separator: true,
        list: [
          {
            name: 'profile',
            to: 'preferences',
            icon: 'mso-account_circle',
          },
          {
            name: 'settings',
            to: 'settings',
            icon: 'mso-settings',
          },
          {
            name: 'billing',
            to: 'billing',
            icon: 'mso-receipt_long',
          },
          {
            name: 'projects',
            to: 'projects',
            icon: 'mso-favorite',
          },
        ],
      },
      {
        name: 'explore',
        separator: true,
        list: [
          {
            name: 'faq',
            to: 'faq',
            icon: 'mso-quiz',
          },
          {
            name: 'helpAndSupport',
            href: 'https://discord.gg/u7fQdqQt8c',
            icon: 'mso-error',
          },
        ],
      },
      {
        name: '',
        separator: false,
        list: [
          {
            name: 'logout',
            to: 'login',
            icon: 'mso-logout',
          },
        ],
      },
    ],
  },
)

const isShown = ref(false)

const resolveLinkAttribute = (item: ProfileListItem) => {
  return item.to ? { to: { name: item.to } } : item.href ? { href: item.href, target: '_blank' } : {}
}
</script>

<style lang="scss">
.profile-dropdown {
  cursor: pointer;

  &__content {
    .menu-item:hover {
      background: var(--hover-color);
    }
  }

  &__anchor {
    display: inline-block;
  }
}
</style>
