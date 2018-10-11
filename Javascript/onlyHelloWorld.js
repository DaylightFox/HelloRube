/* 
    Proposed by EdMaxPrime (github) 
    This must be attached to an html document
*/
//This function gets run as soon as the script is loaded
(function() {
    //get body tag
    var body = document.getElementsByTagName("body");
    if(body.length > 0) {body = body[0];}
    //remove all letters that are not present in the phrase Hello World
    body.textContent = body.textContent.replace(/[^helowrd ]/gi, "");
    //append Hello World just in case it wasn't clear enough
    body.textContent += " Hello World";
})();
