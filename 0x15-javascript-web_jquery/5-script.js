$(document).ready(function(){
    // When the user clicks on the div with id "add_item"
    $("#add_item").click(function(){
        // Create a new list item element
        var newItem = $("<li>").text("Item");
        // Append the new item to the UL with class "my_list"
        $("ul.my_list").append(newItem);
    });
});

