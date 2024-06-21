
// function get_api() {
//     fetch("http://192.168.1.78:8000/data")
//         .then(response => {
//             return response.json(); 
//         })
//         .then(data => {
//             if ("temperature" in data[0]) {
//                 temperature = data[0].temperature
//                 // console.log(temperature)
                
//                 if (temperature < 15) {
//                     score = "🧊🥶";
//                 } else if (temperature > 30) {
//                     score = "🥵" // ethnuil city
//                 } else {
//                     score = "🌡️😎";
//                 }

//                 const temperatureDiv = document.getElementById("temperature");
//                 temperatureDiv.textContent = `${score} Temperatura: ${temperature}°C`;
//             }
//         })

//         .catch(error => {
//             console.log("there is error", error);
//         })
// }

// get_api()