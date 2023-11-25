const $modalAjax = $('#BasicModal')

const initEventListeners = () => {
    $('.update-ajax, .delete-ajax, .create-ajax, .detail-ajax').on('click', loadForm);
}

const loadForm = (e) => {
    e.preventDefault();
    const $btn = $(e.currentTarget);
    $.ajax({
        url: $btn.attr('href'),
        type: 'GET',
        beforeSend: () => {
            $modalAjax.modal('show');
        },
        success: (response) => {
            $modalAjax.find('.modal-content').html(response.html);
            $modalAjax.find('.modal-content form').attr('action', $btn.attr('href'))
        }
    });
};

const saveForm = (e) => {
    e.preventDefault();
    const $form = $(e.currentTarget);
    const $formData = new FormData($form[0]);
    let message = '';
    let title = '';
    $.ajax({
        url: $form.attr('action'),
        method: $form.attr('method'),
        data: $formData,
        contentType: false,
        processData: false,
        success: (response) => {
            if ($form.attr('data-refresh-div')) {
                const divId = $form.attr('data-refresh-div');
                $(`#${divId} .ajax-list`).html(response.html);
            } else {
                $(`.ajax-list`).html(response.html);
            }
            initEventListeners();
            $modalAjax.modal('hide');
            title = response.title;
            message = response.message;
            Toastify({
                text: message,
                backgroundColor: 'green',
                duration: 3000
            }).showToast();    //     Toast with message
        },
        error: (response) => {
            title = 'Error';
            if (response.responseJSON) {
                $modalAjax.find('.modal-content').html(response.responseJSON.html);
                message = 'Form error';
            } else {
                message = 'Unexpected error';
            }
            Toastify({
                text: message,
                backgroundColor: 'red',
                duration: 3000
            }).showToast();  //     Toast with message
            $modalAjax.find('.modal-content form').attr('action', $form.attr('href'));
        }
    })
}
$(() => {
    initEventListeners();
    $modalAjax.on('submit', '.ajax-update-form, .ajax-delete-form, .ajax-create-form', saveForm);
})