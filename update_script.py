import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Create product.html
head_match = re.search(r'(<head>.*?</style>)', html, re.DOTALL)
header_match = re.search(r'(<header.*?</nav>)', html, re.DOTALL)
footer_match = re.search(r'(<!-- Newsletter Section -->.*?</html>)', html, re.DOTALL)

product_styles = """
        /* Product Page Specific Styles */
        .product-page-section {
            max-width: 1200px;
            margin: 40px auto;
            padding: 0 40px;
            display: flex;
            gap: 50px;
            min-height: 60vh;
        }

        .product-gallery {
            flex: 1;
            background: #fff;
            border-radius: 8px;
            padding: 30px;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.03);
            position: relative;
        }

        .product-gallery img {
            max-width: 100%;
            max-height: 500px;
            object-fit: contain;
        }

        .product-details-content {
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .breadcrumb {
            font-size: 14px;
            color: #888;
            margin-bottom: 15px;
        }
        
        .breadcrumb a {
            color: #ff0000;
            text-decoration: none;
        }

        .product-title-large {
            font-size: 32px;
            font-weight: 800;
            color: #1a1a1a;
            margin-bottom: 10px;
        }

        .product-reviews {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 20px;
            font-size: 14px;
            color: #666;
        }

        .stars {
            color: #f5b301;
            letter-spacing: 2px;
        }

        .product-price-section {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 25px;
            padding-bottom: 25px;
            border-bottom: 1px solid #eee;
        }

        .price-offer {
            font-size: 32px;
            font-weight: 700;
            color: #ff0000;
        }

        .price-mrp {
            font-size: 18px;
            color: #888;
            text-decoration: line-through;
        }

        .price-gst {
            font-size: 14px;
            color: #666;
        }

        .discount-badge {
            background-color: #f24b18;
            color: #fff;
            font-size: 13px;
            font-weight: 700;
            padding: 4px 8px;
            border-radius: 4px;
        }

        .product-description {
            font-size: 16px;
            line-height: 1.6;
            color: #444;
            margin-bottom: 25px;
        }

        .product-features-list {
            margin-bottom: 30px;
        }

        .product-features-list h3 {
            font-size: 18px;
            margin-bottom: 15px;
            color: #222;
        }

        .product-features-list ul {
            list-style: none;
        }

        .product-features-list li {
            position: relative;
            padding-left: 25px;
            margin-bottom: 10px;
            font-size: 15px;
            color: #444;
        }

        .product-features-list li::before {
            content: '✔';
            position: absolute;
            left: 0;
            top: 0;
            color: #ff0000;
            font-weight: bold;
        }

        .product-actions {
            display: flex;
            gap: 15px;
            margin-bottom: 30px;
            align-items: center;
        }

        .quantity-selector {
            display: flex;
            align-items: center;
            border: 1px solid #ddd;
            border-radius: 4px;
            overflow: hidden;
            height: 50px;
        }

        .quantity-selector button {
            background: #f5f5f5;
            border: none;
            width: 40px;
            height: 100%;
            font-size: 18px;
            cursor: pointer;
            transition: background 0.2s;
        }

        .quantity-selector button:hover {
            background: #e0e0e0;
        }

        .quantity-selector input {
            width: 50px;
            height: 100%;
            border: none;
            text-align: center;
            font-size: 16px;
            font-weight: 600;
        }

        .btn-add-cart, .btn-buy-whatsapp {
            height: 50px;
            padding: 0 30px;
            font-size: 16px;
            font-weight: 700;
            border-radius: 25px;
            border: none;
            cursor: pointer;
            transition: all 0.2s;
            flex: 1;
        }

        .btn-add-cart {
            background-color: #1a365d;
            color: #fff;
        }

        .btn-add-cart:hover {
            background-color: #112642;
            transform: translateY(-2px);
        }

        .btn-buy-whatsapp {
            background-color: #ff0000;
            color: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }

        .btn-buy-whatsapp:hover {
            background-color: #cc0000;
            transform: translateY(-2px);
        }

        .product-extra-info {
            display: flex;
            flex-direction: column;
            gap: 12px;
            padding-top: 25px;
            border-top: 1px solid #eee;
        }

        .info-item {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 14px;
            color: #555;
            font-weight: 500;
        }

        @media (max-width: 900px) {
            .product-page-section {
                flex-direction: column;
                padding: 0 20px;
                margin: 20px auto;
                gap: 30px;
            }

            .product-actions {
                flex-direction: column;
            }

            .btn-add-cart, .btn-buy-whatsapp {
                width: 100%;
            }
        }
"""

new_head = head_match.group(1).replace("</style>", product_styles + "\n    </style>")

