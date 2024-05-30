$(document).ready(function(){
    // Make an AJAX request to fetch data from the API
    $.ajax({
        url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
        method: "GET",
        success: function(data){
            // Display the translation of "hello" in the div with id "hello"
            $("#hello").text(data.hello);
        },
        error: function(){
            // Display an error message if the request fails
            $("#hello").text("Error fetching translation");
        }
    });
});

