<template>
  <div class="flex flex-col md:flex-row space-y-2 md:space-y-0 md:space-x-6 min-h-[36px] leading-5">
    <p class="font-bold w-[200px]">{{ t('preferences.Email') }}</p>
    <div class="flex-1">
      <div class="max-w-[748px]">
        {{ email }}
      </div>
    </div>
  </div>
  <div class="flex flex-col md:flex-row space-y-2 md:space-y-0 md:space-x-6 min-h-[36px] leading-5">
    <p class="font-bold w-[200px]">{{ t('preferences.Password') }}</p>
    <div class="flex-1">
      <div class="max-w-[748px]">•••••••••••••</div>
    </div>
    <VaButton :style="buttonStyles" class="w-fit h-fit" preset="primary" @click="emits('openResetPasswordModal')">
      {{ t('preferences.reset_password') }}
    </VaButton>
  </div>
  <VaDivider />
  <div class="flex flex-col md:flex-row space-y-2 md:space-y-0 md:space-x-6 min-h-[36px] leading-5">
    <p class="font-bold w-[200px]">{{ t('preferences.email_sub') }}</p>
    <div class="flex-1">
      <div class="max-w-[748px]">
        <p>{{ t('preferences.manage') }}</p>
        <div class="flex space-x-1 w-fit">
          <RouterLink :to="{ name: 'settings' }" class="font-semibold text-primary">{{ t('preferences.manage_button') }}</RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts" setup>
import { useUserStore } from '../../../stores/user-store'

import { buttonStyles } from '../styles'
import {useI18n} from "vue-i18n";

const store = useUserStore()

const emits = defineEmits(['openNameModal', 'openResetPasswordModal'])

const { t } = useI18n()
const email = localStorage.getItem("email");
</script>
