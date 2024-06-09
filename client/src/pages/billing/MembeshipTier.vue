<template>
  <VaCard class="mb-6">
    <VaCardContent>
      <h2 class="page-sub-title">Membership tier</h2>
      <template v-for="(plan, index) in plans" :key="plan.id">
        <div class="flex items-center justify-between md:justify-items-stretch">
          <div
            class="flex grow flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-1 justify-between items-start md:items-center"
          >
            <div class="flex items-center md:w-48">
              <div class="font-bold">{{ t('billing.' + plan.name) }}</div>
              <VaBadge v-if="plan.type === 'current'" class="ml-2" color="success" :text="t('current')" />
            </div>
            <div class="md:w-48">
              <template v-if="plan.priceMonth">
                <p class="mb-1">{{ t('billing.' + plan.priceMonth)  + ' / ' + t('billing.month') }}</p>
                <p>{{ t('billing.' + plan.priceYear) + ' / ' + t('billing.year') }}</p>
              </template>
              <p v-else>Free</p>
            </div>
          </div>
          <div class="md:w-48 flex justify-end">
            <div v-if="plan.type === 'current'" class="font-bold">{{ t('selected') }}</div>
            <VaButton v-else @click="switchPlan(plan.id)">{{ t('select') }}</VaButton>
          </div>
        </div>

        <VaDivider v-if="index !== plans.length - 1" />
      </template>
    </VaCardContent>
  </VaCard>
</template>

<script lang="ts" setup>
import { useToast } from 'vuestic-ui'
import { reactive } from 'vue'
import {useI18n} from "vue-i18n";

const { init } = useToast()
const { t } = useI18n()

type MembershipTier = {
  id: string
  name: string
  type: 'upgrade' | 'downgrade' | 'current'
  padletsUsed: number
  padletsTotal: string
  priceMonth?: string
  priceYear?: string
  uploadLimit: string
}

const plans = reactive<MembershipTier[]>([
  {
    id: '1',
    name: 'Startup',
    type: 'upgrade',
    padletsUsed: 0,
    padletsTotal: 'Unlimited',
    priceMonth: 'price_month_startup',
    priceYear: 'price_year_startup',
    uploadLimit: '500MB',
  },
  {
    id: '2',
    name: 'Advanced',
    type: 'current',
    padletsUsed: 19,
    padletsTotal: '20',
    priceMonth: 'price_month_advanced',
    priceYear: 'price_year_advanced',
    uploadLimit: '100MB',
  },
  {
    id: '3',
    name: 'Enterprise',
    type: 'downgrade',
    padletsUsed: 0,
    padletsTotal: '3',
    priceMonth: "price_month_enterprise",
    priceYear: "price_year_enterprise",
    uploadLimit: '20MB',
  },
])

const switchPlan = (planId: string) => {
  plans.forEach((item, index) => {
    if (item.id === planId) {
      // Set the selected plan to 'current'
      item.type = 'current'
    } else {
      // Determine if other plans are an 'upgrade' or 'downgrade'
      const selectedIndex = plans.findIndex((plan) => plan.id === planId)
      item.type = index < selectedIndex ? 'upgrade' : 'downgrade'
    }
  })
  init({
    message: "You've successfully changed the membership tier",
    color: 'success',
  })
}
</script>
