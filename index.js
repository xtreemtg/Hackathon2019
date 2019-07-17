
let myPlace = $(".temperature-query"); 

$(".btn-success").click(function () {
    $.ajax({
        type: "GET",
        url: `weather/<${myPlace.val()}>`,
    }).done((data) => {
    });
})
