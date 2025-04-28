let gridApi;

let rowData = null;

const columnDefs = [
    {
        headerName: "Campaign Name",
        field: "campaign_name",
        width: 200
    },
    {
        headerName: "Info",
        field: "details"
    },
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
        url: '/my-app/api-campaign-report/',
        type: 'GET',
        success: function(response) {
            const reports = response.campaign_report;

            gridApi.setGridOption("rowData", reports);
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

$(document).ready(function(){
    initializeReportGrid();
});
