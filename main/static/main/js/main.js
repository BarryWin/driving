(function($) {

	"use strict";

	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

	$('#sidebarCollapse').on('click', function () {
      $('#sidebar').toggleClass('active');
  });

})(jQuery);

$(document).ready( function () {
    $('#table_id').DataTable();
} );

$(document).ready( function () {
    $('#documents').DataTable();
} );

$(document).ready( function () {
    $('#next-lessons').DataTable();
} );
