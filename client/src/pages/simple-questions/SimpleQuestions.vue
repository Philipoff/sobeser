<template>
  <div v-for="question in questions">
    {{ question['question'] }}
    <br>
    <br>
    <br>
    {{ question['answer'] }}
  </div>
</template>
<script lang="ts" setup>
import {ref} from 'vue'
import questions from '../../data/pages/python-simple-questions.json'
</script>
