$(document).ready(function () {

    $("#submit").click(function (e) {
        var url = 'message';
        e.preventDefault();
        const str_message = $('#message').val();
        if (str_message) {
            const now = new Date();
            let options = {dateStyle: 'short', timeStyle: 'short'};
            const date_now = now.toLocaleString('fr-FR', options)


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
                google(data.data)
                wiki(data.data)


            },
        });
    });
});

function dom_grandpy(message, id_map = false) {
    const now = new Date();
            let options = {dateStyle: 'short', timeStyle: 'short'};
            const date_now = now.toLocaleString('fr-FR', options)
    var dom_message_bot = "\
                                <div class='d-flex justify-content-start mb-4'>\
                                        <div class='img_cont_msg'>\
                                                <img id='message_bot' alt='avatar' src='/static/img/grandpybot.jpg' class='rounded-circle user_img_msg'>\
                                        </div>\
                                        <div class='msg_cotainer'>\
                                                " + message + "\
                                                <span class='msg_time'>" + date_now + "</span>\
                                        </div>\
                                </div>\
                                <div id=" + id_map + " class='map'></div>"
    var dom_message_bot_without_map = "\
                                <div class='d-flex justify-content-start mb-4'>\
                                        <div class='img_cont_msg'>\
                                                <img id='message_bot' alt='avatar' src='/static/img/grandpybot.jpg' class='rounded-circle user_img_msg'>\
                                        </div>\
                                        <div class='msg_cotainer'>\
                                                " + message + "\
                                                <span class='msg_time'>" + date_now + "</span>\
                                        </div>\
                                </div>"
    if (id_map === false){
        $('#message-chatbot').append(dom_message_bot_without_map)
    }
    else {
        $('#message-chatbot').append(dom_message_bot)
    }
}

function initMap(lat, lng, id) {
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

function google(data) {
    var id_map = "map_" + Date.now()

    setTimeout(function () {
        $('#message_bot_loading').remove()
        if (data.status === false) {
            dom_grandpy(data.message.data, id_map)
            $('#' + id_map).remove()
        } else {
            // $('#message-chatbot').append(dom_message_bot)
            dom_grandpy(data.message.data, id_map)
            initMap(data.location.lat, data.location.lng, id_map)
        }
    }, 500);

}

function wiki(data, id_map) {
    grandpy_question_wiki = "Au passage connais tu l'histoire de ce lieux ?"
    grandpy_return_wiki = data.WIKI

    setTimeout(function () {
        dom_grandpy(grandpy_question_wiki)
        $('#' + id_map).remove()
        dom_grandpy(grandpy_return_wiki)
        $('#' + id_map).remove()
    }, 4000);
}