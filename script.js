document.addEventListener('DOMContentLoaded', () => {
    // Tab Switching Logic
    const tabs = document.querySelectorAll('.product-tabs li');
    
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // Remove active class from all tabs
            tabs.forEach(t => t.classList.remove('active'));
            // Add active class to clicked tab
            tab.classList.add('active');
            
            const filterValue = tab.textContent.trim().toLowerCase();
            const products = document.querySelectorAll('.product-card');
            
            products.forEach(product => {
                product.style.transition = 'all 0.3s ease';
                product.style.opacity = '0';
                product.style.transform = 'scale(0.95)';
                
                setTimeout(() => {
                    if (filterValue === 'all products' || product.dataset.category === filterValue) {
                        product.style.display = 'block';
                        setTimeout(() => {
                            product.style.opacity = '1';
                            product.style.transform = 'scale(1)';
                        }, 50);
                    } else {
                        product.style.display = 'none';
                    }
                }, 300);
            });
        });
    });

    // Buy Now buttons WhatsApp redirect
    const buyNowBtns = document.querySelectorAll('.add-to-cart-btn');
    const whatsappNumber = '919061432885'; // Maxxo WhatsApp number

    buyNowBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Find the closest product card to extract the exact product name
            const productCard = this.closest('.product-card');
            let productName = "a product";
            
            if (productCard) {
                const titleElement = productCard.querySelector('.product-title');
                if (titleElement && titleElement.childNodes.length > 0) {
                    // Grab the first text node to avoid getting the <small> subtext
                    productName = titleElement.childNodes[0].nodeValue.trim();
                }
            }
            
            // Generate the pre-filled WhatsApp message URL
            const message = `Hello, I am interested in purchasing the ${productName}.`;
            const whatsappUrl = `https://wa.me/${whatsappNumber}?text=${encodeURIComponent(message)}`;
            
            // Redirect user to WhatsApp in a new tab
            window.open(whatsappUrl, '_blank');
        });
    });

    // Countdown Timer Logic
    const timeBoxes = document.querySelectorAll('.countdown span');
    if (timeBoxes.length === 3) {
        let hours = 12;
        let minutes = 45;
        let seconds = 30;

        setInterval(() => {
            seconds--;
            if (seconds < 0) {
                seconds = 59;
                minutes--;
                if (minutes < 0) {
                    minutes = 59;
                    hours--;
                    if (hours < 0) {
                        hours = 24; // reset for demo
                    }
                }
            }

            timeBoxes[0].textContent = hours.toString().padStart(2, '0');
            timeBoxes[1].textContent = minutes.toString().padStart(2, '0');
            timeBoxes[2].textContent = seconds.toString().padStart(2, '0');
        }, 1000);
    }
    // Mobile Menu Toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');

    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener('click', (e) => {
            e.preventDefault();
            navLinks.classList.toggle('active');
            
            // Toggle icon between bars and times
            const icon = mobileMenuBtn.querySelector('i');
            if (icon.classList.contains('fa-bars')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-xmark');
            } else {
                icon.classList.remove('fa-xmark');
                icon.classList.add('fa-bars');
            }
        });
    }

    // Search Functionality
    const searchInput = document.getElementById('searchInput');
    const searchBtn = document.getElementById('searchBtn');

    function performSearch() {
        const query = searchInput.value.trim().toLowerCase();
        const products = document.querySelectorAll('.product-card');
        
        // Reset tabs to "All Products" when searching to show accurate results
        const tabsList = document.querySelectorAll('.product-tabs li');
        if (tabsList.length > 0 && query !== "") {
            tabsList.forEach(t => t.classList.remove('active'));
            tabsList[0].classList.add('active');
        }

        products.forEach(product => {
            const title = product.querySelector('.product-title').textContent.toLowerCase();
            
            // Disable transition for instantaneous live-search filtering
            product.style.transition = 'none';
            
            if (title.includes(query)) {
                product.style.display = 'block';
                product.style.opacity = '1';
                product.style.transform = 'scale(1)';
            } else {
                product.style.display = 'none';
            }
        });
    }

    if (searchInput && searchBtn) {
        // Live search on input
        searchInput.addEventListener('input', performSearch);
        
        // Scroll to products on button click or Enter key
        searchBtn.addEventListener('click', () => {
            performSearch();
            const productsSection = document.getElementById('products');
            if (productsSection) productsSection.scrollIntoView({ behavior: 'smooth' });
        });
        
        searchInput.addEventListener('keyup', (e) => {
            if (e.key === 'Enter') {
                const productsSection = document.getElementById('products');
                if (productsSection) productsSection.scrollIntoView({ behavior: 'smooth' });
            }
        });
    }
});
