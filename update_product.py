import re

with open("product.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove hamburger button
html = re.sub(r'<button class="icon-btn hamburger-btn"[^>]*>.*?</button>', '', html, flags=re.DOTALL)

# 2. Remove mobile menu overlay and nav
html = re.sub(r'<div class="mobile-menu-overlay"[^>]*></div>', '', html)
html = re.sub(r'<nav class="mobile-menu" id="mobileMenu">.*?</nav>', '', html, flags=re.DOTALL)

# 3. Remove newsletter section completely
html = re.sub(r'<!-- Newsletter Section -->\s*<section class="newsletter-section">.*?</section>', '', html, flags=re.DOTALL)

# 4. Update the Gallery Section
new_gallery = """        <div class="product-gallery">
            <div class="main-image-wrapper">
                <img id="main-product-image" src="" alt="Product Image">
            </div>
            <div class="product-thumbnails" id="product-thumbnails">
                <!-- Thumbnails will be injected here -->
            </div>
        </div>"""
html = re.sub(r'<div class="product-gallery">\s*<img id="main-product-image"[^>]*>\s*</div>', new_gallery, html)

# 5. Add new CSS for the gallery and buttons
new_css = """
        /* Enhanced Gallery Styles */
        .product-gallery {
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 20px;
            background: transparent;
            box-shadow: none;
            padding: 0;
        }

        .main-image-wrapper {
            background: #fff;
            border-radius: 12px;
            padding: 40px;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: 0 8px 30px rgba(0,0,0,0.04);
            height: 500px;
        }

        .main-image-wrapper img {
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
            transition: transform 0.3s ease;
        }
        
        .main-image-wrapper:hover img {
            transform: scale(1.05);
        }

        .product-thumbnails {
            display: flex;
            gap: 15px;
            justify-content: center;
        }

        .thumbnail {
            width: 80px;
            height: 80px;
            background: #fff;
            border-radius: 8px;
            padding: 10px;
            cursor: pointer;
            border: 2px solid transparent;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            transition: all 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .thumbnail img {
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
        }

        .thumbnail:hover, .thumbnail.active {
            border-color: #ff0000;
            transform: translateY(-2px);
        }

        /* Enhanced Button Styles */
        .btn-add-cart, .btn-buy-whatsapp {
            height: 55px;
            padding: 0 35px;
            font-size: 16px;
            font-weight: 700;
            border-radius: 30px;
            border: none;
            cursor: pointer;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }

        .btn-add-cart {
            background-color: #1a1a1a;
            color: #fff;
        }

        .btn-add-cart:hover {
            background-color: #333;
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        }

        .btn-buy-whatsapp {
            background: linear-gradient(135deg, #25D366, #128C7E);
            color: #fff;
        }

        .btn-buy-whatsapp:hover {
            background: linear-gradient(135deg, #20bd5a, #0e7568);
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(37, 211, 102, 0.3);
        }

        .btn-buy-whatsapp svg {
            width: 24px;
            height: 24px;
            fill: currentColor;
        }
"""
html = html.replace("/* Product Page Specific Styles */", "/* Product Page Specific Styles */" + new_css)

# 6. Update the WhatsApp button HTML to include SVG icon
new_whatsapp_btn = """<button class="btn-buy-whatsapp" onclick="buyNowWhatsApp()">
                    <svg viewBox="0 0 24 24">
                        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z" />
                    </svg>
                    BUY ON WHATSAPP
                </button>"""
html = re.sub(r'<button class="btn-buy-whatsapp" onclick="buyNowWhatsApp\(\)">.*?</button>', new_whatsapp_btn, html)

with open("product.html", "w", encoding="utf-8") as f:
    f.write(html)
