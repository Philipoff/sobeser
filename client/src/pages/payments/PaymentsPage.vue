<template>
  <h1 class="page-title">{{ t('payments.payment_methods') }}</h1>

  <VaCard class="mb-6">
    <VaCardContent>
      <div class="text-2xl font-bold leading-5 mb-6">{{ t('payments.my_cards') }}</div>

      <PaymentCardList />
    </VaCardContent>
  </VaCard>

  <VaCard class="mb-6">
    <VaCardContent>
      <div class="text-2xl font-bold leading-5 mb-6">{{ t('payments.billing_address') }}</div>

      <BillingAddressList />
    </VaCardContent>
  </VaCard>
</template>

<script lang="ts" setup>
import PaymentCardList from './widgets/my-cards/PaymentCardList.vue'
import BillingAddressList from './widgets/billing-address/BillingAddressList.vue'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
</script>
