$(document).ready(function(){
    loadLocations(); // Get location names
    initializeGrid(); //Initialize the Grid

    $('#campaignName').on('input', function(){
        saveCampaignName();

    });
});

$('#filterButton').click(function(){
    loadEmployees();
});

function saveCampaignName(){
    // get value from campaignName input field
    const campaignName = $('#campaignName').val();
    // save the data from campaignName input field to localStorage
    localStorage.setItem('campaignName',JSON.stringify(campaignName));

    $('#campaignName')[0].reset();

}

function loadLocations(){
    $.ajax({
        url: '/employee/api-get-loc/',
        type: 'GET',
        success: function(response){
            const locations = response.unique_locations;

            const locationSelect = $('#locationSelect');

            locationSelect.empty();

            locationSelect.append(new Option('All Locations','All'));

            locations.forEach(function(location){
                locationSelect.append(new Option(location,location));
            });
        },
        error: function(){
            alert('Error loading locations.');
        }
    });
}
// creating grid columns
let gridApi;

let pageSize;

let selectedEmployees = [];

function loadEmployees(){
    const location = $('#locationSelect').val();
    if (location === "None") {
        gridApi.setGridOption("rowData", rowData);
        return;
    }
    $.ajax({
        url: '/employee/api-get-emp-details/',
        type: 'GET',
        data: { location: location },
        success: function(response) {
            const employees = response.Employee_data;
            totalCount = response.total;
            pageSize = response.page_size;

            gridApi.setGridOption("rowData", employees);

            gridApi.setGridOption("paginationPageSize", pageSize)

        },
        error: function() {
            alert('Error loading employee details.');
        }
    });
}

function onRowSelected(event){
    const selectedNode = event.node;
    const empId = selectedNode.data.emp_id;

    if (selectedNode.__selected) {
        if (!selectedEmployees.some(emp => emp.emp_id === empId)) {
            selectedEmployees.push(event.data);
        }

    }
    updateSelectedEmployeesCount();
}


function updateSelectedEmployeesCount(){
    const totalSelectedCount = selectedEmployees.length;

    // store selected employee data in localStorage
    $('#selectedCount').text(totalSelectedCount);
    localStorage.setItem('selectedEmployees',JSON.stringify(selectedEmployees));
    localStorage.setItem('totalSelectedCount',totalSelectedCount);
}

const columnDefs = [
    {
        headerName: "Employee Name",
        field: "emp_name",
        width: 150
    },
    {
        headerName: "Location",
        field: "emp_location",
        width: 150
    },
    {
        headerName: "Phone Number",
        field: "emp_phone",
        width: 150
    }
];

var paginationPageSize = pageSize;

let rowData = null;

// configuring grid settings and applying pagination
const gridOptions = {
    rowSelection: {
        mode: "multiRow",
        groupSelects: "descendants"
    },
    columnDefs: columnDefs,
    pagination: true,
    paginationPageSize: pageSize,
    paginationPageSizeSelector: [5, 10, 20, 50, 100],
    onGridReady: function() {
        loadEmployees();
    },
    onRowSelected: onRowSelected
};


// creating empty grid
function initializeGrid() {
    const gridDiv = document.getElementById('employeeGrid');
    gridApi = agGrid.createGrid(document.getElementById('employeeGrid'),gridOptions);

     gridApi.setGridOption("rowData", rowData);
}

