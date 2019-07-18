hackaton = {}

hackaton.getWeather = function() {
    var cityName = $("#cityWeather").val();
        $.ajax({
            type: "GET",
            crossDomain: true,
            url: ("/weather/" + cityName),
            
            success: function (response) {
                let span = $('.weather-conditions');
                span.append(`The weather condition in ${cityName} right now are: ${response}`)
            },
            error: function (msg) {
                console.log("error")
            },
            complete: function (response, status) {
                console.log("complete")
            }
        })
}

hackaton.routInfo = () => {


    let location = $(".current-location").val();
    let destination = $('.destination').val();
    let routeType = $('.choice-rout').val();

    let myData = {
        location: location,
        destination: destination,
        routeType: routeType
    }

    $.ajax({
        url: '/getdata',
        type: "POST",
        data: myData,
        dataType: "text",
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
$(".btn-primary").click(hackaton.routInfo)

