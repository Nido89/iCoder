var script = document.createElement('script');
script.type = 'text/javascript';
script.src = "https://cdn.ckeditor.com/4.15.0/full-all/ckeditor.js"
document.head.appendChild(script);

script.onload= function(){
   CKEDITOR.replace( 'id_content' );
}

