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
                windSpeed = data.interia_wind_speed_km_h;
                interiaTemp = data.interia_temperature;
                humidity = data.humidity_in_percentage;
                rainPrecipitation = data.rain_precipitation_percentage;
                lastHourTemp = parseFloat(data.last_hour_data.temp);
                lastHourTime = data.last_hour_data.time;
                lastHourTime = lastHourTime.slice(0, 5);
                secondLastHourTemp = parseFloat(data.last_second_hour_data.temp);

                if (interiaTemp < 15) {
                    score = "🧊🥶";
                } else if (interiaTemp > 30) {
                    score = "🥵"
                } else {
                    score = "🌡️😎";
                }
                

                const { day, dayDigit, month } = get_date();

                const pressureDiv = document.getElementById("pressure");
                pressureDiv.textContent = `🔵Pressure: ${pressure} hPa`;

                const sunriseDiv = document.getElementById("sunrise");
                sunriseDiv.textContent = `🌅 Sunrise: ${sunrise} AM`;

                const sunsetDiv = document.getElementById("sunset");
                sunsetDiv.textContent = `🌇 Sunset: ${sunset} PM`;

                const windSpeedDiv = document.getElementById("windSpeed");
                windSpeedDiv.textContent = `💨 Wind Speed: ${windSpeed} km/h`;
    
                const temperatureDiv = document.getElementById("temperature");
                temperatureDiv.textContent = `${score} Temperature: ${interiaTemp}°C`;

                const humidityDiv = document.getElementById("humidity");
                humidityDiv.textContent = `💧 Humidity: ${humidity}%`;

                const precipitationDiv = document.getElementById("rain_precipitation");
                precipitationDiv.textContent = `☔ Chance of precipitation: ${rainPrecipitation}%`;

                const lastHourTempDiv = document.getElementById("hour");
                lastHourTempDiv.textContent = `x${lastHourTime} ☀️ ${lastHourTemp}°C - ☔ ${rainPrecipitation}%`;
            }
        })

        .catch(error => {
            console.log("there is error", error);
        })
}

setInterval(get_api, 600000);
get_api();

function get_date() {
    const weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

    const d = new Date();
    const day = weekday[d.getDay()];
    const dayDigit = d.getDate();
    const month = months[d.getMonth()];

    return { day, dayDigit, month };
}


function display_date() {
    
    const { day, dayDigit, month } = get_date();
 
    const dateDiv = document.getElementById("date");
    dateDiv.textContent = `📅 ${day}, ${dayDigit} ${month}`;
}

setInterval(display_date, 86400000);
display_date();


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


