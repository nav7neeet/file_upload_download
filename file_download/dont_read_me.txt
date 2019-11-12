 ##notes (/test1):
 1. xss3, xss3.hell, xss3.pdf are all the same file. content: <html><script>alert('X_s_S')</script></html>

 2. xss3 and xss3.hell shows xss only in IE and Edge (content sniffing). Absence of file extension and unknown file extension
 in second case provokes IE and Edge to sniff <html> tag and treat it as html content resulting in XSS issue.

 3. xss3.pdf does not result in xss cause it has valid file extension .pdf.
  IE or Edge does not attempt to guess its content because of valid extension .pdf

 4. xss4 has xss payload but it does not exhibit xss issue. Because it has file signature of pdf and hence the browser treats it as pdf rather than html.
 However if the xss payload is moved to line#8, the browser again treats it as html and it shows xss issue. Open the file in text editor to see the location of
 xss payload.

 ##notes (/test2):
 1. xss3 and xss3.hell does not show xss only in IE and Edge. [X-Content-Type-Options'] = 'nosniff' is present.

 ##notes (/test3):
 1. xss3.pdf shows xss issue in chrome and FF although the file type is pdf. Because the application explicitly sets the content type.
 ['Content-Type'] = 'text/html; charset=utf-8'. Because of this content type chrome and FF treats it as html content rather than pdf resulting in xss.
