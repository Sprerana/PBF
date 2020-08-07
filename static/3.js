$(document).ready( function () {
    $('#table_id').DataTable({
      "paging": false,
      "searching": false,
      "info": false,
      "scrollX": true,
      "columnDefs": [
        { "width": "300px", "targets": 1}
      ],
    });
} );