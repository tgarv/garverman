$(document).ready(function() {
    var weddingDate = new Date('2017-05-06T17:30:00');

    var now = new Date();
    var diff = Math.floor((weddingDate - now) / 1000);

    // var clock = $('.countdown_clock').FlipClock(diff, {
    //     countdown: true,
    //     clockFace: 'DailyCounter',
    //     showSeconds: false
    // });
});