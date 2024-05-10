<template>
  <div>
    {{ question }}
  </div>
  <input v-model="answer" />
  <button @click="send_answer">Отправить</button>
  {{ response }}
</template>

<script>
import axios from 'axios'

export default {
  name: 'ExamPage',
  data() {
    return {
      question:
        'What approach can you employ to efficiently determine the Longest Common Subsequence (LCS) of two given strings in Python, emphasizing optimization of execution time and leveraging dynamic programming principles?',
      answer:
        'To determine the Longest Common Subsequence (LCS) of two strings in Python, one can utilize a greedy search algorithm. This algorithm iteratively selects the largest common character in both strings and adds it to the LCS. However, this approach may not always yield the correct result since it does not consider all possible combinations of characters in the strings',
      response: '',
    }
  },
  methods: {
    send_answer() {
      axios
        .post(
          '/api/check_answer',
          {
            question: String(this.question),
            answer: String(this.answer),
          },
          {
            headers: {
              Accept: 'application/json',
              'Content-Type': 'application/json',
            },
          },
        )
        .then((response) => (this.response = response.data))
    },
  },
}
</script>

<style scoped></style>
