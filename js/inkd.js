
jQuery.noConflict()(function($){
	$(document).ready(function() {  



	// Homepage Accordion	
	if ($('#liteaccordion').length > 0){			
		$('#liteaccordion').liteAccordion({
			containerWidth : 960, // width of accordion (px)
			containerHeight : 320, // height of accordion (px)
			headerWidth : 48,  // width of tabs (px)

			firstSlide : 1,  // number of the first active slide (integer)
			slideSpeed : 600, // speed of slide animation (time/ms)

			autoPlay : false,   // automatically scroll through the slides, if true with pause on user click (boolean)
			cycleSpeed : 6000  // time between slide activation (time/ms)
		});
		$('#liteaccordion li').filter(':odd').addClass('acc-alt');
	}
	
	
	// Homepage Carousel	
	if ($('#hp-port-carousel').length > 0){	
	   $("#hp-port-carousel").carouFredSel({
			auto: false,   //Controls whether the carousel uses autoplay or not
			items: 5,    //Tells the script how many items should be shown in visible group
			width: 978,  //Sets the width of the carousel area
			scroll: {
				fx: "scroll",  //Animation effect
				duration: 600,  //Duration of animation
				easing: "easeInOutQuad"  //Sets the easing effect
			},
			next: "#port-carousel-next",
			prev: "#port-carousel-prev"
       }); 
	}   
	
	// Thumbnail Gallery 
	if ($('#thumb-gallery').length > 0){		
	$('#thumb-gallery').galleria({
        width:724,
        height: 493,
		autoplay: false,
		carouselSpeed: 400,	
        imageCrop: true,  //Sets how images will be sized if they are not the same size as the carousel area. False: images are sized down so all of it will fit in window. true fills the player area and parts of image may end							up being cropped off. 'height' scales image to fill height of player area. 'width' scales image to fill width of player area.	
        imageMargin: 0,   	//Adds a space between images and edge of player.
		imagePan: false,   //Allows user to pan around image if parts of image have been cropped off when image is sized to fill the player area.
		showInfo: true,	  //Turns image captions on and off.
		showCounter: false,	//Turns image counter numbers on and off.	
		thumbCrop: true,	//Sets how thumbnails will be sized if they aren't the same size as the thumbnail area. False: images are sized down so all of it will fit. true fills the thumbnail area and parts of image may end up							being cropped off. 	
        thumbMargin: 0,    //Controls the spacing between thumbnails
		thumbnails: true,	//Turn thumbnails on and off
        transition: 'fade',  //    "fade" crossfade betweens images
							 //  "flash" fades into background color between images
							 //  "pulse" quickly removes the image into background color, then fades the next image
							 //   "slide" slides the images depending on image position
							//  "fadeslide" fade between images and slide slightly at the same time
		transitionSpeed: 500,  //Sets how fast the transition between images happens.
		debug: false		//Leave this set to false unless you are customizing the gallery and want the script to output any errors
    });
	}

    /*
	// Portfolio Filtering		
        $('#port-filter a').click(function() {  
            $('#port-filter .port-active').removeClass('port-active');  
            $(this).parent().addClass('port-active');  
      
            var filterVal = $(this).attr("href").replace(/#/g,'');  
      
            if(filterVal == 'all') {  
                $('.port-overlay').fadeOut('300', function() { $(this).css({'display' : 'none'}) });  // To change speed of animation adjust the number '300' lower or higher.
                $('.port-columns li').removeClass('hidden')  				
            } else {  
                $('.port-columns li').each(function() {  
                    if($(this).hasClass(filterVal)) {  
                        $(this).find('.port-overlay').fadeOut('300', function() { $(this).css({'display' : 'none'}) });  // To change speed of animation adjust the number '300' lower or higher.
						$(this).removeClass('hidden') 						
                    } else {  
                        $(this).find('.port-overlay').fadeIn("300", function() { $(this).css({'display' : 'block'}) });  	// To change speed of animation adjust the number '300' lower or higher.
						$(this).addClass('hidden');  								
                    }  
                });  
            }  
      
            return false;  
        });  
        */

	// Switches between Twitter/Facebook feeds in sidebar widget.		
	//When page loads...
	$(".social-content").hide(); //Hide all content
	$("#social-nav li:first").addClass("tab-active").show(); //Activate first tab
	$(".social-content:first").show(); //Show first tab content

	//On Click Event
	$("#social-nav li").click(function() {
		$("#social-nav li").removeClass("tab-active"); //Remove any "active" class
		$(this).addClass("tab-active"); //Add "active" class to selected tab
		$(".social-content").hide(); //Hide all tab content

		var activeTab = $(this).find("a").attr("href"); //Find the href attribute value to identify the active tab + content
		$(activeTab).show(); //Fade in the active ID content
		return false;
	});
		
		
		
	// start tweet timeline feed in sidebar. More customization options in jquery.tweet.js file.
	if ($('#tweet-sidebar').length > 0){			
		$("#tweet-sidebar").tweet({  
			username: "envatowebdev",  // Twitter account user.
			avatar_size: null,  // Size of avatar. Change to, null, to hide avatar
			count: 3,  //  Number of tweets to display from timeline
			loading_text: "loading tweets..."  //  Text displayed while tweet is loading
		});
	}


	// start tweet timeline feed in footer. More customization options in jquery.tweet.js file.
	if ($('#tweet-footer').length > 0){		
		$("#tweet-footer").tweet({
			username: "envatowebdev",  // Twitter account user.
			avatar_size: null,  // Size of avatar. Change to, null, to hide avatar
			count: 1,  //  Number of tweets to display from timeline
			loading_text: "loading tweets...",  //  Text displayed while tweet is loading
      		template: "{avatar}{join}{text}"   // [string or function] template used to construct each tweet <li> - see code for available vars			
		});
	}
	
	// Testimonial Carousel	
	if ($('#test-carousel').length > 0){	
	   $("#test-carousel").carouFredSel({
			auto: false,   //Controls whether the carousel uses autoplay or not
			height: 306, //Sets height of area
			items: {
				visible: 1, //Tells the script how many should be visible at once
				minimum: 1,
				height: 306 //Sets height of testimonial
			},
			scroll: {
				fx: "fade", //Sets animation effect
				duration: 400 //Duraiton of animation
			},
			next: "#test-carousel-next",
			prev: "#test-carousel-prev"
       }); 
	}   




	// Automated Pagination for One Column Portfolio
	if ($('#paginate-onecol').length > 0){
		$('#paginate-onecol').easyPaginate({
			step:3 //Change value here to set the number of items shown on each page. 
		});
	}
	
	// Automated Pagination for Two Column Portfolio
	if ($('#paginate-twocol').length > 0){
		$('#paginate-twocol').easyPaginate({
			step:4 //Change value here to set the number of items shown on each page. To avoid layout display issues it's best to set the number in multiples of the column layout being used. 
			       //For example, a 2 column layout should be set to 2,4, or 6 and so on.
		});	
	}
	
	// Automated Pagination for Three Column Portfolio
	if ($('#paginate-threecol').length > 0){
		$('#paginate-threecol').easyPaginate({
			step:9 //Change value here to set the number of items shown on each page. To avoid layout display issues it's best to set the number in multiples of the column layout being used. 
			       //For example, a 3 column layout should be set to 3,6, or 9 and so on.
		});	
	}
	
	// Automated Pagination for Four Column Portfolio
	if ($('#paginate-fourcol').length > 0){
		$('#paginate-fourcol').easyPaginate({
			step:16 //Change value here to set the number of items shown on each page. To avoid layout display issues it's best to set the number in multiples of the column layout being used. 
			       //For example, a 4 column layout should be set to 4,8, or 12 and so on.
		});	
	}
	
	// Automated Pagination for Grid Portfolio
	if ($('#paginate-grid').length > 0){
		$('#paginate-grid').easyPaginate({
			step:21 //Change value here to set the number of items shown on each page. To avoid layout display issues it's best to set the number in multiples of the column layout being used. 
			       //For example, a grid column layout should be set to 7,14, or 21 and so on.
		});
	}	
	
     // Prevents display of all paginated portfolio images when page is first loaded before the script has had time to finish paginating them.
	 //$('#paginate-grid, #paginate-fourcol, #paginate-threecol, #paginate-twocol, #paginate-onecol, .paginate-nav, #paginate-filter #port-filter').hide();
	 $('#port-loading').show();
	 $(window).load(function() {
		//$('#port-loading').fadeOut('100', function(){$('#paginate-grid, #paginate-fourcol, #paginate-threecol, #paginate-twocol, #paginate-onecol, .paginate-nav, #paginate-filter #port-filter').css('height', 'auto').fadeIn('200'); });
	 });		

	// Photoswipe Fullscreen slideshow lightbox
	if ($('.photoswipe').length > 0){
		var options = {};
		$(".photoswipe li a:has(img)").photoSwipe({

			// General Setttings
			fadeInSpeed: 250,  //The speed of any fading-in elements 
			fadeOutSpeed: 250,   //The speed of any fading-out elements 
			preventHide: false,   //Prevents the user closing PhotoSwipe. Also hides the "close" button from the toolbar. 
			preventSlideshow: false,   //Prevents the slideshow being activated. Also hides the "play" button from the toolbar. 
			zIndex: 9999,
			backButtonHideEnabled: true,  //This will hide the gallery when the user hits the back button. Useful for Android  and Blackberry. 
			enableKeyboard: true,  //Enables keyboard support. 
			enableMouseWheel: true,   //Enables mouse support. 
			mouseWheelSpeed: 350,  //How responsive the mouse wheel is. 
			autoStartSlideshow: false,  //Start the slideshow automatically. Change to false to not start.


			// Carousel
			loop: true,  //Whether the gallery auto-loops back to the beginning when you reach the end
			slideSpeed: 250, //How fast images slide into view
			nextPreviousSlideSpeed: 250,  //How fast images are displayed when the next/previous buttons are clicked
			enableDrag: true, //Enables dragging the next / previous image into view
			swipeThreshold: 50,  //How many pixels your finger has to move across the screen to register a swipe gesture. 
			swipeTimeThreshold: 250, //A swipe must take no longer than this value in milliseconds to be registered as a swipe gesture.
			slideTimingFunction: 'ease-out',   //Easing function used when sliding.
			slideshowDelay: 3000, //The delay between showing the next image when in slideshow mode
			doubleTapSpeed: 250,  //Double tap speed 
			margin: 20,  //The margin between each image in pixels. 
			imageScaleMethod: 'fitNoUpscale', // Either "fit", "fitNoUpscale" or "zoom". "fit" ensures the image always fits the screen. 
											//"fitNoUpscale" works like "fit" but will never upscale the image. "zoom" the image will always fill the full screen and some parts of image may be cropped off.
											//				
			// Toolbar
			captionAndToolbarHide: false,  //Hide the caption and toolbar. 
			captionAndToolbarFlipPosition: false,  //Place the caption at the bottom and the toolbar at the top. 
			captionAndToolbarAutoHideDelay: 5000,  //Set delay before these hide after they're not being interacted with
			captionAndToolbarOpacity: 0.8,	  //Controls the opacity of the caption and toolbar	
			captionAndToolbarShowEmptyCaptions: true,  //Shows a blank caption area even if a caption cannot be found for the current image. 


			// ZoomPanRotate
			allowUserZoom: true, //Allows user to zoom in/out on image 
			allowRotationOnUserZoom: false,  //iOS only - Allow the user to rotate images whilst zooming / panning. 
			maxUserZoom: 5.0,   //The maximum a user can zoom into an image. Default = 5.0 (set to zero for this to be ignored)
			minUserZoom: 0.5,   //The minimum a user can zoom out of an image. Default = 0.5 
			doubleTapZoomLevel: 2.5  //When the user double taps an image, the default "zoom-in" level. 

		});
	}


	// Fancybox Lightbox
	if ($('.fancybox').length > 0){
		$('.fancybox li a:has(img)').fancybox({
		
			padding : 12, //Space between FancyBox wrapper and content
			margin : 60,  //Space between viewport and FancyBox wrapper
			cyclic : true,  // When true, galleries will be cyclic, allowing you to keep pressing next/back.
			centerOnScroll : true,  //When true, FancyBox is centered while scrolling page
			overlayShow : true,   //Hide or show the overlay when lightbox is shown
			overlayOpacity : 0.5,
			overlayColor : '#111',
			titleShow : true,  //Displays the title of the content
			titlePosition : 'over', // The position of title. Can be set to 'outside', 'inside' or 'over'
			transitionIn : 'fade', // The transition type. Can be set to 'elastic', 'fade' or 'none'
			transitionOut : 'fade', // The transition type. Can be set to 'elastic', 'fade' or 'none'
			speedIn : 300,  //Speed of the fade and elastic transitions, in milliseconds
			speedOut : 300,  //Speed of the fade and elastic transitions, in milliseconds
			changeSpeed : 300,  //Speed of resizing when changing gallery items, in milliseconds
			changeFade : 'fast'  //Speed of the content fading while changing gallery items		
		});
	}

	//Contact Form
	if ($('#contact').length > 0){
		
		//Do what we need to when form is submitted.	
		$('#form_submit').click(function(){

		//Setup any needed variables.
		var input_name = $('#form_name').val(),
			input_email = $('#form_email').val(),
			input_message = $('#form_message').val(),
			response_text = $('#response');
			//Hide any previous response text 
			response_text.hide();

			//Change response text to 'loading...'
			response_text.html('Loading...').show();

			//Make AJAX request 
			$.post('php/contact-send.php', {name: input_name, email: input_email, message: input_message}, function(data){
				response_text.html(data);
			});

			//Cancel default action
			return false;
		});
	}

	// Prevents anything from happening when a link you mark as inactive is clicked on. Useful for a menu item that has a sub-menu but doesn't have its own page itself.	
	$('a.inactive').click(function() { return false; });

}); 
});