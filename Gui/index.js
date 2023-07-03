
async function data(event) {
  window.close();
  const response = await eel.chose_game(event.srcElement.value)();
}

play_buttons = document.getElementsByClassName("play")

for (var i = 0; i < play_buttons.length; i++) {
  play_buttons[i].addEventListener('click', data);
}