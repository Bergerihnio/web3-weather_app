function get_api() {
    fetch('http://192.168.178.44:5000/data')
        .then(response => {
            return response.json(); 
        })
        .then(data => {
            if ("temperature" in data) {
                temperature = parseFloat(data.temperature);
                pressure = parseFloat(data.interia_pressure_hPa);
                sunrise = data.interia_sunrise_time;
                sunset = data.interia_sunset_time;
                wind_speed = data.interia_wind_speed_km_h;
                interia_temp = data.interia_temperature;
                humidity = data.humidity;


                if (interia_temp < 15) {
                    score = "🧊🥶";
                } else if (interia_temp > 30) {
                    score = "🥵"
                } else {
                    score = "🌡️😎";
                }
                
                const pressureDiv = document.getElementById("pressure");
                pressureDiv.textContent = `🔵Pressure: ${pressure} hPa`;

                const sunriseDiv = document.getElementById("sunrise");
                sunriseDiv.textContent = `🌅 Sunrise: ${sunrise} AM`;

                const sunsetDiv = document.getElementById("sunset");
                sunsetDiv.textContent = `🌇 Sunset: ${sunset} PM`;

                const wind_speedDiv = document.getElementById("wind_speed");
                wind_speedDiv.textContent = `💨 Wind Speed: ${wind_speed}km/h`;
    
                const temperatureDiv = document.getElementById("temperature");
                temperatureDiv.textContent = `${score} Temperature: ${interia_temp}°C`;

                const humidityDiv = document.getElementById("humidity");
                humidityDiv.textContent = `💧 Humidity: ${humidity}`;
            }
        })

        .catch(error => {
            console.log("there is error", error);
        })
}

setInterval(get_api, 600000);
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


