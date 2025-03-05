$(document).ready(function(){
    initializeReportGrid();

//    window.location.reload();
});



let gridApi;

let rowData = null;

const columnDefs = [
    {
        headerName: "Campaign Name",
        field: "campaign_name",
        width: 150
    },
    {
        headerName:"Date",
        field: "date_of_campaign",
        width: 150
    },
    {
        headerName: "count",
        field: "total_count_of_employees",
        width: 150
    },
    {
        headerName: "Note",
        field: "note_description",
        width: 150
    },
    {
        headerName: "status",
        field: "status",
        width: 150
    }
];

const gridOptions = {
    columnDefs: columnDefs,
    rowData: rowData,
    domLayout: "autoHeight",
    onGridReady: function(){
        loadReports();
    },
};

function loadReports(){
    $.ajax({
        url: '/employee/api-campaign-report/',
        type: 'GET',
        success: function(response) {
            const reports = response.campaign_report;

            gridApi.setGridOption("rowData", [reports]);
        },
        error: function(xhr, status, error) {
                alert('Failed to load report, Try Again.');
        }
    });
}

function initializeReportGrid(){
    const gridReportDiv = document.getElementById('reportGrid');
    gridApi = agGrid.createGrid(gridReportDiv,gridOptions);

    gridApi.setGridOption("rowData",rowData);
}