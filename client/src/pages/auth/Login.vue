<template>
  <VaForm ref="form" @submit.prevent="submit">
    <h1 class="font-semibold text-4xl mb-4">Вход</h1>
    <p class="text-base mb-4 leading-5">
      Ещё нет аккаунта?
      <RouterLink :to="{ name: 'signup' }" class="font-semibold text-primary">Зарегистрируйтесь</RouterLink>
    </p>
    <VaInput
      v-model="formData.email"
      :rules="[validators.required, validators.email]"
      class="mb-4"
      label="Почта"
      type="email"
    />
    <VaValue v-slot="isPasswordVisible" :default-value="false">
      <VaInput
        v-model="formData.password"
        :rules="[validators.required]"
        :type="isPasswordVisible.value ? 'text' : 'password'"
        class="mb-4"
        label="Пароль"
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

    <div class="auth-layout__options flex flex-col sm:flex-row items-start sm:items-center justify-between">
      <VaCheckbox v-model="formData.keepLoggedIn" class="mb-2 sm:mb-0" label="Запомнить меня" />
      <RouterLink :to="{ name: 'recover-password' }" class="mt-2 sm:mt-0 sm:ml-1 font-semibold text-primary">
        Забыли пароль?
      </RouterLink>
    </div>

    <div class="flex justify-center mt-4">
      <VaButton class="w-full" @click="submit">Войти</VaButton>
    </div>
  </VaForm>
</template>

<script lang="ts" setup>
import { reactive } from 'vue'
import { useForm, useToast } from 'vuestic-ui'
import { validators } from '../../services/utils'
const { validate } = useForm('form')
const { init } = useToast()
import axios from 'axios'
import { useUserStore } from '../../stores/user-store'

const store = useUserStore()

const formData = reactive({
  email: '',
  password: '',
  keepLoggedIn: false,
})

const submit = () => {
  if (validate()) {
    axios
      .post(
        '/api/auth/login',
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
        if (response.status === 200) {
          localStorage.setItem('email', formData.email)
          localStorage.setItem('access_token', response.data.access_token)
          localStorage.setItem('refresh_token', response.data.refresh_token)
          window.location.href = '/preferences'
        }
      })
      .catch((error) => {
        alert(error.response.data.detail)
      })
  }
}
</script>
