const { createApp, ref } = Vue

createApp({
  delimiters: ['[[', ']]'],
  setup() {
    const message = ref('Hello Vue!')
    const button = ref('Hello button!')
    const toDoButtonHelpMessage = ref('Go to the To Do app')

    return {
      message, 
      button
    }
  },
  template:
  `
  <div>
  <p>[[ message ]]</p>
  </div>
  `
}).mount('#app')