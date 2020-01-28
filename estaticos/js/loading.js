function loading(opcao) {
    if (opcao == 'login') {
        setTimeout(function () {
            window.location.href = "../principal";
        }, 2500);
    }
    else {
        setTimeout(function () {
            window.location.href = "../logout";
        }, 2500);
    }
}