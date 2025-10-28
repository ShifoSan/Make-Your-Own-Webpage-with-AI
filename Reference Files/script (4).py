
# Component 5: Search Bar
search_bar_content = """
================================================================================
ENHANCED SEARCH BAR COMPONENT
================================================================================

IMPROVEMENTS MADE:
1. Added animated search suggestions/autocomplete
2. Improved expand/collapse animations with smooth transitions
3. Added voice search button functionality
4. Enhanced accessibility with ARIA labels
5. Added loading state indicator
6. Improved mobile responsiveness
7. Added search history feature
8. Better visual feedback with modern styling
9. Added clear button when text is entered
10. Improved keyboard navigation (Enter to search, Escape to close)

================================================================================
index.html
================================================================================

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Enhanced Search Bar</title>
    <link rel="stylesheet" href="style.css" />
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
</head>
<body>
    <div class="container">
        <div class="search-wrapper">
            <input 
                type="text" 
                class="search-input" 
                placeholder="Search anything..."
                aria-label="Search input"
                autocomplete="off"
            />
            
            <button class="search-btn" aria-label="Search" title="Search">
                <i class='bx bx-search'></i>
            </button>
            
            <button class="clear-btn" aria-label="Clear search" title="Clear" style="display: none;">
                <i class='bx bx-x'></i>
            </button>
            
            <button class="voice-btn" aria-label="Voice search" title="Voice Search">
                <i class='bx bx-microphone'></i>
            </button>
            
            <div class="loading-spinner" style="display: none;">
                <i class='bx bx-loader-alt bx-spin'></i>
            </div>
            
            <div class="suggestions-box">
                <div class="suggestions-header">
                    <span>Recent Searches</span>
                    <button class="clear-history" aria-label="Clear history">
                        <i class='bx bx-trash'></i>
                    </button>
                </div>
                <ul class="suggestions-list">
                    <!-- Suggestions will be dynamically added here -->
                </ul>
            </div>
        </div>
        
        <div class="search-info">
            <p class="info-text">Try searching for: Technology, Design, Art, Science</p>
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
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}

body {
    width: 100%;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    font-family: 'Poppins', sans-serif;
}

.container {
    width: 100%;
    max-width: 700px;
    padding: 20px;
}

.search-wrapper {
    position: relative;
    width: 100%;
    height: 70px;
    display: flex;
    align-items: center;
    background: #ffffff;
    border-radius: 50px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

.search-wrapper:focus-within {
    box-shadow: 0 15px 50px rgba(0, 0, 0, 0.4),
                0 0 0 4px rgba(255, 255, 255, 0.3);
    transform: translateY(-2px);
}

.search-input {
    flex: 1;
    height: 100%;
    background: transparent;
    border: none;
    outline: none;
    font-size: 18px;
    font-weight: 500;
    color: #333;
    padding: 0 25px;
    letter-spacing: 0.5px;
}

.search-input::placeholder {
    color: #999;
    font-weight: 400;
}

.search-btn,
.clear-btn,
.voice-btn {
    width: 55px;
    height: 55px;
    border-radius: 50%;
    border: none;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    font-size: 24px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.3s ease;
    margin-right: 8px;
}

.search-btn:hover,
.voice-btn:hover {
    transform: scale(1.1);
    box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
}

.search-btn:active,
.voice-btn:active {
    transform: scale(0.95);
}

.clear-btn {
    width: 40px;
    height: 40px;
    font-size: 20px;
    background: #ff4757;
    animation: fadeIn 0.3s ease;
}

.clear-btn:hover {
    transform: scale(1.1);
    box-shadow: 0 5px 15px rgba(255, 71, 87, 0.4);
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: scale(0.8);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

.voice-btn {
    margin-right: 8px;
}

.voice-btn.listening {
    background: #ff4757;
    animation: pulse 1.5s infinite;
}

@keyframes pulse {
    0%, 100% {
        box-shadow: 0 0 0 0 rgba(255, 71, 87, 0.7);
    }
    50% {
        box-shadow: 0 0 0 15px rgba(255, 71, 87, 0);
    }
}

.loading-spinner {
    position: absolute;
    right: 80px;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #667eea;
    font-size: 28px;
}

.suggestions-box {
    position: absolute;
    top: calc(100% + 15px);
    left: 0;
    width: 100%;
    background: white;
    border-radius: 20px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
    max-height: 0;
    overflow: hidden;
    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    opacity: 0;
    z-index: 10;
}

.search-wrapper.active .suggestions-box {
    max-height: 400px;
    opacity: 1;
}

.suggestions-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 25px 10px;
    border-bottom: 2px solid #f0f0f0;
}

.suggestions-header span {
    font-size: 14px;
    font-weight: 600;
    color: #666;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.clear-history {
    background: none;
    border: none;
    color: #ff4757;
    font-size: 18px;
    cursor: pointer;
    padding: 5px;
    border-radius: 5px;
    transition: all 0.3s ease;
}

.clear-history:hover {
    background: #fff0f1;
    transform: scale(1.1);
}

.suggestions-list {
    list-style: none;
    padding: 10px 0;
    max-height: 300px;
    overflow-y: auto;
}

.suggestions-list::-webkit-scrollbar {
    width: 6px;
}

.suggestions-list::-webkit-scrollbar-track {
    background: #f1f1f1;
}

.suggestions-list::-webkit-scrollbar-thumb {
    background: #888;
    border-radius: 10px;
}

.suggestion-item {
    padding: 15px 25px;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 15px;
    animation: slideIn 0.3s ease backwards;
    animation-delay: calc(var(--i) * 0.05s);
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

.suggestion-item:hover {
    background: #f8f9fa;
}

.suggestion-item i {
    font-size: 20px;
    color: #667eea;
}

.suggestion-item span {
    font-size: 16px;
    color: #333;
    font-weight: 500;
}

.search-info {
    margin-top: 30px;
    text-align: center;
}

.info-text {
    color: white;
    font-size: 16px;
    opacity: 0.9;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
}

@media (max-width: 768px) {
    .container {
        max-width: 500px;
    }
    
    .search-wrapper {
        height: 60px;
    }
    
    .search-input {
        font-size: 16px;
        padding: 0 20px;
    }
    
    .search-btn,
    .voice-btn {
        width: 48px;
        height: 48px;
        font-size: 20px;
    }
}

@media (max-width: 480px) {
    .search-wrapper {
        height: 55px;
        border-radius: 40px;
    }
    
    .search-input {
        font-size: 14px;
        padding: 0 15px;
    }
    
    .search-btn,
    .voice-btn {
        width: 42px;
        height: 42px;
        font-size: 18px;
        margin-right: 6px;
    }
}

================================================================================
script.js
================================================================================

const searchWrapper = document.querySelector('.search-wrapper');
const searchInput = document.querySelector('.search-input');
const searchBtn = document.querySelector('.search-btn');
const clearBtn = document.querySelector('.clear-btn');
const voiceBtn = document.querySelector('.voice-btn');
const loadingSpinner = document.querySelector('.loading-spinner');
const suggestionsList = document.querySelector('.suggestions-list');
const clearHistoryBtn = document.querySelector('.clear-history');

// Sample search history (in a real app, this would be stored in localStorage)
let searchHistory = [
    'Web Development',
    'JavaScript Tutorial',
    'CSS Animations',
    'UI/UX Design',
    'React Components'
];

// Sample suggestions
const sampleSuggestions = [
    'Technology',
    'Design Trends',
    'Programming',
    'Digital Art',
    'Machine Learning',
    'Mobile Development',
    'Cloud Computing'
];

// Show suggestions when input is focused
searchInput.addEventListener('focus', () => {
    searchWrapper.classList.add('active');
    renderSuggestions(searchHistory);
});

// Hide suggestions when clicking outside
document.addEventListener('click', (e) => {
    if (!searchWrapper.contains(e.target)) {
        searchWrapper.classList.remove('active');
    }
});

// Show/hide clear button based on input
searchInput.addEventListener('input', () => {
    if (searchInput.value.length > 0) {
        clearBtn.style.display = 'flex';
    } else {
        clearBtn.style.display = 'none';
    }
    
    // Filter suggestions based on input
    const filtered = searchHistory.filter(item => 
        item.toLowerCase().includes(searchInput.value.toLowerCase())
    );
    renderSuggestions(filtered);
});

// Clear input
clearBtn.addEventListener('click', () => {
    searchInput.value = '';
    clearBtn.style.display = 'none';
    searchInput.focus();
    renderSuggestions(searchHistory);
});

// Search functionality
function performSearch() {
    const query = searchInput.value.trim();
    if (query) {
        // Show loading state
        loadingSpinner.style.display = 'flex';
        searchBtn.style.display = 'none';
        
        // Simulate search delay
        setTimeout(() => {
            loadingSpinner.style.display = 'none';
            searchBtn.style.display = 'flex';
            
            // Add to search history
            if (!searchHistory.includes(query)) {
                searchHistory.unshift(query);
                if (searchHistory.length > 10) {
                    searchHistory.pop();
                }
            }
            
            console.log('Searching for:', query);
            alert(`Searching for: ${query}`);
            
            searchWrapper.classList.remove('active');
        }, 1000);
    }
}

searchBtn.addEventListener('click', performSearch);

searchInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        performSearch();
    } else if (e.key === 'Escape') {
        searchWrapper.classList.remove('active');
        searchInput.blur();
    }
});

// Voice search functionality
voiceBtn.addEventListener('click', () => {
    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        const recognition = new SpeechRecognition();
        
        recognition.onstart = () => {
            voiceBtn.classList.add('listening');
        };
        
        recognition.onresult = (event) => {
            const transcript = event.results[0][0].transcript;
            searchInput.value = transcript;
            clearBtn.style.display = 'flex';
            voiceBtn.classList.remove('listening');
            performSearch();
        };
        
        recognition.onerror = () => {
            voiceBtn.classList.remove('listening');
            alert('Voice search not available or permission denied');
        };
        
        recognition.onend = () => {
            voiceBtn.classList.remove('listening');
        };
        
        recognition.start();
    } else {
        alert('Voice search is not supported in your browser');
    }
});

// Render suggestions
function renderSuggestions(suggestions) {
    suggestionsList.innerHTML = '';
    
    if (suggestions.length === 0) {
        suggestions = sampleSuggestions;
    }
    
    suggestions.forEach((suggestion, index) => {
        const li = document.createElement('li');
        li.className = 'suggestion-item';
        li.style.setProperty('--i', index);
        li.innerHTML = `
            <i class='bx bx-search-alt'></i>
            <span>${suggestion}</span>
        `;
        
        li.addEventListener('click', () => {
            searchInput.value = suggestion;
            clearBtn.style.display = 'flex';
            performSearch();
        });
        
        suggestionsList.appendChild(li);
    });
}

// Clear search history
clearHistoryBtn.addEventListener('click', () => {
    if (confirm('Clear all search history?')) {
        searchHistory = [];
        renderSuggestions(sampleSuggestions);
    }
});

// Initialize
renderSuggestions(searchHistory);
"""

with open('5_Enhanced_Search_Bar.txt', 'w', encoding='utf-8') as f:
    f.write(search_bar_content)

print("✓ Created: 5_Enhanced_Search_Bar.txt")
