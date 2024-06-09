export type PricingPlans = {
  title: string
  model: string
  badges?: string[]
  description: string
  price: string
  priceMonth: string
  features: Feature[]
}

type Feature = {
  description: string
  isAvailable: boolean
}

const features = ['feature_1', 'feature_2', 'feature_3', 'feature_4', 'feature_5', 'feature_6', 'feature_7']

export const pricingPlans: PricingPlans[] = [
  {
    title: 'Startup',
    model: 'Startup',
    description: 'startup',
    price: 'price_year_startup',
    priceMonth: 'price_month_startup',
    features: features.map((d, i) => ({ description: d, isAvailable: i < 3 })),
  },
  {
    title: 'Advanced',
    model: 'Advanced',
    description: 'advanced',
    price: 'price_year_advanced',
    priceMonth: 'price_month_advanced',
    features: features.map((d, i) => ({ description: d, isAvailable: i < 5 })),
  },
  {
    title: 'Enterprise',
    model: 'Enterprise',
    description: 'enterprise',
    price: 'price_year_enterprise',
    priceMonth: 'price_month_enterprise',
    features: features.map((d) => ({ description: d, isAvailable: true })),
  },
]
