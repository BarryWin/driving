(function ($) {

    "use strict";

    var fullHeight = function () {

        $('.js-fullheight').css('height', $(window).height());
        $(window).resize(function () {
            $('.js-fullheight').css('height', $(window).height());
        });

    };
    fullHeight();

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

})(jQuery);

$(document).ready(function () {
    $('#table_id').DataTable({
        "language": {
            "lengthMenu": "Показывает _MENU_ записей на странице",
            "zeroRecords": "Ничего не найдено - сори",
            "emptyTable": "В таблицы нет данных",
            "info": "Показано _END_ из _TOTAL_ записей",
            "infoEmpty": "Нет доступных записей",
            "infoFiltered": "(Выбрано из _MAX_ записей)",
            "search": "Поиск:",
            "paginate": {
                "previous": "Предыдущая страница",
                "next": "Следующая страница",
            }
        }
    });

     $('#tel').mask('+7 (000) 000-0000');
     $('#lessons-history').DataTable();
});


$(document).ready(function () {
    $('#exams').DataTable();
});

$(document).ready(function () {
    $('#documents').DataTable();
});

$(document).ready(function () {
    $('#next-lessons').DataTable();
});

let menuLink = document.querySelectorAll('.menu-link');
let pageLocation = window.location.href;

menuLink.forEach(link => {

	let linkAddress = link.href;

	if (pageLocation === linkAddress) {
	    link.parentElement.classList.add('active');
	}
});
