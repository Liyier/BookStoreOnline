$(document).ready(function() {  
      
    var totalRow = 0;
    $('#orderTable tr').each(function() {
        $(this).find('td:eq(4)').each(function(){
                totalRow += parseFloat($(this).text());
        });  
    });  
      
    $('#orderTal').append('￥'+totalRow);
    $('#orderTal2').append('￥'+totalRow);
});  