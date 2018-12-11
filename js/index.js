let getTopics = function() {
  return fetch('/topic')
           .then(res => res.json())
           .then(data => data.topics);
};

let app = new Vue({
  el: '#app',
  data: {
    topics: []
  },
  created: function() {
    getTopics().then(topics => this.topics = topics);
  },
  methods: {}
});
