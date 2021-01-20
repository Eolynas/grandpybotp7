$(document).ready(function () {

    $("#submit").click(function (e) {
        var url = 'message';
        e.preventDefault();
        const str_message = $('#message').val();
        if (str_message) {
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

        }
        $.ajax({
            type: "POST",
            url: url,
            data: $('form').serialize(),
            dataType: 'json',
            beforeSend: function (data) {
                var loading_message = "\
                            <div class='d-flex justify-content-start mb-4' id='message_bot_loading'>\
                                <div class='img_cont_msg' >\
                                    <img id='message_bot' alt='avatar' src='/static/img/grandpybot.jpg' class='rounded-circle user_img_msg'>\
                                </div>\
                                    <div class='loading-msg'> \
                                        <div class='msg_cotainer'>\
                                            <div class='canvas canvas6'>\
                                                <div class='spinner p1'></div>\
                                                <div class='spinner p2'></div>\
                                                <div class='spinner p3'></div>\
                                                <div class='spinner p4'></div>\
                                            </div>\
                                        </div>\
                                    </div>\
                            </div>"
                $("#message").val("");
                $('#message-chatbot').append(loading_message)


            },
            success: function (data) {
                console.log(data)
                console.log(data.data.address)
                var id_map = "map_" + Date.now()
                // var message = "Voici l'adresse de " + data.data.message.data + ": " + data.data.address
                var dom_message_bot = "\
                                <div class='d-flex justify-content-start mb-4'>\
                                        <div class='img_cont_msg'>\
                                                <img id='message_bot' alt='avatar' src='/static/img/grandpybot.jpg' class='rounded-circle user_img_msg'>\
                                        </div>\
                                        <div class='msg_cotainer'>\
                                                " + data.data.message.data + "\
                                                <span class='msg_time'>" + data.data.message.date + "</span>\
                                        </div>\
                                </div>\
                                <div id="+ id_map +" class='map'></div>"
                var no_found_message = "\
                                <div class='d-flex justify-content-start mb-4'>\
                                        <div class='img_cont_msg'>\
                                                <img id='message_bot' alt='avatar' src='/static/img/grandpybot.jpg' class='rounded-circle user_img_msg'>\
                                        </div>\
                                        <div class='msg_cotainer'>\
                                                " + data.data.message.data + "\
                                                <span class='msg_time'>" + data.data.message.date + "</span>\
                                        </div>\
                                </div>"


                setTimeout(function () {
                    $('#message_bot_loading').remove()
                    if (data.data.status === false) {
                        $('#message-chatbot').append(no_found_message)
                    }
                    else {
                        $('#message-chatbot').append(dom_message_bot)
                        initMap(data.data.location.lat, data.data.location.lng, id_map)
                    }
                }, 500);

            },

        });


    });

});

let map;

function initMap(lat, lng, id) {
    // "lat": 47.9879489,
    // "lng": 0.2084077
    const myLatLng = {lat: lat, lng: lng};
    const map = new google.maps.Map(document.getElementById(id), {
        zoom: 12,
        center: myLatLng,
    });
    new google.maps.Marker({
        position: myLatLng,
        map,
        title: "Hello World!",
    });
}