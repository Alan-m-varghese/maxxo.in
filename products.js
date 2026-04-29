const products = [
    {
        id: "premium-kit",
        name: "MAXXO Premium Kit",
        mrp: "₹2399.00",
        offer: "₹1299.00",
        discount: "-45%",
        images: ["images/premium_kit_maxxo.png"],
        features: [
            "2L High Pressure Foam Sprayer",
            "200ml Ceramic Shampoo",
            "800 GSM Ultra Soft Microfiber Cloth",
            "XL Premium Wash Glove"
        ],
        description: "The MAXXO Premium Kit is your complete solution for professional-level car care at home. This all-in-one kit provides everything you need to achieve a showroom shine while protecting your vehicle's paintwork.",
        reviews: { rating: 4.8, count: 124 },
        inStock: true
    },
    {
        id: "basic-kit",
        name: "MAXXO Basic Kit",
        mrp: "₹1299.00",
        offer: "₹999.00",
        discount: "-23%",
        images: ["images/basic_kit_maxxo.png"],
        features: [
            "2L Foam Sprayer",
            "200ml Shampoo",
            "Microfiber Cloth FREE"
        ],
        description: "The MAXXO Basic Kit offers essential car care tools for your regular maintenance washes. High-quality basics for a clean and shiny vehicle.",
        reviews: { rating: 4.6, count: 85 },
        inStock: true
    },
    {
        id: "black-guard",
        name: "MAXXO Black Guard",
        mrp: "",
        offer: "₹499.00",
        discount: "",
        images: ["images/black_guard_maxxo.jpg"],
        features: [
            "Restores Shine to Plastic Trim",
            "UV Protection",
            "Lasting Results"
        ],
        description: "MAXXO Black Guard easily restores faded plastic, rubber, and vinyl trims back to their original deep black finish while offering long-lasting UV protection against future fading.",
        reviews: { rating: 4.9, count: 210 },
        inStock: true
    },
    {
        id: "microfiber-cloth",
        name: "MAXXO 1200 GSM Cloth",
        mrp: "",
        offer: "₹399.00",
        discount: "",
        images: ["images/microfiber_maxxo.png", "images/microfiber.png"],
        features: [
            "Ultra Soft & Scratch-Free",
            "High Water Absorption",
            "Dual Side Thick Fiber",
            "Perfect for Car & Bike"
        ],
        description: "Experience swirl-free drying and detailing with our ultra-plush 1200 GSM Microfiber Cloth. Designed to absorb maximum water and buff away waxes effortlessly.",
        reviews: { rating: 4.7, count: 340 },
        inStock: true
    },
    {
        id: "foam-spray-bottle",
        name: "MAXXO Foam Spray Bottle",
        mrp: "",
        offer: "₹799.00",
        discount: "",
        images: ["images/foam_spray_bottle_maxxo.jpg"],
        features: [
            "2L High Pressure",
            "Thick Foam Output",
            "Adjustable Nozzle",
            "Easy Pump Action",
            "Strong & Durable Build"
        ],
        description: "Generate thick, clinging snow foam without a pressure washer. The MAXXO Foam Spray Bottle provides high-pressure foam action with a simple hand pump.",
        reviews: { rating: 4.5, count: 95 },
        inStock: true
    }
];

function getProductById(id) {
    return products.find(p => p.id === id);
}

function updateQty(change) {
    const input = document.getElementById('qty-input');
    let newVal = parseInt(input.value) + change;
    if (newVal < 1) newVal = 1;
    input.value = newVal;
}

// Cart Logic
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




function changeMainImage(imgSrc, element) {
    document.getElementById('main-product-image').src = imgSrc;
    
    // Update active thumbnail styling
    document.querySelectorAll('.thumbnail').forEach(thumb => {
        thumb.classList.remove('active');
    });
    if (element) {
        element.classList.add('active');
    }
}

