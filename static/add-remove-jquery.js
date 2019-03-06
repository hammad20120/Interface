$(function () {

    $(document).on('click', '.addRow', function () {
        var myRow = $(this).parents('tr').clone();
        var index = $(this).parents('tr').index();



        var categoryData = $(this).closest('tr').find('#catid').find("#catselect option:selected").val();
        var polarityData = $(this).closest('tr').find('#polid').find("#polselect option:selected").val();
        var textData = $(this).closest('tr').find('#textid').text();
        var revData = $(this).closest('tr').find('#revid').text();


        myRow.closest('tr').find('#catid').find("#catselect").val(categoryData);
        myRow.closest('tr').find('#polid').find("#polselect").val(polarityData);


        $('#thetable > tbody > tr').eq(index).after(myRow);

    });

    $(document).on('click', '.remove', function () {
        $(this).parents('tr').remove();

    });
})
