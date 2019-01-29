

(function() {
    "use strict";

    // custom scrollbar

    $(".left-side").niceScroll({styler:"fb",cursorcolor:"#ccc", cursorwidth: '5', cursorborderradius: '0px', background: '#ccc', spacebarenabled:false, cursorborder: '2'});


    $(".left-side").getNiceScroll();
    if ($('body').hasClass('left-side-collapsed')) {
        $(".left-side").getNiceScroll().hide();
    }



    // Toggle Left Menu
   jQuery('.menu-list > a').click(function() {
      
      var parent = jQuery(this).parent();
      var sub = parent.find('> ul');
      
      if(!jQuery('body').hasClass('left-side-collapsed')) {
         if(sub.is(':visible')) {
            sub.slideUp(200, function(){
               parent.removeClass('nav-active');
               jQuery('.main-content').css({height: ''});
               mainContentHeightAdjust();
            });
         } else {
            visibleSubMenuClose();
            parent.addClass('nav-active');
            sub.slideDown(200, function(){
                mainContentHeightAdjust();
            });
         }
      }
      return false;
   });

   function visibleSubMenuClose() {
      jQuery('.menu-list').each(function() {
         var t = jQuery(this);
         if(t.hasClass('nav-active')) {
            t.find('> ul').slideUp(200, function(){
               t.removeClass('nav-active');
            });
         }
      });
   }

   function mainContentHeightAdjust() {
      // Adjust main content height
      var docHeight = jQuery(document).height();
      if(docHeight > jQuery('.main-content').height())
         jQuery('.main-content').height(docHeight);
   }

   //  class add mouse hover
   jQuery('.custom-nav > li').hover(function(){
      jQuery(this).addClass('nav-hover');
   }, function(){
      jQuery(this).removeClass('nav-hover');
   });


   // Menu Toggle
   jQuery('.toggle-btn').click(function(){
       $(".left-side").getNiceScroll().hide();
       
       if ($('body').hasClass('left-side-collapsed')) {
           $(".left-side").getNiceScroll().hide();
       }
      var body = jQuery('body');
      var bodyposition = body.css('position');

      if(bodyposition != 'relative') {

         if(!body.hasClass('left-side-collapsed')) {
            body.addClass('left-side-collapsed');
            jQuery('.custom-nav ul').attr('style','');

            jQuery(this).addClass('menu-collapsed');

         } else {
            body.removeClass('left-side-collapsed chat-view');
            jQuery('.custom-nav li.active ul').css({display: 'block'});

            jQuery(this).removeClass('menu-collapsed');

         }
      } else {

         if(body.hasClass('left-side-show'))
            body.removeClass('left-side-show');
         else
            body.addClass('left-side-show');

         mainContentHeightAdjust();
      }

   });
   

   /*searchform_reposition();*/

   jQuery(window).resize(function(){

      if(jQuery('body').css('position') == 'relative') {

         jQuery('body').removeClass('left-side-collapsed');

      } else {

         jQuery('body').css({left: '', marginRight: ''});
      }


   });



})(jQuery);





$(function(){
$('.notification-scroll-list').slimScroll({
height: '220px',
 allowPageScroll: true,
    alwaysVisible: true
});
});



$(function(){
$('.message-scroll-list').slimScroll({
	height: '220px',
	allowPageScroll: true,
	alwaysVisible: true
});
});



 $(".inbox-scroll-list").niceScroll({styler:"fb",cursorcolor:"#ccc", cursorwidth: '5', cursorborderradius: '0px', background: '#ccc', spacebarenabled:false, cursorborder: '2'});


$(".chat-scroll-list").niceScroll({styler:"fb",cursorcolor:"#ccc", cursorwidth: '5', cursorborderradius: '0px', background: '#ccc', spacebarenabled:false, cursorborder: '2'});


//tooltip
$(function() {
	$('[data-toggle="tooltip"]').tooltip()
})

// Initialize Popovers
jQuery('[data-toggle="popover"], .js-popover').popover({
	container: 'body',
	animation: true,
	trigger: 'hover'
});



$(document).ready(function () {
	function setHeight() {
		windowHeight = $(window).innerHeight()-100;
		$('.wrapper').css('min-height', windowHeight);
	};
	setHeight();
	
	$(window).resize(function () {
		setHeight();
	});
});
