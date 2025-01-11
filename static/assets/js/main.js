$("#navbarToggler").on("click", function(){
    $("#navbarNav").slideDown("slow");
    $("#navbarToggler").hide();
    $("#navbarCross").show();
    $(".navbar-brand").hide();
});

$(document).ready(function() {
    $("#navbarCross").click(function() {
        $("#navbarNav").hide();
        $("#navbarToggler").show();
        $("#navbarCross").hide();
        $(".navbar-brand").show();
    });
});


$(document).ready(function() {
    let counter = 0;
    function handleVisibility() {
        console.log(counter)
        if ($(window).width() < 995) {
            if (counter == 0){
                counter += 1;
                $("#navbarToggler").show();
                $("#navbarNav").hide();
                $("#navbarCross").hide();
            }  
        } else {
            counter = 0
            $("#navbarNav").show();
            $("#navbarCross").hide();
            $(".navbar-brand").show();
        }
    }
    handleVisibility();

    $(window).resize(function() {
        handleVisibility();
    });
});

// Notifications
