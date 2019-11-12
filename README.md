# XSS through file download

<b>Notes (/test1)</b>

1. xss3, xss3.hell, xss3.pdf are all the same file with content: <code><html><script>alert('X_s_S')</script></html></code>

2. xss3 and xss3.hell show XSS only in IE and Edge because of content sniffing. Absence of file extension and unknown file extension in second case provoke IE and Edge to sniff <html> tag and treat it as HTML content resulting in XSS issue.
  
3. xss3.pdf does not result in XSS because it has valid file extension .pdf. IE or Edge does not attempt to guess its content because of valid file extension .pdf.

4. xss4 has XSS payload but it does not exhibit XSS issue. Because it has file signature (Magic Bytes) of PDF. Hence the browser treats it as PDF rather than HTML. However if the XSS payload is moved to line#8, the browser again treats it as HTML and it shows XSS issue. Open the file in text editor to see the location of XSS payload.

<b>Notes (/test2)</b>

1. xss3 and xss3.hell do not show XSS in IE or Edge. Response header <code>[X-Content-Type-Options'] = 'nosniff' </code>is present.

<b>Notes (/test3)</b>

1. xss3.pdf shows XSS issue in Chrome and FireFox although the file type is PDF. Because the application explicitly sets the content type to <code>['Content-Type'] = 'text/html; charset=utf-8'</code>. Because of this content type Chrome and FireFox treat it as HTML content rather than PDF resulting in XSS issue.
