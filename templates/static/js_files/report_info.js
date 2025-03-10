$(document).ready(function(){
    initializeReportInfoGrid();
});

let gridApi;

const columnDefs = [
    {
        headerName:"Phone Number",
        field: "",
        width: 150
    },
    {
        headerName: "Delivery Time",
        field: "",
        width: 150
    },
    {
        headerName: "Status",
        field: "",
        width: 150
    }
];

const gridOptions = {
    columnDefs: columnDefs,
    rowData: null,
    domLayout: "autoHeight",
//    onGridReady: function() {
//
//    },
};

function initializeReportInfoGrid() {
    const gridDiv = document.getElementById('reportInfoGrid');
    gridApi = agGrid.createGrid(gridDiv,gridOptions);
}