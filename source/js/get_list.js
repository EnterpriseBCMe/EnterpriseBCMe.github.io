$.ajax({
    url: "/resource/shipname.json",
    type: "GET",
    dataType: "json",
    success: 
    function (data) {
        displayData(data)
    }
});