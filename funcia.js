// Envia mensagem para o servidor Flask e recebe a resposta
function sendMessage() {
    let message = document.getElementById('user-input').value;
  
    // Envia mensagem para o servidor Flask
    axios.post('http://localhost:5000/', {text: message})
      .then(function (response) {
        // Recebe a mensagem pré-processada do servidor e exibe no chat
        displayMessage(message);
        displayBotMessage(response.data.preprocessed_text);
      })
      .catch(function (error) {
        console.log(error);
      });
  
    // Limpa o campo de entrada
    document.getElementById('user-input').value = '';
  }
  
  // Exibe mensagem do usuário no chat
  function displayMessage(message) {
    let chatBox = document.querySelector('.chat-box');
    let userMessage = `
      <div class="chat-message">
        <p class="user-message">${message}</p>
      </div>
    `;
    chatBox.insertAdjacentHTML('beforeend', userMessage);
  }
  
  // Exibe mensagem do bot no chat
  function displayBotMessage(message) {
    let chatBox = document.querySelector('.chat-box');
    let botMessage = `
      <div class="chat-message">
        <p class="bot-message">${message}</p>
      </div>
    `;
    chatBox.insertAdjacentHTML('beforeend', botMessage);
  }
  