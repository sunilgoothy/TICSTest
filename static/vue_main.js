Vue.component('colored-box', {
  template: "<div class=\"box\"> - </div>"
})

const vueApp = new Vue({
  el: '#vapp',
  data: { 
  display: 'redbox' 
  }
})