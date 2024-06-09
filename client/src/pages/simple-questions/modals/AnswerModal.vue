<template>
  <VaModal
    :mobile-fullscreen="false"
    size="large"
    hide-default-actions
    model-value
    @update:modelValue="emits('cancel')"
  >
    <VaTextarea :autosize="true" :readonly="true" style="width: 100%" v-html="marked.parse(props.answer)"></VaTextarea>
  </VaModal>
</template>
<script lang="ts" setup>
import { marked } from 'marked'

const props = defineProps({
  answer: String,
})

const emits = defineEmits(['cancel'])
</script>
