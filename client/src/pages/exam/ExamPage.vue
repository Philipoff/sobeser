<template>
  <div>
    <h2 style="font-size: 1.5rem" class="leading-8">{{ t('exam.Question') }}: {{ requestData.question }}</h2>
  </div>
  <br />
  <h2>{{ t('exam.Answer') }}:</h2>
  <div>
    <VaTextarea v-model="requestData.answer" rows="10" class="w-full text-lg rounded-lg border" />
    <VaButton
      type="button"
      class="mt-2 float-right right-10"
      size="large"
      color="success"
      gradient
      :disabled="status.isSubmitting"
      @click="send_answer"
    >
      {{ t('exam.Send') }}
    </VaButton>
  </div>
  <div class="mt-12">
    <h2 class="mt-2">{{ t('exam.Corrections') }}:</h2>
    <VaTextarea
      class="p-2 m-2 w-full text-lg rounded-lg border"
      :autosize="true"
      :readonly="true"
      style="width: 100%"
      v-html="marked.parse(responseData.response)"
    ></VaTextarea>
  </div>
</template>

<script lang="ts" setup>
import { useI18n } from 'vue-i18n'
import { reactive } from 'vue'
import axios from 'axios'
import { marked } from 'marked'

import questions from '../../data/pages/python-simple-questions.json'

const { t } = useI18n()
const status = reactive({
  isSubmitting: false,
})

const requestData = reactive({
  question: questions[Math.floor(Math.random() * questions.length)]['question'],
  answer: '',
})

const responseData = reactive({
  response: '',
})

const send_answer = () => {
  status.isSubmitting = true
  axios
    .post(
      '/api/answer_processing/check_answer',
      {
        question: String(requestData.question),
        answer: String(requestData.answer),
      },
      {
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
      },
    )
    .then((res) => {
      responseData.response = res.data
      status.isSubmitting = false
    })
}

// function getStatus(taskID) {
//   axios.get(`/api/answer_processing/tasks/${taskID}`, {
//     method: 'GET',
//     headers: {
//       'Content-Type': 'application/json'
//     },
//   })
//     .then(res => {
//       console.log(res)
//       console.log(res.data)
//       let taskStatus = res.data.task_id
//       if (taskStatus === 'finished' || taskStatus === 'failed') return false;
//       setTimeout(function () {
//         getStatus(res.data.task_id);
//       }, 1000);
//     })
//     .catch(err => console.log(err));
// }
</script>

<style scoped></style>
