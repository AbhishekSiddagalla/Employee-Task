$(document).ready(function(){

    //get the selected employees and count
    const totalSelectedCount = JSON.parse(localStorage.getItem('totalSelectedCount')) || 0;
    const selectedEmployeeId = JSON.parse(localStorage.getItem('selectedEmployees'));
    const campaignName = JSON.parse(localStorage.getItem('campaignName'));
    // update the total count in preview page
    $('#selectedCount').text(totalSelectedCount);
    $('#campaignName').text(campaignName);

    //give functionality to send button
    $('#sendButton').on('click',function(){
        var note = $('#note').val();
        var docFile = $('#document').prop("files")[0];


        // validating note
        if(!note){
            alert("Note is Empty. Please fill in the Note.");
        }

        var formData = new FormData();
        formData.append("campaign_name", campaignName);
        formData.append("total_count_of_employees", totalSelectedCount);
        formData.append("note_description", note);
        formData.append("document", docFile);
        formData.append("phone_numbers",selectedEmployeeId)
        // get csrf token value
        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        // make an Ajax call to post data to API
        $.ajax({
            url:"/employee/api-add-campaign/",
            type: "POST",
            data: formData,
            contentType: false,
            processData: false,
            headers: {
                'X-CSRFToken': csrfToken
            },
            success: function(response){
                alert(" Note Sent Successfully.");
                $('#add-campaign-form')[0].reset();
            },
            error: function(xhr, status, error) {
                alert('Failed to Send Note, Try Again.');
            }
        });
    });

});
