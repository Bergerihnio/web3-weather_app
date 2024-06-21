function get_api() {
    fetch("http://bergerihnio.ddns.net/data")
        .then(response => {
            return response.json(); 
        })
        .then(data => {
            if ("temperature" in data[0]) {
                temperature = data[0].temperature
            
                if (temperature < 15) {
                    score = "🧊🥶";
                } else if (temperature > 30) {
                    score = "🥵" // ethnuil city
                } else {
                    score = "🌡️😎";
                }

                const temperatureDiv = document.getElementById("temperature");
                temperatureDiv.textContent = `${score} Temperature: ${temperature}°C`;
            }
        })

        .catch(error => {
            console.log("there is error", error);
        })
}

setInterval(get_api, 60000);
get_api();


function get_date() {
    const weekday = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
    const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

    const d = new Date();
    let day = weekday[d.getDay()];

    let dayDigit = d.getDate();

    let month = months[d.getMonth()];
 
    const dateDiv = document.getElementById("date");
    dateDiv.textContent = `📅 ${day}, ${dayDigit} ${month}`;
}

setInterval(get_date, 86400000);
get_date();


function get_time() {
    const d = new Date()
    let minutes = d.getMinutes();
    let hours = d.getHours();

    hours = hours < 10 ? `0${hours}` : hours;
    minutes = minutes < 10 ? `0${minutes}` : minutes;

    const timeDiv = document.getElementById("time");
    timeDiv.textContent = `🕘 ${hours}:${minutes}`;
}

setInterval(get_time, 60000);
get_time();
