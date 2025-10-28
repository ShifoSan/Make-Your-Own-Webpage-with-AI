
# Create enhanced versions of all components as separate text files

# Component 1: HTML Tooltip
tooltip_content = """
================================================================================
ENHANCED HTML TOOLTIP COMPONENT
================================================================================

IMPROVEMENTS MADE:
1. Added accessibility features with ARIA labels
2. Improved positioning system with multiple placement options (top, right, bottom)
3. Added smooth fade-in animation with scale effect
4. Enhanced color scheme with modern gradient
5. Added support for longer tooltip text with max-width
6. Improved responsive design for mobile devices
7. Better visual hierarchy and contrast

================================================================================
index.html
================================================================================

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Enhanced Tooltip</title>
    <link rel="stylesheet" href="style.css" />
</head>
<body>
    <div class="demo-container">
        <div class="main" data-tooltip="CodeByGaurav - Modern UI Developer" aria-label="Hover for more info">
            <span class="text">Tooltip Demo</span>
        </div>
        
        <div class="main" data-tooltip="This tooltip appears on the right side" data-position="right">
            <span class="text">Right Tooltip</span>
        </div>
        
        <div class="main" data-tooltip="Bottom tooltip with longer descriptive text for demonstration" data-position="bottom">
            <span class="text">Bottom Tooltip</span>
        </div>
    </div>
</body>
</html>

================================================================================
style.css
================================================================================

* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}

body {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.demo-container {
    display: flex;
    gap: 40px;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
}

.main {
    position: relative;
    background: #ffffff;
    color: #2d3748;
    padding: 20px 30px;
    border-radius: 12px;
    font-size: 16px;
    font-weight: 600;
    letter-spacing: 0.5px;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2), 
                0 1px 3px rgba(0, 0, 0, 0.1);
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    user-select: none;
}

.main:hover {
    transform: translateY(-2px);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.25),
                0 5px 10px rgba(0, 0, 0, 0.15);
}

.main::before {
    content: attr(data-tooltip);
    position: absolute;
    top: -45px;
    left: 50%;
    transform: translateX(-50%) scale(0.9);
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: #ffffff;
    padding: 10px 16px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 500;
    white-space: nowrap;
    max-width: 250px;
    text-overflow: ellipsis;
    overflow: hidden;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
    transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    z-index: 1000;
}

.main::after {
    content: '';
    position: absolute;
    top: -8px;
    left: 50%;
    transform: translateX(-50%) rotate(45deg) scale(0.9);
    width: 12px;
    height: 12px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    opacity: 0;
    visibility: hidden;
    transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    z-index: 999;
}

.main:hover::before {
    top: -55px;
    opacity: 1;
    visibility: visible;
    transform: translateX(-50%) scale(1);
}

.main:hover::after {
    top: -18px;
    opacity: 1;
    visibility: visible;
    transform: translateX(-50%) rotate(45deg) scale(1);
}

/* Right positioned tooltip */
.main[data-position="right"]::before {
    top: 50%;
    left: calc(100% + 15px);
    transform: translateY(-50%) scale(0.9);
}

.main[data-position="right"]::after {
    top: 50%;
    left: calc(100% + 4px);
    transform: translateY(-50%) rotate(45deg) scale(0.9);
}

.main[data-position="right"]:hover::before {
    left: calc(100% + 20px);
    transform: translateY(-50%) scale(1);
}

.main[data-position="right"]:hover::after {
    left: calc(100% + 9px);
    transform: translateY(-50%) rotate(45deg) scale(1);
}

/* Bottom positioned tooltip */
.main[data-position="bottom"]::before {
    top: calc(100% + 15px);
    transform: translateX(-50%) scale(0.9);
}

.main[data-position="bottom"]::after {
    top: calc(100% + 4px);
    transform: translateX(-50%) rotate(45deg) scale(0.9);
}

.main[data-position="bottom"]:hover::before {
    top: calc(100% + 20px);
    transform: translateX(-50%) scale(1);
}

.main[data-position="bottom"]:hover::after {
    top: calc(100% + 9px);
    transform: translateX(-50%) rotate(45deg) scale(1);
}

@media (max-width: 768px) {
    .demo-container {
        flex-direction: column;
        gap: 30px;
    }
    
    .main::before {
        white-space: normal;
        max-width: 200px;
    }
}
"""

with open('1_Enhanced_HTML_Tooltip.txt', 'w', encoding='utf-8') as f:
    f.write(tooltip_content)

print("✓ Created: 1_Enhanced_HTML_Tooltip.txt")
