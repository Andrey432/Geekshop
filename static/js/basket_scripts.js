window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', function () {
        update(event.target);
    });

    function update(href) {
        $.ajax({
            url: "/basket/edit/" + href.name + "/" + href.value + "/",

            success: function (data) {
                $('.basket_list').html(data.result);
            },
        });
        event.preventDefault();
    }
}