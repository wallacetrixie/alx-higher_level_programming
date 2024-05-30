$(document).ready(function(){
    // Make an AJAX request to fetch data from the SWAPI
    $.ajax({
        url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
        method: "GET",
        success: function(data){
            // Extract the character name from the response
            var characterName = data.name;
            // Display the character name in the div with id "character"
            $("#character").text(characterName);
        },
        error: function(){
            // Display an error message if the request fails
            $("#character").text("Error fetching character data");
        }
    });
});

