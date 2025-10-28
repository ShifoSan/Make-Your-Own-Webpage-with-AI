
# Component 4: Custom Dropdown Select Menu
dropdown_content = """
================================================================================
ENHANCED CUSTOM DROPDOWN SELECT MENU COMPONENT
================================================================================

IMPROVEMENTS MADE:
1. Added search/filter functionality for options
2. Improved keyboard navigation (Arrow keys, Enter, Escape, Tab)
3. Added smooth animations with stagger effect for options
4. Enhanced accessibility with ARIA attributes and roles
5. Added click-outside-to-close functionality
6. Improved visual feedback with hover and focus states
7. Added selected state indicator
8. Better mobile responsiveness
9. Added custom scrollbar styling for long lists
10. Improved color scheme and modern design

================================================================================
index.html
================================================================================

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />
    <link href="https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css" rel="stylesheet" />
    <title>Enhanced Custom Dropdown Select Menu</title>
</head>
<body>
    <div class="container">
        <h1 class="title">Select Your Platform</h1>
        
        <div class="select-menu" role="combobox" aria-expanded="false" aria-haspopup="listbox">
            <div class="select-btn" tabindex="0" role="button" aria-label="Select option button">
                <span class="sBtn-text">Select your option</span>
                <i class="bx bx-chevron-down"></i>
            </div>
            
            <div class="search-box">
                <input 
                    type="text" 
                    placeholder="Search platforms..." 
                    class="search-input"
                    aria-label="Search options"
                />
                <i class="bx bx-search"></i>
            </div>
            
            <ul class="options" role="listbox">
                <li class="option" role="option" data-value="github" tabindex="0">
                    <i class="bx bxl-github" style="color: #171515"></i>
                    <span class="option-text">Github</span>
                    <i class="bx bx-check check-icon"></i>
                </li>
                <li class="option" role="option" data-value="instagram" tabindex="0">
                    <i class="bx bxl-instagram-alt" style="color: #e1306c"></i>
                    <span class="option-text">Instagram</span>
                    <i class="bx bx-check check-icon"></i>
                </li>
                <li class="option" role="option" data-value="linkedin" tabindex="0">
                    <i class="bx bxl-linkedin-square" style="color: #0e76a8"></i>
                    <span class="option-text">LinkedIn</span>
                    <i class="bx bx-check check-icon"></i>
                </li>
                <li class="option" role="option" data-value="facebook" tabindex="0">
                    <i class="bx bxl-facebook-circle" style="color: #4267b2"></i>
                    <span class="option-text">Facebook</span>
                    <i class="bx bx-check check-icon"></i>
                </li>
                <li class="option" role="option" data-value="twitter" tabindex="0">
                    <i class="bx bxl-twitter" style="color: #1da1f2"></i>
                    <span class="option-text">Twitter</span>
                    <i class="bx bx-check check-icon"></i>
                </li>
                <li class="option" role="option" data-value="youtube" tabindex="0">
                    <i class="bx bxl-youtube" style="color: #ff0000"></i>
                    <span class="option-text">YouTube</span>
                    <i class="bx bx-check check-icon"></i>
                </li>
                <li class="option" role="option" data-value="discord" tabindex="0">
                    <i class="bx bxl-discord-alt" style="color: #5865f2"></i>
                    <span class="option-text">Discord</span>
                    <i class="bx bx-check check-icon"></i>
                </li>
            </ul>
        </div>
        
        <div class="selected-info">
            <p>Selected: <span id="selectedValue">None</span></p>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>

================================================================================
style.css
================================================================================

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}

body {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.container {
    text-align: center;
    padding: 20px;
}

.title {
    color: white;
    font-size: 2.5rem;
    margin-bottom: 40px;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
}

.select-menu {
    position: relative;
    width: 380px;
    margin: 0 auto;
}

.select-menu .select-btn {
    display: flex;
    height: 60px;
    background: #fff;
    padding: 0 20px;
    font-size: 18px;
    font-weight: 500;
    border-radius: 12px;
    align-items: center;
    cursor: pointer;
    justify-content: space-between;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
}

.select-menu .select-btn:hover {
    background: #f8f9fa;
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.25);
    transform: translateY(-2px);
}

.select-btn i {
    font-size: 28px;
    transition: transform 0.3s ease;
}

.select-menu.active .select-btn i {
    transform: rotate(-180deg);
}

.select-btn .sBtn-text {
    font-size: 17px;
    font-weight: 500;
    color: #333;
}

.search-box {
    position: relative;
    display: none;
    padding: 15px;
    background: #fff;
}

.select-menu.active .search-box {
    display: block;
    animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(-10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.search-box input {
    width: 100%;
    padding: 12px 40px 12px 15px;
    border: 2px solid #e0e0e0;
    border-radius: 8px;
    font-size: 15px;
    outline: none;
    transition: all 0.3s ease;
}

.search-box input:focus {
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.search-box i {
    position: absolute;
    right: 30px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 20px;
    color: #999;
}

.select-menu .options {
    position: absolute;
    top: 70px;
    width: 100%;
    max-height: 0;
    overflow: hidden;
    overflow-y: auto;
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
    list-style: none;
    transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    opacity: 0;
    z-index: 10;
}

.select-menu.active .options {
    max-height: 320px;
    opacity: 1;
    top: 80px;
}

.options::-webkit-scrollbar {
    width: 8px;
}

.options::-webkit-scrollbar-track {
    background: #f1f1f1;
    border-radius: 10px;
}

.options::-webkit-scrollbar-thumb {
    background: #888;
    border-radius: 10px;
}

.options::-webkit-scrollbar-thumb:hover {
    background: #555;
}

.options .option {
    display: flex;
    height: 60px;
    cursor: pointer;
    padding: 0 20px;
    border-radius: 8px;
    align-items: center;
    margin: 5px 10px;
    transition: all 0.3s ease;
    animation: slideIn 0.3s ease backwards;
    animation-delay: calc(var(--i, 0) * 0.05s);
    position: relative;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateX(-20px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

.options .option:hover,
.options .option:focus {
    background: #f0f0f0;
    outline: none;
}

.option i:first-child {
    font-size: 26px;
    margin-right: 15px;
}

.option .option-text {
    font-size: 17px;
    font-weight: 500;
    color: #333;
    flex: 1;
    text-align: left;
}

.option .check-icon {
    font-size: 24px;
    color: #667eea;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.option.selected {
    background: #e8ebff;
}

.option.selected .check-icon {
    opacity: 1;
}

.option.hidden {
    display: none;
}

.selected-info {
    margin-top: 40px;
    padding: 20px;
    background: rgba(255, 255, 255, 0.2);
    border-radius: 12px;
    backdrop-filter: blur(10px);
}

.selected-info p {
    color: white;
    font-size: 18px;
    font-weight: 500;
}

.selected-info span {
    font-weight: 700;
    color: #fff;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
}

@media (max-width: 480px) {
    .select-menu {
        width: 100%;
        max-width: 340px;
    }
    
    .title {
        font-size: 2rem;
    }
}

================================================================================
script.js
================================================================================

const selectMenu = document.querySelector('.select-menu');
const selectBtn = selectMenu.querySelector('.select-btn');
const options = selectMenu.querySelectorAll('.option');
const sBtn_text = selectMenu.querySelector('.sBtn-text');
const searchInput = document.querySelector('.search-input');
const selectedValueSpan = document.getElementById('selectedValue');

let currentFocusIndex = -1;

// Toggle dropdown
function toggleDropdown() {
    selectMenu.classList.toggle('active');
    selectBtn.setAttribute('aria-expanded', selectMenu.classList.contains('active'));
    
    if (selectMenu.classList.contains('active')) {
        searchInput.focus();
        // Add animation delay to options
        options.forEach((option, index) => {
            option.style.setProperty('--i', index);
        });
    } else {
        searchInput.value = '';
        filterOptions('');
    }
}

selectBtn.addEventListener('click', toggleDropdown);

// Select option
options.forEach((option, index) => {
    option.addEventListener('click', () => {
        selectOption(option);
    });
    
    option.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            selectOption(option);
        }
    });
});

function selectOption(option) {
    let selectedOption = option.querySelector('.option-text').innerText;
    sBtn_text.innerText = selectedOption;
    selectedValueSpan.innerText = selectedOption;
    
    // Remove selected class from all options
    options.forEach(opt => opt.classList.remove('selected'));
    
    // Add selected class to clicked option
    option.classList.add('selected');
    
    selectMenu.classList.remove('active');
    selectBtn.setAttribute('aria-expanded', 'false');
}

// Search functionality
searchInput.addEventListener('input', (e) => {
    filterOptions(e.target.value.toLowerCase());
});

function filterOptions(searchTerm) {
    options.forEach(option => {
        const text = option.querySelector('.option-text').innerText.toLowerCase();
        if (text.includes(searchTerm)) {
            option.classList.remove('hidden');
        } else {
            option.classList.add('hidden');
        }
    });
}

// Close dropdown when clicking outside
document.addEventListener('click', (e) => {
    if (!selectMenu.contains(e.target)) {
        selectMenu.classList.remove('active');
        selectBtn.setAttribute('aria-expanded', 'false');
    }
});

// Keyboard navigation
selectBtn.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        toggleDropdown();
    } else if (e.key === 'ArrowDown') {
        e.preventDefault();
        if (!selectMenu.classList.contains('active')) {
            toggleDropdown();
        }
    }
});

searchInput.addEventListener('keydown', (e) => {
    const visibleOptions = Array.from(options).filter(opt => !opt.classList.contains('hidden'));
    
    if (e.key === 'ArrowDown') {
        e.preventDefault();
        currentFocusIndex = Math.min(currentFocusIndex + 1, visibleOptions.length - 1);
        visibleOptions[currentFocusIndex]?.focus();
    } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        if (currentFocusIndex <= 0) {
            searchInput.focus();
            currentFocusIndex = -1;
        } else {
            currentFocusIndex--;
            visibleOptions[currentFocusIndex]?.focus();
        }
    } else if (e.key === 'Escape') {
        selectMenu.classList.remove('active');
        selectBtn.focus();
    } else if (e.key === 'Enter' && visibleOptions.length > 0) {
        e.preventDefault();
        selectOption(visibleOptions[0]);
    }
});

// Option keyboard navigation
options.forEach((option, index) => {
    option.addEventListener('keydown', (e) => {
        const visibleOptions = Array.from(options).filter(opt => !opt.classList.contains('hidden'));
        const currentIndex = visibleOptions.indexOf(option);
        
        if (e.key === 'ArrowDown') {
            e.preventDefault();
            const nextIndex = Math.min(currentIndex + 1, visibleOptions.length - 1);
            visibleOptions[nextIndex]?.focus();
        } else if (e.key === 'ArrowUp') {
            e.preventDefault();
            if (currentIndex > 0) {
                visibleOptions[currentIndex - 1]?.focus();
            } else {
                searchInput.focus();
            }
        } else if (e.key === 'Escape') {
            selectMenu.classList.remove('active');
            selectBtn.focus();
        }
    });
});
"""

with open('4_Enhanced_Custom_Dropdown.txt', 'w', encoding='utf-8') as f:
    f.write(dropdown_content)

print("✓ Created: 4_Enhanced_Custom_Dropdown.txt")
