<template>
  <VaForm ref="form" @submit.prevent="submit">
    <h1 class="font-semibold text-4xl mb-4">{{ t('auth.SignUp') }}</h1>
    <p class="text-base mb-4 leading-5">
      {{ t('auth.already_account') }}
      <RouterLink :to="{ name: 'login' }" class="font-semibold text-primary">{{ t('auth.authorize') }}</RouterLink>
    </p>
    <VaInput
      v-model="formData.email"
      :rules="[(v) => !!v || 'Email field is required', (v) => /.+@.+\..+/.test(v) || 'Email should be valid']"
      class="mb-4"
      :label="t('auth.email')"
      type="email"
    />
    <VaValue v-slot="isPasswordVisible" :default-value="false">
      <VaInput
        ref="password1"
        v-model="formData.password"
        :rules="passwordRules"
        :type="isPasswordVisible.value ? 'text' : 'password'"
        class="mb-4"
        :label="t('auth.password')"
        :messages="t('auth.password_message')"
        @clickAppendInner.stop="isPasswordVisible.value = !isPasswordVisible.value"
      >
        <template #appendInner>
          <VaIcon
            :name="isPasswordVisible.value ? 'mso-visibility_off' : 'mso-visibility'"
            class="cursor-pointer"
            color="secondary"
          />
        </template>
      </VaInput>
      <VaInput
        ref="password2"
        v-model="formData.repeatPassword"
        :rules="[
          (v) => !!v || 'Repeat Password field is required',
          (v) => v === formData.password || 'Passwords don\'t match',
        ]"
        :type="isPasswordVisible.value ? 'text' : 'password'"
        class="mb-4"
        :label="t('auth.password_repeat')"
        @clickAppendInner.stop="isPasswordVisible.value = !isPasswordVisible.value"
      >
        <template #appendInner>
          <VaIcon
            :name="isPasswordVisible.value ? 'mso-visibility_off' : 'mso-visibility'"
            class="cursor-pointer"
            color="secondary"
          />
        </template>
      </VaInput>
    </VaValue>

    <div class="flex justify-center mt-4">
      <VaButton class="w-full" @click="submit">{{ t('auth.createAccount') }}</VaButton>
    </div>
  </VaForm>
</template>

<script lang="ts" setup>
import { reactive } from 'vue'
import { useForm } from 'vuestic-ui'

const { validate } = useForm('form')
const { t } = useI18n()
import axios from 'axios'
import { useI18n } from 'vue-i18n'

const formData = reactive({
  email: '',
  password: '',
  repeatPassword: '',
})

const submit = () => {
  if (validate()) {
    axios
      .post(
        '/api/auth/register',
        {
          email: String(formData.email),
          password: String(formData.password),
        },
        {
          headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
          },
        },
      )
      .then((response) => {
        if (response.status === 201) {
          window.location.href = '/faq'
        }
      })
      .catch((error) => {
        alert(error.response.data.detail)
      })
  }
}

const passwordRules: ((v: string) => boolean | string)[] = [
  (v) => !!v || 'Password field is required',
  (v) => (v && v.length >= 8) || 'Password must be at least 8 characters long',
  (v) => (v && /[A-Za-z]/.test(v)) || 'Password must contain at least one letter',
  (v) => (v && /\d/.test(v)) || 'Password must contain at least one number',
  (v) => (v && /[!@#$%^&*(),.?":{}|<>]/.test(v)) || 'Password must contain at least one special character',
]
</script>
