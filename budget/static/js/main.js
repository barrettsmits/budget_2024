// button click event, add item modal
function openAddModal(type) {            
    // Populate the modal fields
    
    if (type === 'asset' || type === 'investment') {
        document.getElementById('addItemFrequencyLabel').style.display = 'none';
        document.getElementById('addItemFrequency').style.display = 'none';
    } else {
        document.getElementById('addItemFrequencyLabel').style.display = 'block';
        document.getElementById('addItemFrequency').style.display = 'block';
    }

    $('#addItemType').val(type); 
    
    // Open the modal
    $('#addModal').modal('show');
}

function submitAdd() {
    var type = $('#addItemType').val();
    var description = $('#addItemDescription').val();
    var amount = $('#addItemAmount').val();
    var frequency = $('#addItemFrequency').val();

    $.ajax({
        url: '/add',
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({type: type, description: description, amount: amount, frequency:frequency }),
        success: function(response) {
            // Handle success
            $('#addModal').modal('hide');
            location.reload();
        },
        error: function(xhr, status, error) {
            // Handle error
            console.error("Error in updating item: ", error);
        }
    });
}
// button click event, edit item modal
function openEditModal(type, id, description, amount, frequency) {
    // Populate the modal fields
    $('#itemType').val(type);
    $('#itemId').val(id);
    $('#itemDescription').val(description);
    $('#itemAmount').val(amount.replace(/[$,]/g, ''));
    $('#itemFrequency').val(frequency);

    // Open the modal
    $('#editModal').modal('show');
}

function submitEdit() {
    var type = $('#itemType').val();
    var id = $('#itemId').val();
    var description = $('#itemDescription').val();
    var amount = $('#itemAmount').val();
    var frequency = $('#itemFrequency').val();

    $.ajax({
        url: '/edit/'+ id,
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({type: type, description: description, amount: amount, frequency: frequency}),
        success: function(response) {
            // Handle success
            $('#editModal').modal('hide');
            location.reload();
        },
        error: function(xhr, status, error) {
            // Handle error
            console.error("Error in updating item: ", error);
        }
    });
}
// button even click, delete item modal
function openDeleteModal(type, id, description, amount, frequency) {
    // Set the form action based on the type
    // Populate the modal fields
    $('#deleteItemType').val(type);
    $('#deleteItemId').val(id);
    $('#deleteItemDescription').val(description);
    $('#deleteItemAmount').val(amount.replace(/[$,]/g, ''));
    $('#deleteItemFrequency').val(frequency);

    // Open the modal
    $('#deleteModal').modal('show');
}
function submitDelete(){
    var type = $('#deleteItemType').val();
    var id = $('#deleteItemId').val();

    $.ajax({
        url: '/delete/' + id,
        method: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({type: type, id: id }),
        success: function(response) {
            // Handle success
            $('#deleteModal').modal('hide');
            location.reload();
        },
        error: function(xhr, status, error) {
            // Handle error
            console.error("Error in deleteing item: ", error);
        }
    });
}
