import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => {
    return {
      email: '',
      memberSince: '8/12/2020',
    }
  },
  //
  // getters: {
  //   get_email(state) {
  //     console.log(state)
  //     return state.email
  //   }
  // },
  //
  // actions: {
  //   changeEmail(email: string) {
  //     this.email = email
  //   },
  // },
})
