


// <!-- menu bar -->

    const menuToggle = document.getElementById('mobile-menu');
    const navMenu = document.getElementById('nav-menu');

    menuToggle.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        
        // Hamburger animation (Optional)
        menuToggle.classList.toggle('is-active');
    });

    // Link click karne par menu close ho jaye
    document.querySelectorAll('.nav a').forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
        });
    });





// <!-- clients say -->
 
   
    const slider = document.getElementById('slider');
    const container = document.getElementById('sliderContainer');
    const cards = document.querySelectorAll('.testimonial-card');
    
    let currentIndex = 0;
    let autoPlayInterval;

    function getVisibleCards() {
        if (window.innerWidth <= 768) return 1;
        if (window.innerWidth <= 1024) return 2;
        return 3;
    }

    function updateSlider() {
        const visibleCards = getVisibleCards();
        const totalCards = cards.length;
        const maxIndex = totalCards - visibleCards;

        // Loop logic: Agar end par pahunche to start par aa jaye
        if (currentIndex > maxIndex) {
            currentIndex = 0;
        } else if (currentIndex < 0) {
            currentIndex = maxIndex;
        }

        const gap = (window.innerWidth <= 768) ? 0 : 20;
        const cardWidth = cards[0].offsetWidth + gap;
        slider.style.transform = `translateX(-${currentIndex * cardWidth}px)`;
    }

    function slide(direction) {
        currentIndex += direction;
        updateSlider();
    }

    // Auto Play Function (Every 2 seconds)
    function startAutoPlay() {
        autoPlayInterval = setInterval(() => {
            slide(1);
        }, 2000);
    }

    function stopAutoPlay() {
        clearInterval(autoPlayInterval);
    }

    // Event Listeners: Mouse enter par rukega, leave par chalega
    container.addEventListener('mouseenter', stopAutoPlay);
    container.addEventListener('mouseleave', startAutoPlay);

    // Initial Start & Resize Fix
    window.addEventListener('resize', () => {
        currentIndex = 0;
        updateSlider();
    });

    startAutoPlay();
