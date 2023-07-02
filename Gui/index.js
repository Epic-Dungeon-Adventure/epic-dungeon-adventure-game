
async function data(event) {
  // const game_name = code for finding game name
  window.close();
  const response = await eel.chose_game(event.srcElement.value)();
}

// Add event listener to the "playButton" element
document.getElementById("playButton").addEventListener('click', data);
