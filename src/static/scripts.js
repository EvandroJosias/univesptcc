document.addEventListener('DOMContentLoaded', (event) => {
    console.log("JavaScript carregado e funcionando");

    // Verifica se o cookie 'usuario' está presente
    let usuarioCookie = getCookie('usuario');
    if( usuarioCookie ) {
       // alert( 'Os cookies estao rodando. Valor do cookie: ' + usuarioCookie );
    } else {
        windows.location.href='/busca';
    }
});


function getCookie(k) {
    var cookies = " " + document.cookie;
    var key = " " + k + "=";
    var start = cookies.indexOf(key);

    if (start === -1) return null;

    var pos = start + key.length;
    var last = cookies.indexOf(";", pos);

    if (last !== -1) return cookies.substring(pos, last);

    return cookies.substring(pos);
};

function setCookie(k, v, expira, path) {
    if (!path) path = "/";

    var d = new Date();
    d.setTime(d.getTime() + (expira * 1000));

    document.cookie = encodeURIComponent(k) + "=" + encodeURIComponent(v) + "; expires=" + d.toUTCString() + "; path=" + path;
};