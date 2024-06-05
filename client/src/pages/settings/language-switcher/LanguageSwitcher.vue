<template>
  <div class="flex items-center justify-between">
    <p>{{ t('settings.Language') }}</p>
    <div class="w-40">
      <VaSelect v-model="model" :options="options" />
    </div>
  </div>
</template>
<script lang="ts" setup>
import { computed } from 'vue'

import { useI18n } from 'vue-i18n'

type LanguageMap = Record<string, string>

const { locale } = useI18n()
const { t } = useI18n()

const languages: LanguageMap = {
  english: 'English',
  russian: 'Русский',
}

const languageCodes: LanguageMap = {
  gb: languages.english,
  ru: languages.russian,
}

const languageName: LanguageMap = Object.fromEntries(Object.entries(languageCodes).map(([key, value]) => [value, key]))

const options = Object.values(languageCodes)

const model = computed({
  get() {
    if (localStorage.getItem("language")) {
      locale.value = localStorage.getItem("language")
      return languageCodes[localStorage.getItem("language")]
    }
    return languageCodes[locale.value]
    },
  set(value) {
    locale.value = languageName[value]
    localStorage.setItem("language", languageName[value])
  },
})
</script>
