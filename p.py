import pdfkit

# Set the options for the PDF conversion
options = {
	'page-size': 'A4',
	'margin-top': '0mm',
	'margin-right': '0mm',
	'margin-bottom': '0mm',
	'margin-left': '0mm'
}

# Read the HTML file
with open('change_request_form.html', 'r') as f:
	html = f.read()

# Convert the HTML to a PDF
pdfkit.from_string(html, 'change_request_form.pdf', options=options)
