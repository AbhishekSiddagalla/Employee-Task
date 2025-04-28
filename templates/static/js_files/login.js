$(document).ready(function () {
    $('#login-form').on('submit', function (e) {
        e.preventDefault();

        formData = $(this).serialize();
        const actionUrl = $(this).attr('action');
        $.ajax({
            url: actionUrl,
            type: 'POST',
            data: formData,
            success: function (response) {
                if (response.success) {
                    window.location.href = response.redirect_url;
                } else {
                    $('#response').html(response.error || "Login failed.");
                }
            },
            error: function () {
                $('#response').html("Something went wrong.");
            }
        });
    });
});
