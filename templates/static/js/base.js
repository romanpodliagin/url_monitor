$(document).ready(function() {
});

function sync(url_obj_id) {
    console.log('sync url ' + url_obj_id);

    $.ajax({
        type: 'POST',
        cache: false,
        data: {'url_obj_id': url_obj_id},
        url: '/monitor/url/' + url_obj_id + '/',
        error: function(xhr, status, e) {
           console.log(xhr.responseJSON.msg);
        },
    }).done(function(response) {
        console.log('success');
        location.reload();
    });
}

function sync_all() {
    console.log('sync all urls ');
}

$("[type='checkbox']").change(function() {
    let active = false;

    if(this.checked) {
        console.log('unpause' + this.id);
        active = true;
    } else {
        console.log('pause' + this.id);
        active = false;
    }

    $.ajax({
        type: 'POST',
        cache: false,
        data: {'url_obj_id': this.id,
                'active': active},
        url: '/monitor/active/' + this.id + '/',
        error: function(xhr, status, e) {
           console.log(xhr.responseJSON.msg);
        },
    }).done(function(response) {
        console.log('success');
    });
});