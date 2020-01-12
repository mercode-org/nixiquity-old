{ writeTextFile }:

writeTextFile {
  name = "slideshow-empty";
  text = ''<!doctype html>
<html>
  <head><title>Empty Slideshow</title></head>
  <body><h2>Slideshow is empty. Please do nixiquity.override { slideshowPackage = ...; oemSlideshowPackage = ...; }</h2></body>
</html>
  '';
  destination = "/index.html";
}
