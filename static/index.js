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

hackaton.routInfo = (e) => {
    e.preventDefault();
    console.log(e)

    let location = $(".current-location").val();
    let destination = $('.destination').val();
    let routeType = $('.choice-rout').val();

        const myData = {
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
            console.log(JSON.parse(response))
            let map = $(".mymap");
            map[0].src = `https://www.google.com/maps/embed/v1/directions?key=AIzaSyB1SlyO9n2uirPXWqL9O6k0k0Gx74Sqs6s&mode=walking&origin=${location}&destination=${destination}&waypoints=${JSON.parse(response).join("|")}`
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
//$(".btn-primary").click(hackaton.routInfo(e))
document.querySelector(".btn-primary").addEventListener('click', (e) => {
    hackaton.routInfo(e)
})

