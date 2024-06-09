<template>
  <h1 class="page-title">{{ t('faq.how_to_help') }}</h1>
  <Categories />
  <Questions />
  <Navigation />
</template>

<script setup>
import Categories from './widgets/Categories.vue'
import Questions from './widgets/Questions.vue'
import Navigation from './widgets/Navigation.vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
</script>
