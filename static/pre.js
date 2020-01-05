$(function(){
    $('pre').addClass('prettyprint linenums');
});

(function() {
  let objs = document.getElementsByClassName('html-code');
  for (let i = 0; i < objs.length; i++) {
      objs[i].innerHTML = objs[i].innerHTML
      .replace(/<!--|-->/g, '')
      .replace(/<comment>([\s\S]*?)<\/comment>/g, '<!-- $1 -->')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
  }
})();