$(function(){
    $('#myTable').DataTable();
    $('#add').on("click", function() {
        $('.vmodal').show();

        $('.modal-close').on("click", function() {
            $('.vmodal').hide();
            $('#myTable').show();
        });

        $('#myTable').hide();
    });
})

