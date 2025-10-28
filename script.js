// Sparkle Toggle
const sparklesContainer = document.querySelector('.sparkles-container');

function generateSparkles(count = 20) {
    if (!sparklesContainer) return;
    sparklesContainer.innerHTML = '';

    for (let i = 0; i < count; i++) {
        const sparkle = document.createElement('span');
        sparkle.className = 'sparkle';

        const width = Math.random() > 0.5 ? 2 : 1;
        const deg = Math.random() * 360;
        const duration = 2 + Math.random() * 4;
        const delay = Math.random() * 3;

        sparkle.style.setProperty('--width', width);
        sparkle.style.setProperty('--deg', deg);
        sparkle.style.setProperty('--duration', duration);
        sparkle.style.setProperty('--delay', delay);

        sparklesContainer.appendChild(sparkle);
    }
}

generateSparkles();

// FAQ Accordion
const faqItems = document.querySelectorAll('.faq-item');

faqItems.forEach(item => {
    const question = item.querySelector('.faq-question');
    question.addEventListener('click', () => {
        const isActive = item.classList.contains('active');
        faqItems.forEach(i => i.classList.remove('active'));
        if (!isActive) {
            item.classList.add('active');
        }
    });
});

// --- NEW "AMBIENT DRIFT" SETUP ---
document.addEventListener('DOMContentLoaded', function() {
    // 1. Find all shapes
    const heroShapes = document.querySelectorAll('.hero-shapes div, .hero-shapes .shape-text');

    // 2. Get viewport dimensions
    const heroSection = document.getElementById('hero');
    const vw = heroSection.clientWidth;
    const vh = heroSection.clientHeight;

    // 3. Loop through each shape and assign a random position
    heroShapes.forEach(shape => {
        // Get random % for top and left
        const randomTop = Math.floor(Math.random() * 80) + 10; // 10% to 90%
        const randomLeft = Math.floor(Math.random() * 80) + 10; // 10% to 90%

        // Apply the style
        shape.style.top = `${randomTop}%`;
        shape.style.left = `${randomLeft}%`;

        // Fade them in
        shape.style.opacity = '0.5';
    });
});

// Draggable Navigation
const dragNav = document.getElementById('dragNav');
const toggleBtn = dragNav.querySelector('.toggle-btn');

toggleBtn.addEventListener('click', () => {
    dragNav.classList.toggle('open');
});

let isDragging = false;
let currentX, currentY, initialX, initialY;
let xOffset = 0, yOffset = 0;

dragNav.addEventListener('mousedown', dragStart);
document.addEventListener('mousemove', drag);
document.addEventListener('mouseup', dragEnd);

dragNav.addEventListener('touchstart', dragStart);
document.addEventListener('touchmove', drag);
document.addEventListener('touchend', dragEnd);

function dragStart(e) {
    if (e.target.closest('a') || e.target.closest('.toggle-btn')) return;

    initialX = e.type === 'touchstart' ? e.touches[0].clientX - xOffset : e.clientX - xOffset;
    initialY = e.type === 'touchstart' ? e.touches[0].clientY - yOffset : e.clientY - yOffset;

    isDragging = true;
    dragNav.classList.add('dragging');
}

function drag(e) {
    if (!isDragging) return;

    e.preventDefault();

    currentX = e.type === 'touchmove' ? e.touches[0].clientX : e.clientX;
    currentY = e.type === 'touchmove' ? e.touches[0].clientY : e.clientY;

    xOffset = currentX - initialX;
    yOffset = currentY - initialY;

    setTranslate(xOffset, yOffset, dragNav);
}

function dragEnd() {
    isDragging = false;
    dragNav.classList.remove('dragging');
}

function setTranslate(xPos, yPos, el) {
    el.style.transform = `translate(${xPos}px, ${yPos}px)`;
}

// FAQ Search Filter
const searchInput = document.querySelector('#details .search-input');
const faqAccordion = document.querySelector('.faq-accordion');

searchInput.addEventListener('input', (e) => {
    const searchTerm = e.target.value.toLowerCase();

    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question').textContent.toLowerCase();
        const answer = item.querySelector('.faq-answer').textContent.toLowerCase();

        if (question.includes(searchTerm) || answer.includes(searchTerm)) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
});
