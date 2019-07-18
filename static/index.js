hackaton = {}

hackaton.getWeather = function() {
    var cityName = $("#cityWeather").val();
        $.ajax({
            type: "GET",
            crossDomain: true,
            url: ("/weather/" + cityName),
            
            success: function (response) {
                console.log(response)
            },
            error: function (msg) {
                console.log("error")
            },
            complete: function (response, status) {
                console.log("complete")
            }
        })
}

$(".btn-success").click(hackaton.getWeather);