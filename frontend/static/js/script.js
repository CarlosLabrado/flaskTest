$(function () {
    $("#refresh_stats").click(function () {
        $.ajax({
            url: '/refreshStatus',
            data: $("#status_form").serialize(),
            type: 'POST',
            success: function (response) {
                console.log(response);

                $("#status").empty().append("<ul id='list'></ul>");

                var json_obj = $.parseJSON(response);

                console.log(json_obj);

                $("#list").append("<li>" + "Well Status : " + json_obj.well_status + "</li>")
                    .append("<li>" + "Automatic : " + json_obj.automatic + "</li>")
                    .append("<li>" + "Percent Fillage : " + json_obj.percent_fillage + "</li>")
                    .append("<li>" + "Run Time : " + json_obj.run_time + "</li>")
                    .append("<li>" + "Strokes This Cycle : " + json_obj.strokes_this + "</li>")
                    .append("<li>" + "Strokes Last Cycle : " + json_obj.strokes_last + "</li>");

            },
            error: function (error) {
                console.log(error);
            }
        });
    });
    $("#update_settings").click(function () {
        $.ajax({
            url: '/updateSettings',
            data: $("#settings_form").serialize(),
            dataType: 'json',
            type: 'POST',
            success: function (data) {
                console.log(data)

            }
        });
    })
});