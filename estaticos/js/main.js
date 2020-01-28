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

