$(function () {
    $(".CaixaMagica").on("keyup", function (e) {
        if (this.value != "") {
            $(".CheckboxMagico").prop("checked", "checked");
        } else {
            $(".CheckboxMagico").prop('checked', "");
        }
    });
});