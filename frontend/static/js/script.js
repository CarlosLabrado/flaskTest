$(function () {
    $('button').click(function () {
        $.ajax({
            url: '/refreshStatus',
            data: $('form').serialize(),
            type: 'POST',
            success: function (response) {
                console.log(response);

                $("#status").empty().append("<ul id='list'></ul>");

                var json_obj = $.parseJSON(response);

                console.log(json_obj);
                console.log(json_obj[0]);

                // var output="<ul>";
                for (var i in json_obj) {
                    $("#list").append("<li>" + json_obj[i].well_status + " : " + json_obj.automatic + "</li>");
                }
                // output+="</ul>";

                // $.each(json_obj, function(n, elem) {
                //    $("#list").append("<li>" + elem.status + " : " + elem.user + "</li>");
                // });
                // $('span').html(output);
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});