// Initialization for the product page
document.addEventListener('DOMContentLoaded', () => {
    updateCartBadge();
    // Only run if we are on the product page
    if (!document.getElementById('product-name')) return;

    const params = new URLSearchParams(window.location.search);
    const productId = params.get('id');
    
    if (!productId) {
        document.querySelector('.product-page-section').innerHTML = '<h2>Product not found</h2>';
        return;
    }

    const product = getProductById(productId);
    
    if (!product) {
        document.querySelector('.product-page-section').innerHTML = '<h2>Product not found</h2>';
        return;
    }

    // Populate data
    document.title = `MAXXO - ${product.name}`;
    document.getElementById('product-name').textContent = product.name;
    document.getElementById('breadcrumb-name').textContent = product.name;
    
    // Initialize gallery
    document.getElementById('main-product-image').src = product.images[0];
    document.getElementById('main-product-image').alt = product.name;
    
    const thumbnailsContainer = document.getElementById('product-thumbnails');
    thumbnailsContainer.innerHTML = ''; // clear any dummy content
    
    // If there are multiple images, create thumbnails
    if (product.images.length > 1) {
        product.images.forEach((imgSrc, index) => {
            const thumbDiv = document.createElement('div');
            thumbDiv.className = `thumbnail ${index === 0 ? 'active' : ''}`;
            thumbDiv.onclick = function() { changeMainImage(imgSrc, this); };
            
            const thumbImg = document.createElement('img');
            thumbImg.src = imgSrc;
            thumbImg.alt = `${product.name} view ${index + 1}`;
            
            thumbDiv.appendChild(thumbImg);
            thumbnailsContainer.appendChild(thumbDiv);
        });
    } else {
        // If only 1 image, don't show thumbnail list
        thumbnailsContainer.style.display = 'none';
    }
    
    document.getElementById('product-offer').textContent = product.offer;
    
    if (product.mrp) {
        document.getElementById('product-mrp').textContent = product.mrp;
        document.getElementById('product-mrp').style.display = 'inline';
    } else {
        document.getElementById('product-mrp').style.display = 'none';
    }

    if (product.discount) {
        document.getElementById('product-discount').textContent = product.discount;
        document.getElementById('product-discount').style.display = 'inline';
    } else {
        document.getElementById('product-discount').style.display = 'none';
    }

    document.getElementById('product-description').textContent = product.description;
    document.getElementById('review-count').textContent = `(${product.reviews.count} reviews)`;

    const featuresList = document.getElementById('product-features');
    featuresList.innerHTML = '';
    product.features.forEach(feature => {
        const li = document.createElement('li');
        li.textContent = feature;
        featuresList.appendChild(li);
    });
});


function openCart() {
    document.getElementById('cartDrawer').classList.add('active');
    document.getElementById('cartOverlay').classList.add('active');
    renderCartItems();
}

function closeCart() {
    document.getElementById('cartDrawer').classList.remove('active');
    document.getElementById('cartOverlay').classList.remove('active');
}

function removeFromCart(productId) {
    let cart = getCart();
    cart = cart.filter(item => item.id !== productId);
    saveCart(cart);
    renderCartItems();
}

function renderCartItems() {
    const cart = getCart();
    const container = document.getElementById('cartItemsContainer');
    const totalPriceEl = document.getElementById('cartTotalPrice');
    
    container.innerHTML = '';
    
    if (cart.length === 0) {
        container.innerHTML = '<div class="empty-cart-msg">Your cart is empty.</div>';
        totalPriceEl.textContent = '₹0';
        return;
    }
    
    let total = 0;
    
    cart.forEach(item => {
        // clean price string like '₹1299.00' to number
        const priceNum = parseFloat(item.price.replace(/[^0-9.-]+/g,""));
        total += priceNum * item.quantity;
        
        const div = document.createElement('div');
        div.className = 'cart-item';
        div.innerHTML = `
            <img src="${item.image}" alt="${item.name}">
            <div class="cart-item-details">
                <div class="cart-item-title">${item.name}</div>
                <div class="cart-item-price">${item.price} x ${item.quantity}</div>
                <div class="cart-item-actions">
                    <button class="cart-item-remove" onclick="removeFromCart('${item.id}')">Remove</button>
                </div>
            </div>
        `;
        container.appendChild(div);
    });
    
    totalPriceEl.textContent = '₹' + total.toFixed(2);
}



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
        packageInfo = "*PACKAGE*\n";
        cart.forEach(item => {
            packageInfo += `- ${item.quantity}x ${item.name} (${item.price} each)\n`;
            const priceNum = parseFloat(item.price.replace(/[^0-9.-]+/g,""));
            total += priceNum * item.quantity;
        });
        packageInfo += `\n*Total: ₹${total.toFixed(2)}*\n\n`;
    } else if (source === 'product') {
        const params = new URLSearchParams(window.location.search);
        const productId = params.get('id');
        const product = getProductById(productId);
        
        const qtyInput = document.getElementById('qty-input');
        const qty = qtyInput ? qtyInput.value : 1;
        
        if (product) {
            packageInfo = "*PACKAGE*\n";
            packageInfo += `- ${qty}x ${product.name} (${product.offer} each)\n`;
            const priceNum = parseFloat(product.offer.replace(/[^0-9.-]+/g,""));
            total = priceNum * parseInt(qty);
            packageInfo += `\n*Total: ₹${total.toFixed(2)}*\n\n`;
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
