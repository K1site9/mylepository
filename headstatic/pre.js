$(function(){
    $('pre').addClass('prettyprint linenums');
});

//const htmlEscape = (str) => {
//    if (!str) return;
//    return str.replace(/[<>&"'`]/g, (match) => {
//        const escape = {
//            '<': '&lt;',
//            '>': '&gt;',
//            '&': '&amp;',
//            '"': '&quot;',
//            "'": '&#39;',
//            '`': '&#x60;'
//        };
//        return escape[match];
//    });
//}
//
//document.querySelectorAll('pre').forEach(pre =>{
//    pre.innerText = htmlEscape(pre.innerText)
//})
