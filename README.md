# BugPoc Cards XSS Challenge Solution

## Description
This POC is a unintended solution to the challenge that only works in Safari.  The exploit works by extracting the nonce value from the DOM one character at a time using CSS selectors in order to bypass the CSP and exploit an HTML injection vulnerability.  This only works in Safari as that is the only browser (that I'm aware of at least) that leaves the nonce value as an attribute of the script tag.


### Running the POC

* Start the flask server
```
export FLASK_APP=nonce-server.py
flask run
```
* Navigate to http://127.0.0.1:5000/exploit in Safari to trigger the POC.  Ensure that popups are allowed as the exploit code will open a new window.


## Notes

* [SirDarkCat Research on CSP Nonce Bypasses](http://sirdarckcat.blogspot.com/2016/12/how-to-bypass-csp-nonces-with-dom-xss.html)
* [Safari Bug Ticket for Hiding CSP Nonces in DOM](https://bugs.webkit.org/show_bug.cgi?id=179728)
* [HTML Spec on Nonce Attributes](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#nonce-attributes%3Aattr-nonce)