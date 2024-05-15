<template>
  <div>
    <h2 style="font-size: 1.5rem" class="leading-8">
      Question: {{ question }}
    </h2>
  </div>
  <br>
  <h2>
    Answer:
  </h2>
  <div>
    <VaTextarea rows="10" class="w-full text-lg rounded-lg border" v-model="answer" />
    <VaButton type="button" class="mt-2 float-right right-10" size="large" @click="send_answer" color="success" gradient>Отправить</VaButton>
  </div>
  <div class="mt-12">
    <h2 class="mt-2">
      Corrections:
    </h2>
    <VaTextarea rows="10" class="w-full text-lg rounded-lg border" disabled v-model="response" />
  </div>
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
      this.response = "fasfaskbhkvbkzjsvbkasufkayufjkdabksdjaskyufbaksdbkasjdhfbkhjfbkajh kjd fhbakds hbfakjhfbkasjh dksjh vfkajdvksv asjdhvf aksdhvf khf kfvk sbflakjbbsldiabdskjfbsj"
      // axios
      //   .post(
      //     '/api/check_answer',
      //     {
      //       question: String(this.question),
      //       answer: String(this.answer),
      //     },
      //     {
      //       headers: {
      //         Accept: 'application/json',
      //         'Content-Type': 'application/json',
      //       },
      //     },
      //   )
      //   .then((response) => (this.response = response.data))
    },
  },
}
</script>

<style scoped></style>
