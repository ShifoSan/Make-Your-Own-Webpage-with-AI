
# Component 2: Draggable Navigation Menu
draggable_nav_content = """
================================================================================
ENHANCED DRAGGABLE NAVIGATION MENU COMPONENT
================================================================================

IMPROVEMENTS MADE:
1. Added smooth momentum-based dragging with inertia effect
2. Improved touch device support with passive event listeners
3. Added boundary constraints to keep menu visible on screen
4. Enhanced visual feedback with ripple click effects
5. Better animation timing and cubic-bezier easing functions
6. Added keyboard accessibility (Arrow keys navigation + Enter key)
7. Improved icon transitions and hover states with scale effects
8. Added drag indicator and visual cues
9. Added nav labels that appear on hover
10. Improved mobile responsiveness

================================================================================
index.html
================================================================================

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enhanced Draggable Navigation Menu</title>
    <link rel="stylesheet" href="style.css">
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
</head>
<body>
    <nav id="dragNav" tabindex="0" role="navigation" aria-label="Main Navigation">
        <div class="nav-content">
            <div class="toggle-btn" role="button" aria-label="Toggle navigation menu" tabindex="0">
                <i class='bx bx-plus'></i>
            </div>
            <span style="--i:1;" class="nav-item">
                <a href="#" aria-label="Home" tabindex="-1">
                    <i class='bx bxs-home'></i>
                    <span class="nav-label">Home</span>
                </a>
            </span>
            <span style="--i:2;" class="nav-item">
                <a href="#" aria-label="Gallery" tabindex="-1">
                    <i class='bx bxs-camera'></i>
                    <span class="nav-label">Gallery</span>
                </a>
            </span>
            <span style="--i:3;" class="nav-item">
                <a href="#" aria-label="Alarms" tabindex="-1">
                    <i class='bx bxs-alarm'></i>
                    <span class="nav-label">Alarms</span>
                </a>
            </span>
            <span style="--i:4;" class="nav-item">
                <a href="#" aria-label="Location" tabindex="-1">
                    <i class='bx bxs-map'></i>
                    <span class="nav-label">Location</span>
                </a>
            </span>
            <span style="--i:5;" class="nav-item">
                <a href="#" aria-label="Settings" tabindex="-1">
                    <i class='bx bxs-cog'></i>
                    <span class="nav-label">Settings</span>
                </a>
            </span>
        </div>
        <div class="drag-indicator">
            <i class='bx bx-move'></i>
        </div>
    </nav>

    <div class="page-content">
        <h1>Enhanced Draggable Navigation</h1>
        <p>Drag the floating navigation menu anywhere on the screen!</p>
        <ul>
            <li>✓ Smooth momentum-based dragging</li>
            <li>✓ Touch device support</li>
            <li>✓ Keyboard navigation (Arrow keys + Enter)</li>
            <li>✓ Boundary constraints</li>
            <li>✓ Ripple click effects</li>
        </ul>
    </div>

    <script src="script.js"></script>
</body>
</html>

================================================================================
style.css
================================================================================

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    min-height: 100vh;
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    overflow-x: hidden;
}

.page-content {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    color: white;
    text-align: center;
    padding: 20px;
}

.page-content h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.page-content p {
    font-size: 1.2rem;
    margin-bottom: 2rem;
    opacity: 0.9;
}

.page-content ul {
    list-style: none;
    font-size: 1.1rem;
}

.page-content ul li {
    margin: 0.5rem 0;
    opacity: 0.85;
}

nav {
    position: fixed;
    bottom: 40px;
    right: 40px;
    width: 70px;
    height: 70px;
    z-index: 1000;
    cursor: move;
    transition: transform 0.1s ease-out;
}

nav.dragging {
    transition: none;
    cursor: grabbing;
}

nav.dragging .drag-indicator {
    opacity: 1;
    transform: translateY(0);
}

.drag-indicator {
    position: absolute;
    top: -30px;
    left: 50%;
    transform: translateX(-50%) translateY(-5px);
    color: rgba(255, 255, 255, 0.7);
    font-size: 20px;
    opacity: 0;
    transition: all 0.3s ease;
    pointer-events: none;
}

nav:hover .drag-indicator {
    opacity: 0.7;
    transform: translateX(-50%) translateY(0);
}

.nav-content {
    position: relative;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

.toggle-btn {
    position: absolute;
    width: 70px;
    height: 70px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
    transition: all 0.3s ease;
    z-index: 100;
    overflow: hidden;
}

.toggle-btn::before {
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle, rgba(255,255,255,0.3) 0%, transparent 70%);
    transform: scale(0);
    transition: transform 0.5s ease;
}

.toggle-btn:hover::before,
.toggle-btn:focus::before {
    transform: scale(1);
}

.toggle-btn:hover {
    transform: scale(1.1);
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.4);
}

.toggle-btn:active {
    transform: scale(0.95);
}

.toggle-btn i {
    color: white;
    font-size: 30px;
    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

nav.open .toggle-btn i {
    transform: rotate(135deg);
}

.nav-item {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    opacity: 0;
    visibility: hidden;
    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    transition-delay: calc(0.05s * var(--i));
}

nav.open .nav-item {
    opacity: 1;
    visibility: visible;
}

nav.open .nav-item:nth-child(2) {
    transform: translate(-50%, -140px);
}

nav.open .nav-item:nth-child(3) {
    transform: translate(60px, -110px);
}

nav.open .nav-item:nth-child(4) {
    transform: translate(90px, -20px);
}

nav.open .nav-item:nth-child(5) {
    transform: translate(60px, 70px);
}

nav.open .nav-item:nth-child(6) {
    transform: translate(-50%, 100px);
}

.nav-item a {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 55px;
    height: 55px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 50%;
    color: white;
    text-decoration: none;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.nav-item a::before {
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle, rgba(255,255,255,0.4) 0%, transparent 70%);
    transform: scale(0);
    transition: transform 0.4s ease;
}

.nav-item a:hover::before,
.nav-item a:focus::before {
    transform: scale(1);
}

.nav-item a:hover,
.nav-item a:focus {
    transform: scale(1.15);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
}

.nav-item a:active {
    transform: scale(0.95);
}

.nav-item a i {
    font-size: 24px;
    z-index: 1;
}

.nav-label {
    position: absolute;
    left: 50%;
    bottom: -25px;
    transform: translateX(-50%);
    background: rgba(0, 0, 0, 0.8);
    color: white;
    padding: 4px 10px;
    border-radius: 4px;
    font-size: 12px;
    white-space: nowrap;
    opacity: 0;
    pointer-events: none;
    transition: all 0.3s ease;
}

.nav-item a:hover .nav-label,
.nav-item a:focus .nav-label {
    opacity: 1;
    bottom: -30px;
}

@media (max-width: 768px) {
    nav {
        bottom: 20px;
        right: 20px;
    }
    
    .page-content h1 {
        font-size: 2rem;
    }
    
    .page-content p {
        font-size: 1rem;
    }
}

================================================================================
script.js
================================================================================

const nav = document.getElementById('dragNav');
const toggleBtn = document.querySelector('.toggle-btn');
const navItems = document.querySelectorAll('.nav-item a');

let isDragging = false;
let currentX, currentY, initialX, initialY;
let xOffset = 0, yOffset = 0;
let velocityX = 0, velocityY = 0;
let lastX = 0, lastY = 0;
let lastTime = Date.now();

// Toggle navigation
function toggleNav(e) {
    if (!isDragging) {
        nav.classList.toggle('open');
        const isOpen = nav.classList.contains('open');
        navItems.forEach((item, index) => {
            item.setAttribute('tabindex', isOpen ? '0' : '-1');
        });
        e.stopPropagation();
    }
}

toggleBtn.addEventListener('click', toggleNav);
toggleBtn.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        toggleNav(e);
    }
});

// Dragging functionality
function dragStart(e) {
    if (e.target.closest('.toggle-btn') || e.target.closest('.nav-item')) {
        return;
    }
    
    initialX = e.type === 'touchstart' ? e.touches[0].clientX - xOffset : e.clientX - xOffset;
    initialY = e.type === 'touchstart' ? e.touches[0].clientY - yOffset : e.clientY - yOffset;
    
    lastX = initialX;
    lastY = initialY;
    lastTime = Date.now();
    
    isDragging = true;
    nav.classList.add('dragging');
}

function drag(e) {
    if (!isDragging) return;
    
    e.preventDefault();
    
    currentX = e.type === 'touchmove' ? e.touches[0].clientX : e.clientX;
    currentY = e.type === 'touchmove' ? e.touches[0].clientY : e.clientY;
    
    xOffset = currentX - initialX;
    yOffset = currentY - initialY;
    
    // Calculate velocity for momentum
    const currentTime = Date.now();
    const deltaTime = currentTime - lastTime;
    if (deltaTime > 0) {
        velocityX = (currentX - lastX) / deltaTime;
        velocityY = (currentY - lastY) / deltaTime;
    }
    
    lastX = currentX;
    lastY = currentY;
    lastTime = currentTime;
    
    setTranslate(xOffset, yOffset, nav);
}

function dragEnd() {
    if (!isDragging) return;
    
    isDragging = false;
    nav.classList.remove('dragging');
    
    // Apply momentum effect
    let momentumX = velocityX * 50;
    let momentumY = velocityY * 50;
    
    xOffset += momentumX;
    yOffset += momentumY;
    
    // Apply boundary constraints
    const rect = nav.getBoundingClientRect();
    const maxX = window.innerWidth - rect.width;
    const maxY = window.innerHeight - rect.height;
    
    xOffset = Math.max(-rect.left, Math.min(xOffset, maxX - rect.left));
    yOffset = Math.max(-rect.top, Math.min(yOffset, maxY - rect.top));
    
    setTranslate(xOffset, yOffset, nav);
    
    velocityX = 0;
    velocityY = 0;
}

function setTranslate(xPos, yPos, el) {
    el.style.transform = `translate(${xPos}px, ${yPos}px)`;
}

// Mouse events
nav.addEventListener('mousedown', dragStart);
document.addEventListener('mousemove', drag);
document.addEventListener('mouseup', dragEnd);

// Touch events
nav.addEventListener('touchstart', dragStart, { passive: false });
document.addEventListener('touchmove', drag, { passive: false });
document.addEventListener('touchend', dragEnd);

// Keyboard navigation
let currentIndex = -1;
nav.addEventListener('keydown', (e) => {
    if (!nav.classList.contains('open')) return;
    
    const items = Array.from(navItems);
    
    if (e.key === 'ArrowDown' || e.key === 'ArrowRight') {
        e.preventDefault();
        currentIndex = (currentIndex + 1) % items.length;
        items[currentIndex].focus();
    } else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') {
        e.preventDefault();
        currentIndex = currentIndex <= 0 ? items.length - 1 : currentIndex - 1;
        items[currentIndex].focus();
    }
});

// Ripple effect on click
navItems.forEach(item => {
    item.addEventListener('click', function(e) {
        const ripple = document.createElement('span');
        const rect = this.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = e.clientX - rect.left - size / 2;
        const y = e.clientY - rect.top - size / 2;
        
        ripple.style.cssText = `
            position: absolute;
            width: ${size}px;
            height: ${size}px;
            left: ${x}px;
            top: ${y}px;
            background: rgba(255, 255, 255, 0.5);
            border-radius: 50%;
            transform: scale(0);
            animation: ripple-effect 0.6s ease-out;
            pointer-events: none;
        `;
        
        this.appendChild(ripple);
        
        setTimeout(() => ripple.remove(), 600);
    });
});

// Add CSS animation for ripple
const style = document.createElement('style');
style.textContent = `
    @keyframes ripple-effect {
        to {
            transform: scale(2);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);
"""

with open('2_Enhanced_Draggable_Navigation.txt', 'w', encoding='utf-8') as f:
    f.write(draggable_nav_content)

print("✓ Created: 2_Enhanced_Draggable_Navigation.txt")
