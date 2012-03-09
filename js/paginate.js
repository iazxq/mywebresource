/*
 * 	Easy Paginate 1.0 - jQuery plugin
 *	written by Alen Grakalic	
 *	http://cssglobe.com/
 *
 *	Copyright (c) 2011 Alen Grakalic (http://cssglobe.com)
 *	Dual licensed under the MIT (MIT-LICENSE.txt)
 *	and GPL (GPL-LICENSE.txt) licenses.
 *
 *	Built for jQuery library
 *	http://jquery.com
 *
 */

(function($) {
		  
	$.fn.easyPaginate = function(options){

		var defaults = {				
			step: 4,  //sets the number of items displayed but this value is overriden in the ink.js files. Make your changes to the number of items shown there instead.
			delay: 200,  //sets the pause between the items hiding and the next items showing. If you want to speed up the fading and out itself then change the values on lines 44 and 46 below
			numeric: true,
			nextprev: true,
			controls: 'pagination',
			current: 'pag-active' 
		}; 
		
		var options = $.extend(defaults, options); 
		var step = options.step;
		var lower, upper;
		var children = $(this).children();
		var count = children.length;
		var obj, next, prev;		
		var page = 1;
		var timeout;
		var clicked = false;
				

		function show(){
			clearTimeout(timeout);
			lower = ((page-1) * step);
			upper = lower+step;
			$(children).each(function(i){
				var child = $(this);
				child.fadeOut('300');  //change animate out speed
				if(i>=lower && i<upper){ 
					setTimeout(function(){ child.fadeIn('300',function(){child.parent().css("height", "auto").css("height", child.parent().height()); })}, options.delay );  //change animate in speed

				}
				if(options.nextprev){
					if(upper >= count) { next.hide('30'); } else { next.show('30'); };
					if(lower >= 1) { prev.show('30'); } else { prev.hide('30'); };
				};
			});	
			$('li','.'+ options.controls).removeClass(options.current);
			$('li[data-index="'+page+'"]','.'+ options.controls).addClass(options.current);
			
			if(options.auto){
				if(options.clickstop && clicked){}else{ timeout = setTimeout(auto,options.pause); };
			};
		};
		
		function auto(){
			if(upper <= count){ page++; show(); }			
		};
		
		this.each(function(){ 
			
			obj = this;
			
			if(count>step){
				
				var pages = Math.floor(count/step);
				if((count/step) > pages) pages++;
				
				var ul = $('<ul class="'+ options.controls +'"></ul>').appendTo('.paginate-nav');
				
				
				if(options.nextprev){
					prev = $('<li class="pag-prev"></li>')
						.hide()
						.appendTo(ul)
						.click(function(){
							clicked = true;
							page--;
							show();
						});
				};
				
				if(options.numeric){
					for(var i=1;i<=pages;i++){
					$('<li data-index="'+ i +'">'+ i +'</li>')
						.appendTo(ul)
						.click(function(){	
							clicked = true;
							page = $(this).attr('data-index');
							show();
						});					
					};				
				};
				
				if(options.nextprev){
					next = $('<li class="pag-next"></li>')
						.hide()
						.appendTo(ul)
						.click(function(){
							clicked = true;			
							page++;
							show();
						});
				};
			
				show();
			};
		});	
		
	};	

})(jQuery);