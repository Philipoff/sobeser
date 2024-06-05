<template>
  <VaForm ref="passwordForm" @submit.prevent="submit">
    <h1 class="font-semibold text-4xl mb-4">{{ t('auth.forgot_password') }}</h1>
    <p class="text-base mb-4 leading-5">
      {{ t('auth.forgot_message') }}
    </p>
    <VaInput
      v-model="email"
      :rules="[(v) => !!v || 'Email field is required']"
      class="mb-4"
      :label="t('auth.email')"
      type="email"
    />
    <VaButton class="w-full mb-2" @click="submit">{{ t('auth.send_password') }}</VaButton>
    <VaButton :to="{ name: 'login' }" class="w-full" preset="secondary" @click="submit">{{ t('auth.go_back') }}</VaButton>
  </VaForm>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { useForm } from 'vuestic-ui'
import { useRouter } from 'vue-router'
import {useI18n} from "vue-i18n";

const email = ref('')
const form = useForm('passwordForm')
const router = useRouter()
const {t} = useI18n()

const submit = () => {
  if (form.validate()) {
    router.push({ name: 'recover-password-email' })
  }
}
</script>
