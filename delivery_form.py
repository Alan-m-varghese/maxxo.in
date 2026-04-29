import re

modal_html = """
    <!-- Delivery Modal -->
    <div class="modal-overlay" id="deliveryModalOverlay" onclick="closeDeliveryForm()"></div>
    <div class="delivery-modal" id="deliveryModal">
        <div class="modal-header">
            <h2>Delivery Details</h2>
            <button class="close-modal-btn" onclick="closeDeliveryForm()">&times;</button>
        </div>
        <form class="delivery-form" id="deliveryForm" onsubmit="submitDeliveryForm(event)">
            <input type="hidden" id="checkoutSource" value="">
            
            <div class="form-group">
                <label>Name *</label>
                <input type="text" id="dfName" required placeholder="Full Name">
            </div>
            <div class="form-group">
                <label>Address *</label>
                <textarea id="dfAddress" required rows="2" placeholder="House No, Street, Area"></textarea>
            </div>
            <div class="form-row">
                <div class="form-group">
                    <label>Place *</label>
                    <input type="text" id="dfPlace" required placeholder="Locality/Village">
                </div>
                <div class="form-group">
                    <label>Landmark</label>
                    <input type="text" id="dfLandmark" placeholder="Near Hospital, etc.">
                </div>
            </div>
            <div class="form-row">
                <div class="form-group">
                    <label>City *</label>
                    <input type="text" id="dfCity" required>
                </div>
                <div class="form-group">
                    <label>District & State *</label>
                    <input type="text" id="dfState" required>
                </div>
            </div>
            <div class="form-row">
                <div class="form-group">
                    <label>Pin Code *</label>
                    <input type="text" id="dfPin" required>
                </div>
                <div class="form-group">
                    <label>Contact Number *</label>
                    <input type="tel" id="dfPhone" required>
                </div>
            </div>
            <div class="form-row">
                <div class="form-group">
                    <label>Alternate Number</label>
                    <input type="tel" id="dfAltPhone">
                </div>
                <div class="form-group">
                    <label>Payment Method *</label>
                    <select id="dfPayment" required>
                        <option value="COD">Cash on Delivery (COD)</option>
                        <option value="PREPAID">Prepaid</option>
                    </select>
                </div>
            </div>
            
            <button type="submit" class="btn-submit-order">
                <svg viewBox="0 0 24 24">
                    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z" />
                </svg>
                Send Order to WhatsApp
            </button>
        </form>
    </div>
"""

modal_css = """
        /* Delivery Modal */
        .modal-overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.6);
            backdrop-filter: blur(4px);
            z-index: 2000;
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        .modal-overlay.active {
            display: block;
            opacity: 1;
        }
        .delivery-modal {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -40%);
            width: 90%;
            max-width: 600px;
            background: #fff;
            z-index: 2001;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            max-height: 90vh;
            display: flex;
            flex-direction: column;
        }
        .delivery-modal.active {
            transform: translate(-50%, -50%);
            opacity: 1;
            visibility: visible;
        }
        .modal-header {
            padding: 20px 25px;
            border-bottom: 1px solid #eee;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .modal-header h2 {
            font-size: 20px;
            color: #1a1a1a;
            font-weight: 700;
            margin: 0;
        }
        .close-modal-btn {
            background: none;
            border: none;
            font-size: 28px;
            color: #888;
            cursor: pointer;
            line-height: 1;
        }
        .close-modal-btn:hover {
            color: #ff0000;
        }
        .delivery-form {
            padding: 25px;
            overflow-y: auto;
            flex: 1;
        }
        .form-row {
            display: flex;
            gap: 15px;
        }
        .form-row .form-group {
            flex: 1;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            font-size: 13px;
            font-weight: 600;
            color: #444;
            margin-bottom: 6px;
        }
        .form-group input, .form-group textarea, .form-group select {
            width: 100%;
            padding: 12px 15px;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-size: 14px;
            font-family: inherit;
            transition: border-color 0.2s;
            background: #fafafa;
        }
        .form-group input:focus, .form-group textarea:focus, .form-group select:focus {
            outline: none;
            border-color: #1a1a1a;
            background: #fff;
        }
        .btn-submit-order {
            width: 100%;
            height: 55px;
            background: linear-gradient(135deg, #25D366, #128C7E);
            color: #fff;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s;
            text-transform: uppercase;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            margin-top: 15px;
        }
        .btn-submit-order:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(37, 211, 102, 0.3);
        }
        .btn-submit-order svg {
            width: 22px;
            height: 22px;
            fill: currentColor;
        }
        @media (max-width: 600px) {
            .form-row {
                flex-direction: column;
                gap: 0;
            }
        }
"""

