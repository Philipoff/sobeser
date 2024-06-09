<template>
  <VaCard class="mb-4">
    <VaCardContent>
      <h2 class="va-h5">{{ t('faq.questions.popular_questions') }}</h2>
      <VaAccordion v-model="accordionState" :style="{ '--va-collapse-padding': '1rem 0' }" class="mb-1">
        <VaCollapse :header="t('faq.questions.reload_page_q')">
          <article class="max-w-3xl leading-5">
            <p class="mb-2">
              {{ t('faq.questions.reload_page_a1') }}
            </p>
            <ul class="list-disc list-inside leading-5 ml-4">
              <li>
                {{ t('faq.questions.reload_page_a2') }}
              </li>
              <li>
                {{ t('faq.questions.reload_page_a3') }}
              </li>
              <li>{{ t('faq.questions.reload_page_a4') }}</li>
            </ul>
          </article>
        </VaCollapse>

        <VaCollapse :header="t('faq.questions.return_policy_q')">
          <article class="max-w-3xl leading-5">
            <p class="mb-2">
              {{ t('faq.questions.return_policy_a') }}
            </p>
          </article>
        </VaCollapse>

        <VaCollapse :header="t('faq.questions.how_to_use_q')">
          <article class="max-w-3xl leading-5">
            <p class="mb-2">
              {{ t('faq.questions.how_to_use_a') }}
            </p>
          </article>
        </VaCollapse>

        <VaCollapse :header="t('faq.questions.contact_q')">
          <article class="max-w-3xl leading-5">
            <p class="mb-2">
              {{ t('faq.questions.contact_a') }}
            </p>
          </article>
        </VaCollapse>
      </VaAccordion>
    </VaCardContent>
  </VaCard>
</template>

<script setup>
import { reactive } from 'vue'
import { useI18n } from 'vue-i18n'

const accordionState = reactive([false, false, false, false])
const { t } = useI18n()
</script>
