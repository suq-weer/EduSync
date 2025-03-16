import { defineStore } from 'pinia'

export const accountStates = defineStore('account', {
  state: () => {
    return {
      power: ''
    }
  },
  actions: {
    setPower(power: string) {
      this.power = power
    }
  }
})