product_body = """
    <section class="product-page-section">
        <div class="product-gallery">
            <img id="main-product-image" src="" alt="Product Image">
        </div>
        <div class="product-details-content">
            <div class="breadcrumb">
                <a href="index.html">Home</a> / <a href="index.html#products">Shop</a> / <span id="breadcrumb-name">Product</span>
            </div>
            <h1 id="product-name" class="product-title-large">Product Name</h1>
            <div class="product-reviews">
                <span class="stars">★★★★★</span>
                <span id="review-count">(0 reviews)</span>
            </div>
            <div class="product-price-section">
                <span id="product-offer" class="price-offer"></span>
                <span id="product-mrp" class="price-mrp"></span>
                <span class="price-gst">Incl. GST</span>
                <span id="product-discount" class="discount-badge"></span>
            </div>
            
            <p id="product-description" class="product-description"></p>
            
            <div class="product-features-list">
                <h3>Key Features:</h3>
                <ul id="product-features">
                </ul>
            </div>
            
            <div class="product-actions">
                <div class="quantity-selector">
                    <button onclick="updateQty(-1)">-</button>
                    <input type="text" id="qty-input" value="1" readonly>
                    <button onclick="updateQty(1)">+</button>
                </div>
                <button class="btn-add-cart" onclick="addToCart()">ADD TO CART</button>
                <button class="btn-buy-whatsapp" onclick="buyNowWhatsApp()">BUY ON WHATSAPP</button>
            </div>
            
            <div class="product-extra-info">
                <div class="info-item">
                    <span>🚚</span> Free Delivery Over INR 999
                </div>
                <div class="info-item">
                    <span>🛡️</span> 100% Secure Payment
                </div>
            </div>
        </div>
    </section>
"""

new_footer = footer_match.group(1).replace("</body>", '<script src="products.js"></script>\n</body>')

product_html = f'''<!DOCTYPE html>
<html lang="en">
{new_head}
</head>
<body>
{header_match.group(1)}

{product_body}

{new_footer}
'''

with open("product.html", "w", encoding="utf-8") as f:
    f.write(product_html)


# 2. Update index.html
products_grid_replacement = """        <div class="product-grid" id="product-grid">
            <!-- Product 1 -->
            <a href="product.html?id=premium-kit" class="product-card" style="text-decoration: none; color: inherit;">
                <div class="product-image-container">
                    <div class="badge-discount">-45%</div>
                    <img src="images/premium_kit_maxxo.png" alt="MAXXO Premium Kit">
                </div>
                <div class="product-info" style="align-items: center; padding: 0 15px;">
                    <h3 class="product-title">MAXXO Premium Kit</h3>
                    <div class="product-pricing">
                        <span class="product-mrp">₹2399.00</span>
                        <span class="product-offer">₹1299.00</span>
                        <span class="product-gst">Incl. GST</span>
                    </div>
                    <button class="btn-buy-now" style="margin-top: 15px; margin-bottom: 15px;">VIEW DETAILS</button>
                </div>
            </a>

            <!-- Product 2 -->
            <a href="product.html?id=basic-kit" class="product-card" style="text-decoration: none; color: inherit;">
                <div class="product-image-container">
                    <div class="badge-discount">-23%</div>
                    <img src="images/basic_kit_maxxo.png" alt="MAXXO Basic Kit">
                </div>
                <div class="product-info" style="align-items: center; padding: 0 15px;">
                    <h3 class="product-title">MAXXO Basic Kit</h3>
                    <div class="product-pricing">
                        <span class="product-mrp">₹1299.00</span>
                        <span class="product-offer">₹999.00</span>
                        <span class="product-gst">Incl. GST</span>
                    </div>
                    <button class="btn-buy-now" style="margin-top: 15px; margin-bottom: 15px;">VIEW DETAILS</button>
                </div>
            </a>

            <!-- Product 3 -->
            <a href="product.html?id=black-guard" class="product-card" style="text-decoration: none; color: inherit;">
                <div class="product-image-container">
                    <img src="images/black_guard_maxxo.png" alt="MAXXO Black Guard">
                </div>
                <div class="product-info" style="align-items: center; padding: 0 15px;">
                    <h3 class="product-title">MAXXO Black Guard</h3>
                    <div class="product-pricing">
                        <span class="product-offer">₹499.00</span>
                        <span class="product-gst">Incl. GST</span>
                    </div>
                    <button class="btn-buy-now" style="margin-top: 15px; margin-bottom: 15px;">VIEW DETAILS</button>
                </div>
            </a>

            <!-- Product 4 -->
            <a href="product.html?id=microfiber-cloth" class="product-card" style="text-decoration: none; color: inherit;">
                <div class="product-image-container">
                    <img src="images/microfiber_maxxo.png" alt="MAXXO 1200 GSM Cloth">
                </div>
                <div class="product-info" style="align-items: center; padding: 0 15px;">
                    <h3 class="product-title">MAXXO 1200 GSM Cloth</h3>
                    <div class="product-pricing">
                        <span class="product-offer">₹399.00</span>
                        <span class="product-gst">Incl. GST</span>
                    </div>
                    <button class="btn-buy-now" style="margin-top: 15px; margin-bottom: 15px;">VIEW DETAILS</button>
                </div>
            </a>

            <!-- Product 5 -->
            <a href="product.html?id=foam-spray-bottle" class="product-card" style="text-decoration: none; color: inherit;">
                <div class="product-image-container">
                    <img src="images/foam_spray_bottle_maxxo.png" alt="MAXXO Foam Spray Bottle">
                </div>
                <div class="product-info" style="align-items: center; padding: 0 15px;">
                    <h3 class="product-title">MAXXO Foam Spray Bottle</h3>
                    <div class="product-pricing">
                        <span class="product-offer">₹799.00</span>
                        <span class="product-gst">Incl. GST</span>
                    </div>
                    <button class="btn-buy-now" style="margin-top: 15px; margin-bottom: 15px;">VIEW DETAILS</button>
                </div>
            </a>
        </div>"""

html = re.sub(r'<div class="product-grid">.*?</div>\s*</section>', products_grid_replacement + '\n    </section>', html, flags=re.DOTALL)

# Add products.js to index.html as well
if '<script src="products.js"></script>' not in html:
    html = html.replace("</body>", '<script src="products.js"></script>\n</body>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updates applied successfully.")
