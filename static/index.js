hackaton = {}

hackaton.getWeather = function() {
    var cityName = $("#cityWeather").val();
    console.log(cityName)

        $.ajax({
            type: "GET",
            crossDomain: true,
            dataType: "json",
            url: (`http://api.openweathermap.org/data/2.5/weather?q=${cityName}&units=metric&APPID=fb0e6229d78973814f4cf193f2900387`),
            success: function (response) {
                let span = $('.weather-conditions');
                span.append(`The weather condition in ${cityName} right now are: ${response}`)
            },
            error: function (msg) {
            },
            complete: function (response, status) {
            }
        })
}

$(".btn-success").click(hackaton.getWeather);