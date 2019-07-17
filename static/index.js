hackaton = {}

hackaton.getWeather = function() {
    var cityName = $("#cityWeather").val();
    console.log(cityName)

    // $.get("localhost:8080/weather/" + cityName,
    //  function(data, status){
    //     alert("Data: " + data + "\nStatus: " + status);
    //   });

        $.ajax({
            type: "GET",
            crossDomain: true,
            dataType: "json",
            url: ("localhost:8080/weather/" + cityName),
            
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