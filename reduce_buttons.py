import re

with open("product.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix .product-actions to allow wrapping
new_actions_css = """        .product-actions {
            display: flex;
            gap: 15px;
            margin-bottom: 30px;
            align-items: center;
            flex-wrap: wrap;
        }"""
html = re.sub(r'\.product-actions\s*\{[^\}]*\}', new_actions_css, html)

# Fix button widths
new_buttons_css = """        .btn-add-cart, .btn-buy-whatsapp {
            height: 56px;
            padding: 0 25px;
            font-size: 14px;
            font-weight: 700;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            /* Removed flex: 1 to prevent excessive stretching */
            min-width: 180px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            text-transform: uppercase;
            letter-spacing: 1px;
            position: relative;
            overflow: hidden;
            white-space: nowrap;
        }"""
html = re.sub(r'\.btn-add-cart,\s*\.btn-buy-whatsapp\s*\{.*?(?=\.btn-add-cart\s*\{)', new_buttons_css + '\n\n', html, flags=re.DOTALL)

with open("product.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Button width reduced.")
