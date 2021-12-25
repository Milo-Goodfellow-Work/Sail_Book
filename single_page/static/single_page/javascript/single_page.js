$(document).ready(function(){

  //Switch each media image to GET from the current url
  let slides = document.getElementsByClassName("swiper-slide");
  for(i in slides){
    slides[i].src = window.location.origin + slides[i].src;
  }

  if($(window).width()<992)
  {
    $('#mobile-sell').append($("#desktop-sell").html());
    /*$('#mobile-buy').append($("#desktop-buy").html());*/
    $('#desktop-sell').empty();
    /*$('#desktop-buy').empty();*/

  }else {
    $('#mobile-sell').empty();
    $('#mobile-buy').empty();

  }

  $(window).on("resize", function(){

    if($(window).width()<992 && $('#mobile-sell').is(':empty'))
    {
      $('#mobile-sell').append($("#desktop-sell").html());
      $('#desktop-sell').empty();

    }else if ($(window).width()>992 && $('#desktop-sell').is(':empty')) {
      $('#desktop-sell').append($("#mobile-sell").html());
      $('#mobile-sell').empty();

    }

    if($(window).width()<992 && $('#mobile-buy').is(':empty'))
    {
      $('#mobile-buy').append($("#desktop-buy").html());
      $('#desktop-buy').empty();

    }else if ($(window).width()>992 && $('#desktop-buy').is(':empty')) {
      $('#desktop-buy').append($("#mobile-buy").html());
      $('#mobile-buy').empty();

    }

  })

});


$(".search-input").on("change enter", function(){
  window.location.href = (window.location.origin + ($(this).val()));

})

var slideSwiper = new Swiper('.swiper-container', {
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',

  },

  pagination: {
    el: '.swiper-pagination',

  }
});
