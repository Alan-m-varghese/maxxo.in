import re

cart_html = """
    <!-- Cart Drawer -->
    <div class="cart-drawer-overlay" id="cartOverlay" onclick="closeCart()"></div>
    <div class="cart-drawer" id="cartDrawer">
        <div class="cart-header">
            <h2>Your Cart</h2>
            <button class="close-cart-btn" onclick="closeCart()">&times;</button>
        </div>
        <div class="cart-items" id="cartItemsContainer">
            <!-- Items inject here -->
        </div>
        <div class="cart-footer">
            <div class="cart-total">
                <span>Total:</span>
                <span id="cartTotalPrice">₹0</span>
            </div>
            <button class="btn-checkout" onclick="checkoutWhatsApp()">Checkout via WhatsApp</button>
        </div>
    </div>
"""

cart_css = """
        /* Cart Drawer */
        .cart-drawer-overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.5);
            z-index: 1000;
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        .cart-drawer-overlay.active {
            display: block;
            opacity: 1;
        }
        .cart-drawer {
            position: fixed;
            top: 0;
            right: -400px;
            width: 100%;
            max-width: 400px;
            height: 100%;
            background: #fff;
            z-index: 1001;
            box-shadow: -5px 0 25px rgba(0,0,0,0.1);
            transition: right 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            display: flex;
            flex-direction: column;
        }
        .cart-drawer.active {
            right: 0;
        }
        .cart-header {
            padding: 20px 25px;
            border-bottom: 1px solid #eee;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .cart-header h2 {
            font-size: 20px;
            color: #1a1a1a;
            font-weight: 700;
        }
        .close-cart-btn {
            background: none;
            border: none;
            font-size: 28px;
            color: #666;
            cursor: pointer;
            transition: color 0.2s;
            line-height: 1;
        }
        .close-cart-btn:hover {
            color: #ff0000;
        }
        .cart-items {
            flex: 1;
            overflow-y: auto;
            padding: 20px 25px;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        .empty-cart-msg {
            text-align: center;
            color: #888;
            margin-top: 50px;
            font-size: 16px;
        }
        .cart-item {
            display: flex;
            gap: 15px;
            border-bottom: 1px solid #f5f5f5;
            padding-bottom: 20px;
        }
        .cart-item img {
            width: 80px;
            height: 80px;
            object-fit: contain;
            background: #f9f9f9;
            border-radius: 8px;
            padding: 5px;
        }
        .cart-item-details {
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .cart-item-title {
            font-size: 14px;
            font-weight: 600;
            color: #1a1a1a;
            margin-bottom: 5px;
        }
        .cart-item-price {
            color: #ff0000;
            font-weight: 700;
            font-size: 14px;
            margin-bottom: 10px;
        }
        .cart-item-actions {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .cart-item-remove {
            color: #888;
            font-size: 13px;
            text-decoration: underline;
            cursor: pointer;
            background: none;
            border: none;
        }
        .cart-item-remove:hover {
            color: #ff0000;
        }
        .cart-footer {
            padding: 20px 25px;
            border-top: 1px solid #eee;
            background: #fcfcfc;
        }
        .cart-total {
            display: flex;
            justify-content: space-between;
            font-size: 18px;
            font-weight: 700;
            color: #1a1a1a;
            margin-bottom: 20px;
        }
        .btn-checkout {
            width: 100%;
            height: 50px;
            background: linear-gradient(135deg, #25D366, #128C7E);
            color: #fff;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s;
            text-transform: uppercase;
        }
        .btn-checkout:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(37, 211, 102, 0.3);
        }
"""

def inject_to_html(filename):
    with open(filename, "r", encoding="utf-8") as f:
        html = f.read()

    # Clean up double script tag
    html = html.replace('<script src="products.js"></script>\n<script src="products.js"></script>', '<script src="products.js"></script>')

    # Inject CSS before </style>
    if "/* Cart Drawer */" not in html:
        html = html.replace("</style>", cart_css + "\n    </style>")
    
    # Inject HTML before </body>
    if "cartDrawer" not in html:
        html = html.replace('</body>', cart_html + '\n</body>')
        
    # Make cart icon clickable
    html = re.sub(r'<button class="icon-btn"\s*aria-label="Cart"[^>]*>', '<button class="icon-btn" aria-label="Cart" onclick="openCart()">', html)
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

inject_to_html("index.html")
inject_to_html("product.html")

print("Cart drawer fixed.")
