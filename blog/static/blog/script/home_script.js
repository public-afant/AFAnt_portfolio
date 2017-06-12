/*
    $(function() {
        $(window).scroll(function() {
            var value = $(this).scrollTop();  //스크롤 수치를 취득
            $('.scrollValue').text(value);
        });
    });
*/
    $(function() {
	var area2PosTop = $('#area2').offset().top;
	var area3PosTop = $('#area3').offset().top;
	var area4PosTop = $('#area4').offset().top;

	$(window).scroll(function() {
		var value = $(this).scrollTop();
		$('.scrollValue').text(value);

		$('#area1').css('background-position-y', value);

		if (value > area2PosTop) {
			$('#area2').css('background-position-y', area2PosTop);
			console.log('area2 variable');
		} else {
		 	$('#area2').css('background-position-y', 'top');
		 	console.log('area2 top');
		 }

		if (value > area3PosTop) {
			$('#area3').css('background-position-y', value - area3PosTop);
			console.log('area3 variable');
		} else {
			$('#area3').css('background-position-y', 'top');
			console.log('area3 top');
		}
     
	});
});