$(function () {
    'use strict'
  
    $('[data-toggle="offcanvas"]').on('click', function () {
      $('.offcanvas-collapse').toggleClass('open')
    })
  });


  $(function() {
    $('[data-toggle="tooltip"]').tooltip()
  })