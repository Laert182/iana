axios.post('http://localhost:5000/', {text: 'Hello, how are you doing today? I hope everything is going well.'})
  .then(function (response) {
    console.log(response.data.preprocessed_text);
  })
  .catch(function (error) {
    console.log(error);
  });
