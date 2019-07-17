hackaton = {}

hackaton.getWeather = function() {
    var cityName = $("#cityWeather").val();
        $.ajax({
            type: "GET",
            dataType: 'json',
            url: ("localhost/weather/" + cityName),
            success: function (response) {
                console.log(response)
            },
            error: function (msg) {
            },
            complete: function (response, status) {
            }
        })
}

$(".btn-success").click(hackaton.getWeather);