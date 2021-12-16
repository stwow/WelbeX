
    $("#sender").click(function (e) {
        e.preventDefault();
        let data = $('#form').serialize();

        $.post('/sort/', data, function (result) {
                document.querySelector('#table').innerHTML = result;
                func();
        })
    });

    func();

    function  func(){
        $('.pagination').find('a').each(function(index) {
            $(this).click(function (e) {
                e.preventDefault();
                let data = $(this).attr('href').slice(1);

                $.get('/sort/', data, function (result) {
                    document.querySelector('#table').innerHTML = result;
                    func();
                })
            })
        })
    }
