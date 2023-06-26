
async function data() {
  // Retrieve data from Python function
  const response = await eel.hello_from_python("narmeen")();

  // Display the response in the console
  console.log(response);
}

// Add event listener to the "playButton" element
document.getElementById("playButton").addEventListener('click', data);
