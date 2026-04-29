import re

with open("product.html", "r", encoding="utf-8") as f:
    html = f.read()

back_btn_html = """        <div class="header-left">
            <a href="index.html" class="back-button">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <line x1="19" y1="12" x2="5" y2="12"></line>
                    <polyline points="12 19 5 12 12 5"></polyline>
                </svg>
                Back to Home
            </a>"""

html = html.replace('<div class="header-left">', back_btn_html, 1)

back_btn_css = """
        .back-button {
            display: flex;
            align-items: center;
            gap: 6px;
            text-decoration: none;
            color: #1a1a1a;
            font-weight: 700;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            transition: all 0.2s ease;
        }
        .back-button:hover {
            transform: translateX(-4px);
            color: #ff0000;
        }
        .back-button svg {
            width: 18px;
            height: 18px;
        }
        
        /* Hide desktop nav on product page if needed, but it's okay to keep */
"""

html = html.replace('/* Product Page Specific Styles */', '/* Product Page Specific Styles */\n' + back_btn_css)

with open("product.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Back button added.")
