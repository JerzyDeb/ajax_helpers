const modalAjax = $('#') //     id of modal

const initEventListeners = () => {
    $(".update-ajax, .delete-ajax, .create-ajax, .detail-ajax").on('click', loadForm);
}

const loadForm = (e) => {
    e.preventDefault();
    let btn = $(e.currentTarget);

    $.ajax({
        url: btn.attr('href'),
        type: 'GET',
        beforeSend: () => {
            modalAjax.modal('show');
        },
        success: (response) => {
            modalAjax.find(".modal-content").html(response.html);
        }
    });
};

const saveForm = (e) => {
    let form = $(e.currentTarget);
    e.preventDefault();
    let formData = new FormData(form[0]);
    let message = ''
    let title = ''
    $.ajax({
        url: form.attr('action'),
        method: form.attr('method'),
        data: formData,
        contentType: false,
        processData: false,
        headers: {
            'X-CSRFToken': ''  //     Csrf Token from Cookie
        },

        success: (response) => {
            $('.ajax-list').html(response.html_object_list)
            initEventListeners()
            modalAjax.modal("hide");
            title = response.title
            message = response.message
            alert(`${title} - ${message}`)  //     Here toast with message and title
        },
        error: (response) => {
            title = 'Error'
            if (response.responseJSON) {
                modalAjax.find(".modal-content").html(response.responseJSON.html);
                message = 'Form error'
            } else {
                message = 'Unexpected error'
            }
            alert(`${title} - ${message}`)  //     Toast with message and title
        }

    })
}
$(() => {
    initEventListeners()
    modalAjax.on('submit', '.ajax-update-form, .ajax-delete-form, .ajax-create-form', saveForm);
})