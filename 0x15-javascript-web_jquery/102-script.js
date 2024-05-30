$(document).ready(function(){
    // When the user clicks on the button to translate
    $("#btn_translate").click(function(){
        // Get the language code entered by the user
        var languageCode = $("#language_code").val();
        
        // Make an AJAX request to fetch the translation
        $.ajax({
            url: "https://www.fourtonfish.com/hellosalut/hello/",
            method: "GET",
            dataType: "json",
            data: { lang: languageCode },
            success: function(data){
                // Display the translation of "Hello" in the div with id "hello"
                $("#hello").text(data.hello);
            },
            error: function(){
                // Display an error message if the request fails
                $("#hello").text("Error fetching translation");
            }
        });
    });
});

