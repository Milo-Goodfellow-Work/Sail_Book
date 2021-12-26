$(document).ready(function(){
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

  $("#search-input-large").on("change enter", function(){
    console.log('Test');
    new_url = new URL(window.location.origin);
    new_url.append('search',document.getElementById("search-input-large").value.split(' ').join('_'));
    window.location.replace(new_url.href);

  })

  $("#search-input-small").on("change enter", function(){
    console.log('Test');
    new_url = new URL(window.location.origin);
    new_url.append('search',document.getElementById("search-input-small").value.split(' ').join('_'));
    window.location.replace(new_url.href);

  })

});

var slideSwiper = new Swiper('.swiper-container', {
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',

  },

  pagination: {
    el: '.swiper-pagination',

  }
});
