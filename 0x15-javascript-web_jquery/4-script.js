$(document).ready(function(){
    // When the user clicks on the div with id "toggle_header"
    $("#toggle_header").click(function(){
        // Toggle the class "red" and "green" on the header element
        $("header").toggleClass("red green");
    });
});

