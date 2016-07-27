/* global $ */
$(document).ready(function() {
  $('.js-expand-location-information').on('click', function() {
    $('.js-location-information').toggleClass('hidden');
  });

  $('.js-toggle-electronic-invitation-form').on('click', function() {
    $('.js-electronic-invitation-form').toggleClass('hidden');
    $('.js-regrets-form').addClass('hidden');
  });

  $('.js-toggle-regrets-form').on('click', function() {
    $('.js-regrets-form').toggleClass('hidden');
    $('.js-electronic-invitation-form').addClass('hidden');
  });
});