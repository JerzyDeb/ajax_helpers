const modalAjax = $('#BasicModal')

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
            modalAjax.find(".modal-content form").attr('action', btn.attr('href'))
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

        success: (response) => {
            $('.ajax-list').html(response.html)
            initEventListeners()
            modalAjax.modal("hide");
            title = response.title
            message = response.message
            Toastify({
                text: message,
                backgroundColor: 'green',
                duration: 3000
            }).showToast();

            // alert(`${title} - ${message}`)  //     Toast with message
        },
        error: (response) => {
            title = 'Error'
            if (response.responseJSON) {
                modalAjax.find(".modal-content").html(response.responseJSON.html);
                message = 'Form error'
            } else {
                message = 'Unexpected error'
            }
            Toastify({
                text: message,
                backgroundColor: 'red',
                duration: 3000
            }).showToast();  //     Toast with message
        }

    })
}
$(() => {
    initEventListeners()
    modalAjax.on('submit', '.ajax-update-form, .ajax-delete-form, .ajax-create-form', saveForm);
})