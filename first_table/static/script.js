
    $("#sender").click(function (e) {
        e.preventDefault();
        var input = $(this).val();

        $.ajax({
            url: '/sort/',
            method: 'POST',
            data: $('#form').serialize(),
            //dataType: 'json',
            success: function (data) {
                document.querySelector('#table').innerHTML = data;
            }
          });
        });

    // $('.pagination').find('a').each(function(index) {
    //     $(this).click(function (e) {
    //         e.preventDefault();
    //         let data = $(this).attr('href').slice(1);
    //
    //         $.get('/sort/', data, function (data) {
    //             document.querySelector('#table').innerHTML = data;
    //         })
    //     })
    // });
