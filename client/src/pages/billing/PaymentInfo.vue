<template>
  <VaCard class="mb-6">
    <VaCardContent>
      <h2 class="page-sub-title">{{ t('payments.payment_info') }}</h2>

      <div class="flex items-center justify-between md:justify-items-stretch">
        <div
          class="flex grow flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-1 justify-between items-start md:items-center"
        >
          <div class="md:w-48">
            <p class="mb-1">{{ t('payments.payment_plan') }}</p>
            <p class="font-bold">
              {{ paymentPlan.isYearly ? paymentPlan.priceYear : paymentPlan.priceMonth }}&nbsp;/{{
                paymentPlan.isYearly ? t('billing.annual') : t('billing.monthly')
              }}
            </p>
          </div>
        </div>

        <div class="md:w-48 flex flex-col justify-end items-end">
          <VaButton preset="primary" @click="togglePaymentPlanModal">
            {{ t('billing_info.Switch to') }} {{ paymentPlan.isYearly ? t('billing.monthly') : t('billing.annual') }}
          </VaButton>

          <div v-if="!paymentPlan.isYearly" class="mt-2 text-regularSmall">
            <span>{{ paymentPlan.priceYear }}&nbsp;/ {{ t('billing.year') }}</span>
            <span class="text-danger ml-1">{{ t('billing_info.save') }} 16%</span>
          </div>
        </div>
      </div>

      <template v-if="paymentCard">
        <VaDivider />

        <div class="flex items-center justify-between md:justify-items-stretch">
          <div
            class="flex grow flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-1 justify-between items-start md:items-center"
          >
            <div class="md:w-48">
              <p class="mb-1">{{ t('billing_info.Payment method') }}</p>
              <p class="font-bold capitalize">{{ paymentCard.paymentSystem }} {{ paymentCard.cardNumberMasked }}</p>
            </div>
          </div>
          <div class="md:w-48 flex justify-end">
            <VaButton :to="{ name: 'payment-methods' }" preset="primary">{{ t('menu.payment-methods') }}</VaButton>
          </div>
        </div>
      </template>
    </VaCardContent>
  </VaCard>

  <ChangeYourPaymentPlan
    v-if="isChangeYourPaymentPlanModalOpen"
    :yearly-plan="paymentPlan.isYearly"
    @confirm="updatePaymentPlan"
    @cancel="togglePaymentPlanModal"
  />
</template>

<script lang="ts" setup>
import { computed, ref } from 'vue'
import { usePaymentCardsStore } from '../../stores/payment-cards'

import ChangeYourPaymentPlan from './modals/ChangeYourPaymentPlan.vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
const paymentPlan = ref({
  id: '1',
  name: 'Gold',
  isYearly: false,
  type: 'current',
  padletsUsed: 19,
  padletsTotal: '20',
  priceMonth: '$6.99',
  priceYear: '$69.99',
  switchToYearlySave: '16%',
  uploadLimit: '100MB',
})

const cardStore = usePaymentCardsStore()

const isChangeYourPaymentPlanModalOpen = ref(false)

const paymentCard = computed(() => cardStore.currentPaymentCard)
const togglePaymentPlanModal = () => {
  isChangeYourPaymentPlanModalOpen.value = !isChangeYourPaymentPlanModalOpen.value
}

const updatePaymentPlan = () => {
  paymentPlan.value.isYearly = !paymentPlan.value.isYearly
  isChangeYourPaymentPlanModalOpen.value = false
}
</script>
