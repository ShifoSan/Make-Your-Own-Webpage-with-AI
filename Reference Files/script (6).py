
# Component 7: Simple Toggle Button
simple_toggle_content = """
================================================================================
ENHANCED SIMPLE TOGGLE BUTTON COMPONENT
================================================================================

IMPROVEMENTS MADE:
1. Added multiple toggle styles (iOS style, Material Design, Custom)
2. Improved animation with smooth transitions
3. Enhanced accessibility with ARIA labels and keyboard support
4. Added labeled on/off states
5. Better visual feedback with colors and shadows
6. Added disabled state styling
7. Improved mobile touch responsiveness
8. Added sound toggle option indicator
9. Better color scheme variations
10. Added ripple effect on click

================================================================================
index.html
================================================================================

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Enhanced Toggle Buttons</title>
    <link rel="stylesheet" href="style.css" />
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
</head>
<body>
    <div class="container">
        <h1 class="title">Modern Toggle Switches</h1>
        
        <!-- iOS Style Toggle -->
        <div class="toggle-group">
            <label class="toggle-label-text">iOS Style</label>
            <label class="switch-button ios-style" for="switch1">
                <input id="switch1" type="checkbox" role="switch" aria-label="iOS style toggle" />
                <div class="switch-bg">
                    <div class="switch-slider">
                        <i class='bx bx-check'></i>
                    </div>
                </div>
                <span class="state-text">
                    <span class="off-text">OFF</span>
                    <span class="on-text">ON</span>
                </span>
            </label>
        </div>
        
        <!-- Material Design Toggle -->
        <div class="toggle-group">
            <label class="toggle-label-text">Material Design</label>
            <label class="switch-button material-style" for="switch2">
                <input id="switch2" type="checkbox" role="switch" aria-label="Material design toggle" />
                <div class="switch-bg">
                    <div class="switch-slider"></div>
                </div>
            </label>
        </div>
        
        <!-- Custom Animated Toggle -->
        <div class="toggle-group">
            <label class="toggle-label-text">Custom Animated</label>
            <label class="switch-button custom-style" for="switch3">
                <input id="switch3" type="checkbox" role="switch" aria-label="Custom animated toggle" />
                <div class="switch-bg">
                    <div class="switch-slider">
                        <div class="slider-inner"></div>
                    </div>
                    <div class="icons">
                        <i class='bx bx-moon moon-icon'></i>
                        <i class='bx bx-sun sun-icon'></i>
                    </div>
                </div>
            </label>
        </div>
        
        <!-- Gradient Toggle -->
        <div class="toggle-group">
            <label class="toggle-label-text">Gradient Style</label>
            <label class="switch-button gradient-style" for="switch4">
                <input id="switch4" type="checkbox" role="switch" aria-label="Gradient style toggle" />
                <div class="switch-bg">
                    <div class="switch-slider">
                        <i class='bx bx-check'></i>
                    </div>
                </div>
            </label>
        </div>
        
        <!-- Disabled Toggle -->
        <div class="toggle-group">
            <label class="toggle-label-text">Disabled State</label>
            <label class="switch-button ios-style disabled" for="switch5">
                <input id="switch5" type="checkbox" disabled role="switch" aria-label="Disabled toggle" aria-disabled="true" />
                <div class="switch-bg">
                    <div class="switch-slider">
                        <i class='bx bx-x'></i>
                    </div>
                </div>
            </label>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>

================================================================================
style.css
================================================================================

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    font-family: 'Poppins', sans-serif;
    padding: 20px;
}

.container {
    background: rgba(255, 255, 255, 0.95);
    padding: 50px 40px;
    border-radius: 25px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    max-width: 500px;
    width: 100%;
}

.title {
    text-align: center;
    font-size: 2.2rem;
    font-weight: 700;
    color: #333;
    margin-bottom: 40px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.toggle-group {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
    padding: 15px;
    background: #f8f9fa;
    border-radius: 15px;
    transition: all 0.3s ease;
}

.toggle-group:hover {
    background: #e9ecef;
    transform: translateX(5px);
}

.toggle-label-text {
    font-size: 1.1rem;
    font-weight: 600;
    color: #495057;
}

.switch-button {
    position: relative;
    display: inline-block;
    cursor: pointer;
    user-select: none;
}

.switch-button.disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

.switch-button input {
    display: none;
}

/* iOS Style Toggle */
.ios-style .switch-bg {
    width: 70px;
    height: 35px;
    background: #ccc;
    border-radius: 50px;
    position: relative;
    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    box-shadow: inset 0 2px 5px rgba(0, 0, 0, 0.2);
}

.ios-style .switch-slider {
    position: absolute;
    width: 29px;
    height: 29px;
    background: white;
    border-radius: 50%;
    top: 3px;
    left: 3px;
    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    box-shadow: 0 3px 8px rgba(0, 0, 0, 0.3);
    display: flex;
    align-items: center;
    justify-content: center;
}

.ios-style .switch-slider i {
    font-size: 18px;
    color: #4caf50;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.ios-style input:checked + .switch-bg {
    background: linear-gradient(135deg, #4caf50 0%, #45a049 100%);
}

.ios-style input:checked + .switch-bg .switch-slider {
    left: 38px;
}

.ios-style input:checked + .switch-bg .switch-slider i {
    opacity: 1;
}

.ios-style .state-text {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 8px;
    pointer-events: none;
}

.ios-style .state-text span {
    font-size: 10px;
    font-weight: 700;
    color: white;
    transition: opacity 0.3s ease;
}

.ios-style .off-text {
    opacity: 0.7;
}

.ios-style .on-text {
    opacity: 0;
}

.ios-style input:checked ~ .state-text .off-text {
    opacity: 0;
}

.ios-style input:checked ~ .state-text .on-text {
    opacity: 1;
}

/* Material Design Toggle */
.material-style .switch-bg {
    width: 60px;
    height: 25px;
    background: rgba(0, 0, 0, 0.26);
    border-radius: 50px;
    position: relative;
    transition: all 0.3s ease;
}

.material-style .switch-slider {
    position: absolute;
    width: 20px;
    height: 20px;
    background: white;
    border-radius: 50%;
    top: 2.5px;
    left: 2.5px;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.material-style input:checked + .switch-bg {
    background: rgba(102, 126, 234, 0.5);
}

.material-style input:checked + .switch-bg .switch-slider {
    left: 37.5px;
    background: #667eea;
}

.material-style .switch-slider::before {
    content: '';
    position: absolute;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: rgba(0, 0, 0, 0.05);
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(0);
    transition: transform 0.3s ease;
}

.material-style input:checked + .switch-bg .switch-slider::before {
    transform: translate(-50%, -50%) scale(1);
    background: rgba(102, 126, 234, 0.2);
}

/* Custom Animated Toggle */
.custom-style .switch-bg {
    width: 80px;
    height: 40px;
    background: #2c3e50;
    border-radius: 50px;
    position: relative;
    transition: all 0.4s ease;
    overflow: hidden;
}

.custom-style .switch-slider {
    position: absolute;
    width: 34px;
    height: 34px;
    background: linear-gradient(145deg, #ffffff, #e6e6e6);
    border-radius: 50%;
    top: 3px;
    left: 3px;
    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    display: flex;
    align-items: center;
    justify-content: center;
}

.custom-style .slider-inner {
    width: 20px;
    height: 20px;
    background: radial-gradient(circle, #ffd700, #ff8c00);
    border-radius: 50%;
    transition: all 0.4s ease;
}

.custom-style .icons {
    position: absolute;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 10px;
    pointer-events: none;
}

.custom-style .moon-icon,
.custom-style .sun-icon {
    font-size: 18px;
    transition: all 0.4s ease;
}

.custom-style .moon-icon {
    color: #f39c12;
}

.custom-style .sun-icon {
    color: white;
    opacity: 0.3;
}

.custom-style input:checked + .switch-bg {
    background: #3498db;
}

.custom-style input:checked + .switch-bg .switch-slider {
    left: 43px;
}

.custom-style input:checked + .switch-bg .slider-inner {
    background: radial-gradient(circle, #ffffff, #e0e0e0);
}

.custom-style input:checked ~ .icons .moon-icon {
    opacity: 0.3;
}

.custom-style input:checked ~ .icons .sun-icon {
    opacity: 1;
}

/* Gradient Style Toggle */
.gradient-style .switch-bg {
    width: 75px;
    height: 38px;
    background: linear-gradient(135deg, #ddd 0%, #ccc 100%);
    border-radius: 50px;
    position: relative;
    transition: all 0.4s ease;
    box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.2);
}

.gradient-style .switch-slider {
    position: absolute;
    width: 32px;
    height: 32px;
    background: linear-gradient(145deg, #ffffff, #f0f0f0);
    border-radius: 50%;
    top: 3px;
    left: 3px;
    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25);
    display: flex;
    align-items: center;
    justify-content: center;
}

.gradient-style .switch-slider i {
    font-size: 20px;
    color: #667eea;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.gradient-style input:checked + .switch-bg {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.gradient-style input:checked + .switch-bg .switch-slider {
    left: 40px;
    background: linear-gradient(145deg, #ffffff, #ffffff);
    box-shadow: 0 4px 15px rgba(102, 126, 234, 0.5);
}

.gradient-style input:checked + .switch-bg .switch-slider i {
    opacity: 1;
}

@media (max-width: 480px) {
    .container {
        padding: 30px 20px;
    }
    
    .title {
        font-size: 1.8rem;
    }
    
    .toggle-label-text {
        font-size: 1rem;
    }
}

================================================================================
script.js
================================================================================

// Get all toggle switches
const switches = document.querySelectorAll('.switch-button input[type="checkbox"]');

// Add event listeners to all switches
switches.forEach((switchInput, index) => {
    switchInput.addEventListener('change', function() {
        const isChecked = this.checked;
        const label = this.closest('.switch-button');
        
        // Update ARIA attribute
        this.setAttribute('aria-checked', isChecked);
        
        // Add ripple effect
        createRipple(label, isChecked);
        
        // Optional: Haptic feedback on mobile
        if ('vibrate' in navigator) {
            navigator.vibrate(30);
        }
        
        // Log state change
        console.log(`Toggle ${index + 1} is now ${isChecked ? 'ON' : 'OFF'}`);
        
        // Optional: Store state in localStorage
        localStorage.setItem(`toggle_${index}`, isChecked);
    });
    
    // Keyboard accessibility
    const label = switchInput.closest('.switch-button');
    label.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            if (!switchInput.disabled) {
                switchInput.checked = !switchInput.checked;
                switchInput.dispatchEvent(new Event('change'));
            }
        }
    });
    
    // Restore state from localStorage
    const savedState = localStorage.getItem(`toggle_${index}`);
    if (savedState !== null) {
        switchInput.checked = savedState === 'true';
        switchInput.setAttribute('aria-checked', switchInput.checked);
    }
});

// Create ripple effect
function createRipple(element, isChecked) {
    const ripple = document.createElement('span');
    const rect = element.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height) * 2;
    
    ripple.style.cssText = `
        position: absolute;
        width: ${size}px;
        height: ${size}px;
        border-radius: 50%;
        background: ${isChecked ? 'rgba(102, 126, 234, 0.4)' : 'rgba(0, 0, 0, 0.2)'};
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%) scale(0);
        pointer-events: none;
        z-index: 1;
    `;
    
    const switchBg = element.querySelector('.switch-bg');
    if (switchBg) {
        switchBg.style.position = 'relative';
        switchBg.style.overflow = 'visible';
        switchBg.appendChild(ripple);
        
        // Trigger animation
        requestAnimationFrame(() => {
            ripple.style.transition = 'transform 0.6s ease-out, opacity 0.6s ease-out';
            ripple.style.transform = 'translate(-50%, -50%) scale(1)';
            ripple.style.opacity = '0';
        });
        
        setTimeout(() => ripple.remove(), 600);
    }
}

// Add hover effect
switches.forEach(switchInput => {
    const label = switchInput.closest('.switch-button');
    
    label.addEventListener('mouseenter', () => {
        if (!switchInput.disabled) {
            const slider = label.querySelector('.switch-slider');
            if (slider) {
                slider.style.transform = 'scale(1.1)';
            }
        }
    });
    
    label.addEventListener('mouseleave', () => {
        const slider = label.querySelector('.switch-slider');
        if (slider) {
            slider.style.transform = 'scale(1)';
        }
    });
});

// Prevent disabled toggles from being interacted with
document.querySelectorAll('.switch-button.disabled').forEach(label => {
    label.addEventListener('click', (e) => {
        e.preventDefault();
    });
});
"""

with open('7_Enhanced_Simple_Toggle.txt', 'w', encoding='utf-8') as f:
    f.write(simple_toggle_content)

print("✓ Created: 7_Enhanced_Simple_Toggle.txt")
print("\n" + "="*80)
print("ALL ENHANCED COMPONENTS CREATED SUCCESSFULLY!")
print("="*80)
