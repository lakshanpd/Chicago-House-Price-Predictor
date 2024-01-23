let inputForm = document.getElementById("input_form");

inputForm.addEventListener("submit", (e) => {
  e.preventDefault();

  let bedroom = document.getElementById("bedroom").value;
  let space = document.getElementById("space").value;
  let room = document.getElementById("room").value;
  let bathroom = document.getElementById("bathroom").value;
  let garage = document.getElementById("garage").value;
  let condition = document.getElementById("condition").value;

// Create an object with the data
let data = {
    "Bedroom": bedroom,
    "Space": space,
    "Room": room,
    "Bathroom": bathroom,
    "Garage": garage,
    "Condition": condition
  };

  console.log(data)
  
  // Send the data to the backend using fetch
  fetch('http://127.0.0.1:5001/predict_home_price', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
    .then(response => response.json())
    .then(result => {
      // Handle the response from the backend
      console.log(result);
      document.getElementById("output").innerText = `Estimated Price: ${result.estimated_price}`;
    })
    .catch(error => {
      console.error('Error:', error);
    });


});