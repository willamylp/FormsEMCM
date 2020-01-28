var data = [], totalPoints = 110;
var updateInterval = 3200;
var realtime = 'on';

$(function () {
    //Real time ==========================================================================================
    var valores = [getRandomData()];
    console.log(valores);

    var plot = $.plot('#real_time_chart', valores, {
        series: {
            shadowSize: 2,
            color: 'rgb(0, 150, 130)'
        },
        grid: {
            borderColor: '#f3f3f3',
            borderWidth: 1,
            tickColor: '#f3f3f3'
        },
        lines: {
            fill: true
        },
        yaxis: {
            min: 0,
            max: 100
        },
        xaxis: {
            min: 0,
            max: 100
        }
    });

    function updateRealTime() {
        plot.setData([getRandomData()]);
        plot.draw();

        var timeout;
        if (realtime === 'on') {
            timeout = setTimeout(updateRealTime, updateInterval);
        } else {
            clearTimeout(timeout);
        }
    }

    updateRealTime();

    $('#realtime').on('change', function () {
        realtime = this.checked ? 'on' : 'off';
        updateRealTime();
    });
    //====================================================================================================
});

function getRandomData() {
    if (data.length > 0) data = data.slice(1);

    while (data.length < totalPoints) {
        var prev = data.length > 0 ? data[data.length - 1] : 5, y = prev + Math.random() * 10 - 5;
        if (y < 0) { y = 0; } else if (y > 10) { y = 10; }

        data.push(y);
    }

    var res = [];
    for (var i = 0; i < data.length; ++i) {
        res.push([i, data[i]])
        
    }
    
    return res;
}