def inject_delivery_form(filename):
    with open(filename, "r", encoding="utf-8") as f:
        html = f.read()

    if "/* Delivery Modal */" not in html:
        html = html.replace("</style>", modal_css + "\n    </style>")
    
    if "deliveryModal" not in html:
        html = html.replace('</body>', modal_html + '\n</body>')
        
    # Replace the buy on whatsapp buttons in product.html and products.js
    if filename == "product.html":
        html = re.sub(r'onclick="buyNowWhatsApp\(\)"', 'onclick="openDeliveryForm(\'product\')"', html)
        
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

inject_delivery_form("index.html")
inject_delivery_form("product.html")

# Update JS Logic
with open("products.js", "r", encoding="utf-8") as f:
    js = f.read()

# Replace the checkoutWhatsApp in cart logic to use openDeliveryForm
js = re.sub(r'function checkoutWhatsApp\(\) \{.*?(?=\n\nfunction|\Z)', '', js, flags=re.DOTALL)
# Also remove the buyNowWhatsApp if it exists
js = re.sub(r'function buyNowWhatsApp\(\) \{.*?(?=\n\nfunction|\Z)', '', js, flags=re.DOTALL)

modal_js = """
function checkoutWhatsApp() {
    openDeliveryForm('cart');
}

function openDeliveryForm(source) {
    if (source === 'cart') {
        const cart = getCart();
        if (cart.length === 0) {
            alert("Your cart is empty.");
            return;
        }
        // Close cart drawer so it's out of the way
        closeCart();
    }
    
    document.getElementById('checkoutSource').value = source;
    document.getElementById('deliveryModalOverlay').classList.add('active');
    document.getElementById('deliveryModal').classList.add('active');
}

function closeDeliveryForm() {
    document.getElementById('deliveryModalOverlay').classList.remove('active');
    document.getElementById('deliveryModal').classList.remove('active');
}

function submitDeliveryForm(event) {
    event.preventDefault();
    
    const source = document.getElementById('checkoutSource').value;
    let packageInfo = "";
    let total = 0;

    if (source === 'cart') {
        const cart = getCart();
        packageInfo = "*PACKAGE*\\n";
        cart.forEach(item => {
            packageInfo += `- ${item.quantity}x ${item.name} (${item.price} each)\\n`;
            const priceNum = parseFloat(item.price.replace(/[^0-9.-]+/g,""));
            total += priceNum * item.quantity;
        });
        packageInfo += `\\n*Total: ₹${total.toFixed(2)}*\\n\\n`;
    } else if (source === 'product') {
        const params = new URLSearchParams(window.location.search);
        const productId = params.get('id');
        const product = getProductById(productId);
        
        const qtyInput = document.getElementById('qty-input');
        const qty = qtyInput ? qtyInput.value : 1;
        
        if (product) {
            packageInfo = "*PACKAGE*\\n";
            packageInfo += `- ${qty}x ${product.name} (${product.offer} each)\\n`;
            const priceNum = parseFloat(product.offer.replace(/[^0-9.-]+/g,""));
            total = priceNum * parseInt(qty);
            packageInfo += `\\n*Total: ₹${total.toFixed(2)}*\\n\\n`;
        }
    }

    const name = document.getElementById('dfName').value;
    const address = document.getElementById('dfAddress').value;
    const place = document.getElementById('dfPlace').value;
    const landmark = document.getElementById('dfLandmark').value;
    const city = document.getElementById('dfCity').value;
    const state = document.getElementById('dfState').value;
    const pin = document.getElementById('dfPin').value;
    const phone = document.getElementById('dfPhone').value;
    const altPhone = document.getElementById('dfAltPhone').value;
    const payment = document.getElementById('dfPayment').value;

    const message = `${packageInfo}🔖Name:- ${name}
🔖Address: ${address}
🔖Place:- ${place}
🔖Landmark:- ${landmark}
🔖City:- ${city}
🔖District &State:- ${state}
🔖Pin Code:- ${pin}
🔖Contact Number:- ${phone}
🔖alternate mobile number:- ${altPhone}
*🔖COD/PREPAID:- ${payment}*`;

    const phoneNum = "919061432885";
    const url = `https://wa.me/${phoneNum}?text=${encodeURIComponent(message)}`;
    window.open(url, '_blank');
    
    closeDeliveryForm();
    
    // Optional: Clear cart after successful checkout intent
    if (source === 'cart') {
        saveCart([]);
        renderCartItems();
    }
}
"""

if "function openDeliveryForm(" not in js:
    with open("products.js", "w", encoding="utf-8") as f:
        f.write(js + "\n" + modal_js)

print("Delivery form integrated successfully.")
