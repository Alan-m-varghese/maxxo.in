import re

def update_cart_in_js():
    with open("products.js", "r", encoding="utf-8") as f:
        js = f.read()
    
    # Replace the old addToCart function with the new advanced one and add cart logic
    old_add_to_cart = r'function addToCart\(\) \{\s*alert\("Product added to cart!"\);\s*\}'
    
    new_cart_logic = """// Cart Logic
function getCart() {
    const cart = localStorage.getItem('maxxo_cart');
    return cart ? JSON.parse(cart) : [];
}

function saveCart(cart) {
    localStorage.setItem('maxxo_cart', JSON.stringify(cart));
    updateCartBadge();
}

function updateCartBadge() {
    const cart = getCart();
    const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
    
    const badges = document.querySelectorAll('.cart-badge');
    badges.forEach(badge => {
        if (totalItems > 0) {
            badge.textContent = totalItems;
            badge.style.display = 'flex';
        } else {
            badge.style.display = 'none';
        }
    });
}

function addToCart() {
    const params = new URLSearchParams(window.location.search);
    const productId = params.get('id');
    const product = getProductById(productId);
    
    if (!product) return;

    const qty = parseInt(document.getElementById('qty-input').value) || 1;
    
    let cart = getCart();
    const existingItem = cart.find(item => item.id === productId);
    
    if (existingItem) {
        existingItem.quantity += qty;
    } else {
        cart.push({
            id: productId,
            name: product.name,
            price: product.offer,
            image: product.images[0],
            quantity: qty
        });
    }
    
    saveCart(cart);
    
    // Visual feedback
    const btn = document.querySelector('.btn-add-cart');
    const originalText = btn.innerHTML;
    btn.innerHTML = '✓ ADDED';
    btn.style.backgroundColor = '#25D366';
    btn.style.borderColor = '#25D366';
    btn.style.color = '#fff';
    
    setTimeout(() => {
        btn.innerHTML = originalText;
        btn.style.backgroundColor = '';
        btn.style.borderColor = '';
        btn.style.color = '';
    }, 2000);
}
"""
    
    if "saveCart(" not in js:
        js = re.sub(old_add_to_cart, new_cart_logic, js)
        
        # Add updateCartBadge to DOMContentLoaded
        js = js.replace("document.addEventListener('DOMContentLoaded', () => {", "document.addEventListener('DOMContentLoaded', () => {\n    updateCartBadge();")
        
        with open("products.js", "w", encoding="utf-8") as f:
            f.write(js)

def add_badge_to_html(filename):
    with open(filename, "r", encoding="utf-8") as f:
        html = f.read()

    # Find the cart button SVG part
    cart_btn_pattern = r'(<button class="icon-btn"[^>]*aria-label="Cart"[^>]*>\s*<svg.*?</svg>\s*</button>)'
    
    replacement = """<div class="cart-btn-wrapper" style="position: relative; display: flex;">
            \\1
            <span class="cart-badge" style="position: absolute; top: 0px; right: 0px; background-color: #ff0000; color: #fff; font-size: 10px; font-weight: 700; width: 16px; height: 16px; border-radius: 50%; display: none; align-items: center; justify-content: center; pointer-events: none;">0</span>
        </div>"""
    
    # We only want to replace it if we haven't already wrapped it
    if 'class="cart-badge"' not in html:
        # We need to escape backreferences in python string for re.sub if we just format it, but using \1 works
        html = re.sub(cart_btn_pattern, replacement, html, flags=re.DOTALL)
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)

update_cart_in_js()
add_badge_to_html("index.html")
add_badge_to_html("product.html")

print("Cart logic added.")
