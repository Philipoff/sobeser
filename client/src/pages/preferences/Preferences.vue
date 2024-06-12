<template>
  <h1 class="page-title">{{ t('preferences.Account') }}</h1>
  <div class="flex flex-col p-4 space-y-10 bg-backgroundSecondary rounded-lg">
    <div class="flex space-x-5">
      <PreferencesHeader v-model:memberSince="user_data.created_at"/>
    </div>
    <div class="space-y-4 md:space-y-6">
      <Settings @openNameModal="isEditNameModalOpen = true" @openResetPasswordModal="isResetPasswordModalOpen = true" />
    </div>
  </div>
  <EditNameModal v-if="isEditNameModalOpen" @cancel="isEditNameModalOpen = false" />
  <ResetPasswordModal v-if="isResetPasswordModalOpen" @cancel="isResetPasswordModalOpen = false" />
</template>
<script lang="ts" setup>
import {reactive, ref} from 'vue'

import PreferencesHeader from './preferences-header/PreferencesHeader.vue'
import Settings from './settings/Settings.vue'
import ResetPasswordModal from './modals/ResetPasswordModal.vue'
import { useI18n } from 'vue-i18n'
import axios from 'axios'
import questions from "../../data/pages/python-simple-questions.json";

const isEditNameModalOpen = ref(false)
const isResetPasswordModalOpen = ref(false)

const { t } = useI18n()

const user_data = reactive({
  email: '',
  created_at: '',
})

const get_user_info = () => {
  axios
    .post(
      '/api/profile/info',
      {
        token: String(localStorage.getItem("access_token")),
      },
      {
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
      },
    )
    .then((res) => {
      user_data.email = res.data["email"]
      user_data.created_at = res.data["created_at"]
    })
}

get_user_info()
</script>
