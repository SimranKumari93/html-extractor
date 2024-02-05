from bs4 import BeautifulSoup

# Example HTML content (replace with your actual HTML content)
html_content = """
<html>
<head><title>Example</title></head>
<body>
<h1>Hello, BeautifulSoup!</h1>
<p>This is a paragraph.</p>
<img src="image.jpg" alt="Image">
<table>
<tr><td>Row 1, Column 1</td><td>Row 1, Column 2</td></tr>
<tr><td>Row 2, Column 1</td><td>Row 2, Column 2</td></tr>
</table>
</body>
</html>
"""

# Parse HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract text
text = soup.get_text()

# Extract images (replace 'image.jpg' with actual image URL)
images = [img['src'] for img in soup.find_all('img')]

# Extract tables
tables = []
for table in soup.find_all('table'):
    rows = []
    for row in table.find_all('tr'):
        cells = [cell.get_text(strip=True) for cell in row.find_all('td')]
        rows.append(cells)
    tables.append(rows)

# Print extracted data
print("Extracted Text:")
print(text)
print("\nExtracted Images:")
print(images)
print("\nExtracted Tables:")
for table in tables:
    print(table)
