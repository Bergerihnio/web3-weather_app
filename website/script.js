const getOldWeather = (oldWeatherData) => ({
    temp: parseFloat(oldWeatherData.temp),
    time: oldWeatherData.time.slice(0,5),
    rain: oldWeatherData.rain,
    emoji: oldWeatherData.emoji
})

const getMedianTempData = (medianTempData) => ({
    date: medianTempData.date.slice(8, 11),
    median_temp: parseFloat(medianTempData.median_temp),
    month: medianTempData.month,
    day: medianTempData.day,
    median_emoji: medianTempData.median_emoji
})

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
                emoji = data.emoji

                const oldWeather = {
                    oneHourBack: getOldWeather(data.last_hour_data),
                    twoHoursBack: getOldWeather(data.last_second_hour_data),
                    fourHoursBack: getOldWeather(data.last_fourth_hour_data),
                    sevenHoursBack: getOldWeather(data.last_seventh_hour_data),
                    tenHoursBack: getOldWeather(data.last_10th_hour_data),
                    thirteenHoursBack: getOldWeather(data.last_13th_hour_data)
                }

                const medianTempData = {
                    lastMedian: getMedianTempData(data.last_median_temp),
                    lastSecondMedian: getMedianTempData(data.last_second_median_temp),
                    lastThirdMedian: getMedianTempData(data.last_third_median_temp),
                    lastFourthMedian: getMedianTempData(data.last_fourth_median_temp),
                    lastFifthMedian: getMedianTempData(data.last_fifth_median_temp)
                }

                

                if (interiaTemp < 15) {
                    score = ""//🧊🥶";
                } else if (interiaTemp > 30) {
                    score = ""// "🥵"
                } else {
                    score = ""//"🌡️😎";
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
                temperatureDiv.textContent = `${emoji}${score} Temperature ${interiaTemp}°C`;

                const humidityDiv = document.getElementById("humidity");
                humidityDiv.textContent = `💧 Humidity: ${humidity}%`;

                const precipitationDiv = document.getElementById("rain_precipitation");
                precipitationDiv.textContent = `☔ Chance of precipitation: ${rainPrecipitation}%`;

                const lastHourTempDiv = document.getElementById("hour");
                lastHourTempDiv.textContent = `${oldWeather.oneHourBack.time} ${oldWeather.oneHourBack.emoji} ${oldWeather.oneHourBack.temp}°C - ☔ ${oldWeather.oneHourBack.rain}%`;

                const fourthLastHourTempDiv = document.getElementById("fourth_hour");
                fourthLastHourTempDiv.textContent = `${oldWeather.fourHoursBack.time} ${oldWeather.fourHoursBack.emoji} ${oldWeather.fourHoursBack.temp}°C - ☔ ${oldWeather.fourHoursBack.rain}%`;

                const seventhLastHourTempDiv = document.getElementById("seventh_hour");
                seventhLastHourTempDiv.textContent = `${oldWeather.sevenHoursBack.time} ${oldWeather.sevenHoursBack.emoji} ${oldWeather.sevenHoursBack.temp}°C - ☔ ${oldWeather.sevenHoursBack.rain}%`;

                const tenHoursBackTempDiv = document.getElementById("tenth_hour");
                tenHoursBackTempDiv.textContent = `${oldWeather.tenHoursBack.time} ${oldWeather.tenHoursBack.emoji} ${oldWeather.tenHoursBack.temp}°C - ☔ ${oldWeather.tenHoursBack.rain}%`;

                const thirteenHoursBackTempDiv = document.getElementById("thirteen_hour");
                thirteenHoursBackTempDiv.textContent = `${oldWeather.thirteenHoursBack.time} ${oldWeather.thirteenHoursBack.emoji} ${oldWeather.thirteenHoursBack.temp}°C - ☔ ${oldWeather.thirteenHoursBack.rain}%`;

                const lastMedianDiv = document.getElementById("day");
                lastMedianDiv.textContent = `${medianTempData.lastMedian.median_emoji} ${medianTempData.lastMedian.day}, ${medianTempData.lastMedian.date} ${medianTempData.lastMedian.month} ${medianTempData.lastMedian.median_temp}°C`;

                const lastSecondMedianDiv = document.getElementById("last_day");
                lastSecondMedianDiv.textContent = `${medianTempData.lastSecondMedian.median_emoji} ${medianTempData.lastSecondMedian.day}, ${medianTempData.lastSecondMedian.date} ${medianTempData.lastSecondMedian.month} ${medianTempData.lastSecondMedian.median_temp}°C`;

                const lastThirdMedianDiv = document.getElementById("second_last_day");
                lastThirdMedianDiv.textContent = `${medianTempData.lastThirdMedian.median_emoji} ${medianTempData.lastThirdMedian.day}, ${medianTempData.lastThirdMedian.date} ${medianTempData.lastThirdMedian.month} ${medianTempData.lastThirdMedian.median_temp}°C`;

                const lastFourthMedianDiv = document.getElementById("third_last_day");
                lastFourthMedianDiv.textContent = `${medianTempData.lastFourthMedian.median_emoji} ${medianTempData.lastFourthMedian.day}, ${medianTempData.lastFourthMedian.date} ${medianTempData.lastFourthMedian.month} ${medianTempData.lastFourthMedian.median_temp}°C`;

                const lastFifthMedianDiv = document.getElementById("fourth_last_day");
                lastFifthMedianDiv.textContent = `${medianTempData.lastFifthMedian.median_emoji} ${medianTempData.lastFifthMedian.day}, ${medianTempData.lastFifthMedian.date} ${medianTempData.lastFifthMedian.month} ${medianTempData.lastFifthMedian.median_temp}°C`;
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


