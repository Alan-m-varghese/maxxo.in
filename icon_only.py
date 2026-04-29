import re

with open("product.html", "r", encoding="utf-8") as f:
    html = f.read()

# Remove the text
html = re.sub(r'</svg>\s*Back to Home\s*</a>', '</svg>\n            </a>', html)

# Update the CSS for back-button
new_css = """        .back-button {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 44px;
            height: 44px;
            border-radius: 50%;
            text-decoration: none;
            color: #1a1a1a;
            transition: all 0.2s ease;
            background-color: transparent;
        }
        .back-button:hover {
            transform: translateX(-4px);
            color: #ff0000;
            background-color: #f5f5f5;
        }
        .back-button svg {
            width: 24px;
            height: 24px;
        }"""

html = re.sub(r'\.back-button\s*\{.*?(?=\s*/\* Hide desktop nav)', new_css, html, flags=re.DOTALL)

with open("product.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Icon updated successfully.")
