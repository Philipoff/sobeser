<template>
  <h1 class="page-title">{{ t('questions.Questions') }}</h1>
  <h3 class="page-sub-title">{{ t('questions.Help') }}</h3>

  <div v-for="question in questions">
    <div
      class="flex mb-4 flex-col p-4 space-y-10 bg-backgroundSecondary rounded-lg"
      @click="isEditNameModalOpen = true;
              clicked_question = question['answer'];"
    >
      <VaTextarea v-model="question['question']" autosize readonly></VaTextarea>
    </div>
  </div>
  <AnswerModal v-if="isEditNameModalOpen" v-model:answer="clicked_question" @cancel="isEditNameModalOpen = false"/>
</template>
<script lang="ts" setup>
import AnswerModal from './modals/AnswerModal.vue'

import questions from '../../data/pages/python-simple-questions.json'
import {ref} from 'vue'
import {useI18n} from 'vue-i18n'

const {t} = useI18n()
let isEditNameModalOpen = ref(false)
let clicked_question = ''
</script>
