$(document).ready(function () {

    $("#submit").click(function (e) {
        var url = 'message';
        e.preventDefault();
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
                        </div>")

                    // setTimeout(function(){
                    //     $('#message-chatbot').append("\
                    //         <div class='d-flex justify-content-start mb-4'>\
                    //             <div class='img_cont_msg' >\
                    //                 <img id='message_bot' alt='avatar' src='/static/img/grandpybot.jpg' class='rounded-circle user_img_msg'>\
                    //             </div>\
                    //                 <div class='loading-msg'> \
                    //                     <div class='msg_cotainer'>\
                    //                         <div class='canvas canvas6'>\
                    //                             <div class='spinner p1'></div>\
                    //                             <div class='spinner p2'></div>\
                    //                             <div class='spinner p3'></div>\
                    //                             <div class='spinner p4'></div>\
                    //                         </div>\
                    //                     </div>\
                    //                 </div>\
                    //         </div>")
                    // }, 2000);
                    }
        $.ajax({
            type: "POST",
            url: url,
            data: $('form').serialize(),
            dataType: 'json',
            beforeSend: function (data) {
                $("#message").val("");
            },
            success: function (data) {
                console.log(data)
                console.log(data.data.address)
                var message = "Voici l'addresse: " + data.data.address
                $('#message-chatbot').append("\
                            <div class='d-flex justify-content-start mb-4'>\
                                    <div class='img_cont_msg'>\
                                        <img id='message_bot' alt='avatar' src='/static/img/grandpybot.jpg' class='rounded-circle user_img_msg'>\
                                    </div>\
                                    <div class='msg_cotainer'>\
                                        "+ message +"\
                                        <span class='msg_time'></span>\
                                    </div>\
                                </div>"
                )
            }

        });
        // setTimeout(function(){
        //         $("#message_bot").replaceWith(<p id='message_bot'> Voici ma réponse </p>)
        //         }, 2000);


    });

});