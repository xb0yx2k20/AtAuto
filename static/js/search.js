// static/js/live_search.js

$(document).ready(function () {
    $('#search').on('input', function () {
        var searchQuery = $(this).val();

        $.ajax({
            type: 'GET',
            url: '/cars/search',
            data: { search: searchQuery },
            success: function (data) {
                displayResults(data.cars);
            }
        });
    });

    function displayResults(cars) {
        var carsList = $('#carsList');
        carsList.empty();

        if (cars.length === 0) {
            carsList.append('<p>No cars found.</p>');
        } else {
            cars.forEach(function (car) {
                carsList.append('<li class="list-group-item">' + car.Mark + '</li>');
            });
        }
    }
});
