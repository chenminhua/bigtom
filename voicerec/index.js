const btn = document.querySelector('.talk');
const content = document.querySelector('.content');
var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
const recognition = new SpeechRecognition();

btn.addEventListener('click', () => {
  recognition.start();
});

recognition.onstart = function() {
  console.log('you can speak');
};

recognition.onend = function() {
  console.log('you can stop');
};

recognition.onerror = function(event) {
  console.log('wtf');
};

recognition.onresult = function(event) {
  const current = event.resultIndex;
  const transcript = event.results[current][0].transcript;
  content.textContent = transcript;
  readOutLoud(transcript);
};

function readOutLoud(message) {
  const speech = new SpeechSynthesisUtterance();
  speech.volume = 1;
  speech.rate = 1;
  speech.pitch = 1;
  speech.text = message;
  window.speechSynthesis.speak(speech);
}
