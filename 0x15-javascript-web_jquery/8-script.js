$(document).ready(function(){
    // Make an AJAX request to fetch data from the SWAPI
    $.ajax({
        url: "https://swapi-api.alx-tools.com/api/films/?format=json",
        method: "GET",
        success: function(data){
            // Loop through the results to extract movie titles
            data.results.forEach(function(movie){
                // Create a new list item for each movie title
                var listItem = $("<li>").text(movie.title);
                // Append the list item to the UL with id "list_movies"
                $("#list_movies").append(listItem);
            });
        },
        error: function(){
            // Display an error message if the request fails
            $("#list_movies").append("<li>Error fetching movie data</li>");
        }
    });
});

