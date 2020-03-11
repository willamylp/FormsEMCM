
$(function () {
    $(".CaixaMagica").on("keyup", function (e) {
        if (this.value != "") {
            $(".CheckboxMagico").prop("checked", "checked");
        } else {
            $(".CheckboxMagico").prop('checked', "");
        }
    });

    $(".CaixaMagica2").on("keyup", function (e) {
        if (this.value != "") {
            $(".CheckboxMagico2").prop("checked", "checked");
        } else {
            $(".CheckboxMagico2").prop('checked', "");
        }
    });
    $(".CaixaMagica3").on("keyup", function (e) {
        if (this.value != "") {
            $(".CheckboxMagico3").prop("checked", "checked");
        } else {
            $(".CheckboxMagico3").prop('checked', "");
        }
    });
    $(".CaixaMagica4").on("keyup", function (e) {
        if (this.value != "") {
            $(".CheckboxMagico4").prop("checked", "checked");
        } else {
            $(".CheckboxMagico4").prop('checked', "");
        }
    });
    $(".CaixaMagica5").on("keyup", function (e) {
        if (this.value != "") {
            $(".CheckboxMagico5").prop("checked", "checked");
        } else {
            $(".CheckboxMagico5").prop('checked', "");
        }
    });
    $(".CaixaMagica6").on("keyup", function (e) {
        if (this.value != "") {
            $(".CheckboxMagico6").prop("checked", "checked");
        } else {
            $(".CheckboxMagico6").prop('checked', "");
        }
    });
    $(".CaixaMagica7").on("keyup", function (e) {
        if (this.value != "") {
            $(".CheckboxMagico7").prop("checked", "checked");
        } else {
            $(".CheckboxMagico7").prop('checked', "");
        }
    });
    $(".CaixaMagica8").on("keyup", function (e) {
        if (this.value != "") {
            $(".CheckboxMagico8").prop("checked", "checked");
        } else {
            $(".CheckboxMagico8").prop('checked', "");
        }
    });
});
function ConfirmarDelete(valor) {
    swalWithBootstrapButtons = swal.mixin({
        confirmButtonClass: 'btn btn-danger',
        cancelButtonClass: 'btn btn-success',
        confirmButtonColor: '#d33',
        cancelButtonColor: '#17a2b8',
        buttonsStyling: true,
    })
    swalWithBootstrapButtons({
        title: 'Você tem certeza?',
        text: "Você não poderá reverter isso!",
        type: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Sim, Deletar!',
        cancelButtonText: 'Não, Cancelar!',
        reverseButtons: true
    }).then((result) => {
        if (result.value) {
            swalWithBootstrapButtons(
                'Deletado!',
                'REGISTRO DELETADO COM SUCESSO!',
                'success'
            )
            var url;
            var urlAtual = window.location.href;
            var urlAtual = urlAtual.split('/');
            if (urlAtual.length > 6) {
                url = '../../DeletarHost/' + valor;
            } else {
                url = '../DeletarHost/' + valor;
            }
            location.href = url;
        } else if (
            result.dismiss === swal.DismissReason.cancel
        ) {
            swalWithBootstrapButtons(
                'Cancelado!',
                'O REGISTRO NÃO FOI DELETADO!',
                'error'
            )
        }
    })
}
