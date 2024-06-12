<template>
  <VaAvatar size="large" color="warning"><span class="text-4xl"> 😍 </span></VaAvatar>
  <div class="flex flex-col justify-center">
    <div class="flex space-x-1 text-[13px] leading-4">
      <p>{{ t('preferences.member_since') }}</p>
      <p>{{ props.memberSince }}</p>
    </div>
  </div>
</template>
<script lang="ts" setup>
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

const props = defineProps({
  memberSince: String,
})
console.log(props)
</script>
