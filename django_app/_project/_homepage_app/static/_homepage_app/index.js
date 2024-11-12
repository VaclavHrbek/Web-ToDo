const { createApp, ref } = Vue

createApp({
  delimiters: ['[[', ']]'],
  setup() {
    const message = ref('Hello Vue!')
    const button = ref('Hello button!')

    return {
      message, 
      button
    }
  }
}).mount('#app')