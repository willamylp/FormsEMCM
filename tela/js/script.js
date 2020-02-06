$(function(){
    $(".CaixaMagica").keyup(function(){
        if($(this).val().length > 0){
            $(this).parent().parent().find(".CheckboxMagico").prop("checked", true);
        } else {
            $(this).parent().parent().find(".CheckboxMagico").prop("checked", false);
        }
    });
});