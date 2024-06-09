<template>
  <VaAvatar size="large" color="warning"><span class="text-4xl"> 😍 </span></VaAvatar>
  <div class="flex flex-col justify-center">
    <h2 class="text-[28px] md:text-[32px] leading-10 font-bold">{{ store.userName }}</h2>
    <div class="flex space-x-1 text-[13px] leading-4">
      <p>{{ t('preferences.member_since') }}</p>
      <p>{{ store.memberSince }}</p>
    </div>
  </div>
</template>
<script lang="ts" setup>
import { useUserStore } from '../../../stores/user-store'
import { useI18n } from 'vue-i18n'

const store = useUserStore()
const { t } = useI18n()
</script>
