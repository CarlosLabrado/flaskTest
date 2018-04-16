var chart;

/**
 * Request data from the server, add it to the graph and set a timeout
 * to request again
 */
function requestData() {
    $.ajax({
        url: '/live-data',
        success: function (point) {
            // var series = chart.series[0],
            //     shift = series.data.length > 20; // shift if the series is
            //                                      // longer than 20

            // add the point
            // chart.series[0].addPoint(point, true, shift);
            chart.series[0].addPoint(point);

            // call it again after one second
            setTimeout(requestData, 1000);
            setTimeout(clearData, 10000);
        },
        cache: false
    });
}

function clearData() {
    $.ajax({
        url: '/live-data',
        success: function () {
            chart.series[0].clear();

        },
        cache: false
    });
}

$(document).ready(function () {
    chart = new Highcharts.Chart('container', {
        chart: {
            renderTo: 'container',
            margin: [70, 50, 60, 80],
            defaultSeriesType: 'scatter',
            events: {
                load: requestData
            }
        },
        title: {
            text: 'Live petrolog data'
        },
        xAxis: {
            title: {
                text: 'Position'
            },
            gridLineWidth: 1,
            minPadding: 0.2,
            maxPadding: 0.2,
            maxZoom: 60
        },
        yAxis: {
            title: {
                text: 'Load'
            },
            minPadding: 0.2,
            maxPadding: 0.2,
            maxZoom: 60,
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        legend: {
            enabled: false
        },
        exporting: {
            enabled: false
        },
        plotOptions: {
            series: {
                lineWidth: 1,
            }
        },
        series: [{
            name: 'Dyna data',
            data: []
        }]
    });
});