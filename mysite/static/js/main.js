/**
 * Created by Administrator on 2018-10-14.
 * Design nas.
 */





$(document).ready(function () {//HTML 과 CSS 의 모든 로딩이 끝나면 J-Query 를 실행.
    Logic();

    $(".container").niceScroll({
        cursorcolor: "#000",
        cursorwidth: 4,
        scrollspeed: 60,
        cursorborderradius: 0,
        mousescrollstep: 40,
        cursoropacitymin: 0,
        cursoropacitymax: 1,
        background: "none",
        cursorborder: "none",
        autohidemode: true,
        boxzoom: false,
        smoothscroll: true,
        zindex: 9999
    });

    // =========================
    // on event section      ===
    //==========================












//==============================================================
});




$(function () {

    // scroll event
    $('.container').scroll(function () {
        var scrollTop = $('.container').scrollTop();
        $('.posNum').text(scrollTop); // 스크롤값


        // =========================
        // scroll event section  ===
        //==========================






        // $("").stop().animate({"margin-top": -scrollTop * 0.1}, 200);





        //===================================================================
        // nav on/off event
        $('.container .main > section').each(function (i) {
            var fastNum = 100;
            var firstY = $('.container .main > section:first').position().top;
            var posY = $(this).position().top;
            if (scrollTop <= firstY - fastNum) {
                $('#nav').each(function () {
                    $('li', this).removeClass('on').eq(0).addClass('on');
                })
            } else if (scrollTop >= posY - fastNum) {
                $('#nav').each(function () {
                    $('li', this).removeClass('on').eq(i).addClass('on');
                })
            }
        })

    });
});












