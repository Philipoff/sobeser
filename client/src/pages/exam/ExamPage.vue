<template>
  <div>
    {{ question }}
  </div>
<input v-model="answer">
  <button @click="send_answer">

  </button>
</template>

<script>
import axios from "axios";

export default {
  name: "ExamPage",
  data() {
    return {
      question: "What is my name?",
      answer: "Python"
    }
  },
  methods: {
    send_answer() {
      axios.post("/api/check_answer", {
          "question": question,
          "answer": answer,
        }, {
          headers: {
            'Accept':
              'application/json',
            'Content-Type':
              'application/json'
          }
        }
      ).then((response) => this.user = response.data)
    }
  }

}
</script>

<style scoped>

</style>
