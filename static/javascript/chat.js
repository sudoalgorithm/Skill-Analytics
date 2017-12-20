
function loading(ennable) {
    if (ennable) {
        $('#loader').removeClass('hidden');
        $('#input').attr('disabled', "");
        $('#submit').prop('disabled', true);
    } else {
        $('#loader').addClass('hidden');
        $('#input').removeAttr('disabled');
        $('#submit').prop('disabled', false);
    }
}

function addMyChat(text) {
    $('#chat').append("<div class='bubble-me'>" + text + "</div");
    $('#results').animate({ scrollTop: $('#results').get(0).scrollHeight }, 1000);
}

function addResponceChat(text) {
    $('#chat').append("<div class='bubble-them'>" + text + "</div");
    $('#results').animate({ scrollTop: $('#results').get(0).scrollHeight }, 1000);
}

function sendRequest(request) {
    loading(true);    
    $('#input-field').val('');
    $.ajax({
        method: "GET",
        url: "./message",
        contentType: "application/json",
        data: { "message": request }
    })
        .done(function (response) {
            addResponceChat(response);
            loading(false);
        });
}

$('#input-field').keydown(function (e) {
    var data = $('#input-field').val();
    if (e.which == 13 && data.length > 0) { //catch Enter key
        addMyChat(data)
        sendRequest(data);
    }
});

$('#send').click(function (e) {
    var data = $('#input-text').val();
    if (data.length > 0) {
        addMyChat(data);
        sendRequest(data);
    }
});
