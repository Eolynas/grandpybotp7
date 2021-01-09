$(document).ready(function () {

    $("#submit").click(function (e) {
        var url = 'message';
        e.preventDefault();
        $.ajax({
            type: "POST",
            url: url,
            data: $('form').serialize(),
            dataType: 'json',
            success: function (data) {
                // console.log(data);
                // console.log(data.data.message);

                const str_message = $('#message').val();
                if (str_message){
                    const now = new Date();
                    const date_now = now.getDate() + '/' + now.getMonth() + '/' + now.getFullYear() + ' ' + now.getHours() + ':' + now.getMinutes();
                    console.log('val ' + str_message)


                    $('#message-chatbot').append("\
                        <div class='d-flex justify-content-end mb-4'>\
                                <div class='msg_cotainer_send'>\
                                    " + str_message + "\
                                    <span class='msg_time_send'>" + date_now + "</span>\
                                </div>\
                                <div class='img_cont_msg'>\
                                    <img alt='avatar' src='/static/img/child.jpg' class='rounded-circle user_img_msg'>\
                                </div>\
                        </div>"
                    )
                    document.getElementById("message").value = "";
                    }


            }
        });

    });

});