
# Component 3: 3D CSS Social Tiles
social_tiles_content = """
================================================================================
ENHANCED 3D CSS SOCIAL TILES COMPONENT
================================================================================

IMPROVEMENTS MADE:
1. Updated to modern social media platforms (Added Discord, LinkedIn, removed Google Plus)
2. Improved 3D transform effects with better perspective
3. Added smooth color transitions and hover animations
4. Enhanced shadow effects with multiple layers
5. Improved accessibility with ARIA labels and keyboard navigation
6. Better responsive design with flexbox
7. Added modern color schemes for each platform
8. Improved icon sizing and positioning
9. Added entrance animations for tiles
10. Better organized CSS with custom properties

================================================================================
index.html
================================================================================

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Enhanced 3D Social Tiles</title>
    <link rel="stylesheet" href="style.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
</head>
<body>
    <div class="container">
        <h1 class="title">Connect With Us</h1>
        <ul class="social-tiles">
            <li class="tile" style="--delay: 0.1s;">
                <a href="#" aria-label="Follow us on Facebook">
                    <i class="fab fa-facebook-f" aria-hidden="true"></i>
                    <span class="platform-name">Facebook</span>
                </a>
            </li>
            <li class="tile" style="--delay: 0.2s;">
                <a href="#" aria-label="Follow us on Twitter">
                    <i class="fab fa-twitter" aria-hidden="true"></i>
                    <span class="platform-name">Twitter</span>
                </a>
            </li>
            <li class="tile" style="--delay: 0.3s;">
                <a href="#" aria-label="Follow us on Instagram">
                    <i class="fab fa-instagram" aria-hidden="true"></i>
                    <span class="platform-name">Instagram</span>
                </a>
            </li>
            <li class="tile" style="--delay: 0.4s;">
                <a href="#" aria-label="Connect on LinkedIn">
                    <i class="fab fa-linkedin-in" aria-hidden="true"></i>
                    <span class="platform-name">LinkedIn</span>
                </a>
            </li>
            <li class="tile" style="--delay: 0.5s;">
                <a href="#" aria-label="Join our Discord">
                    <i class="fab fa-discord" aria-hidden="true"></i>
                    <span class="platform-name">Discord</span>
                </a>
            </li>
        </ul>
    </div>
</body>
</html>

================================================================================
style.css
================================================================================

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

:root {
    --facebook: #3b5998;
    --facebook-dark: #2d4373;
    --facebook-light: #4a69ad;
    --twitter: #1da1f2;
    --twitter-dark: #0c85d0;
    --twitter-light: #53b9e0;
    --instagram: #e4405f;
    --instagram-dark: #d81c3f;
    --instagram-light: #e46880;
    --linkedin: #0077b5;
    --linkedin-dark: #005885;
    --linkedin-light: #0095d5;
    --discord: #5865f2;
    --discord-dark: #4752c4;
    --discord-light: #7289da;
}

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
    perspective: 1500px;
    overflow-x: hidden;
}

.container {
    text-align: center;
    padding: 40px 20px;
}

.title {
    color: white;
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 60px;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    animation: fadeInDown 0.8s ease-out;
}

@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.social-tiles {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    gap: 30px;
    list-style: none;
    padding: 0;
}

.tile {
    animation: fadeInUp 0.6s ease-out backwards;
    animation-delay: var(--delay);
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px) rotateX(-15deg);
    }
    to {
        opacity: 1;
        transform: translateY(0) rotateX(0);
    }
}

.tile a {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    width: 240px;
    height: 85px;
    background: #ffffff;
    text-decoration: none;
    padding-left: 25px;
    border-radius: 10px;
    position: relative;
    transform-style: preserve-3d;
    transform: rotateX(10deg) rotateY(-10deg);
    transition: all 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    box-shadow: 
        -15px 15px 20px rgba(0, 0, 0, 0.3),
        -5px 5px 10px rgba(0, 0, 0, 0.2),
        inset 0 -2px 5px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}

.tile a::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
    transition: left 0.5s;
}

.tile a:hover::before {
    left: 100%;
}

.tile a::after {
    content: '';
    position: absolute;
    top: 12px;
    left: -22px;
    height: 100%;
    width: 22px;
    background: #b1b1b1;
    transform-origin: bottom;
    transform: rotateY(90deg) rotateZ(-45deg);
    transition: background 0.4s;
}

.tile a .fa-facebook-f,
.tile a .fa-twitter,
.tile a .fa-instagram,
.tile a .fa-linkedin-in,
.tile a .fa-discord {
    font-size: 42px;
    color: #262626;
    transition: all 0.4s ease;
    z-index: 2;
    margin-right: 18px;
}

.tile a .platform-name {
    font-size: 20px;
    font-weight: 600;
    color: #262626;
    letter-spacing: 1px;
    transition: all 0.4s ease;
    z-index: 2;
}

.tile a:hover {
    transform: rotateX(0deg) rotateY(0deg) translateY(-10px);
    box-shadow: 
        -30px 30px 40px rgba(0, 0, 0, 0.4),
        -10px 10px 20px rgba(0, 0, 0, 0.3);
}

.tile a:active {
    transform: rotateX(0deg) rotateY(0deg) translateY(-5px);
}

/* Facebook */
.tile:nth-child(1) a:hover {
    background: var(--facebook);
}

.tile:nth-child(1) a:hover::after {
    background: var(--facebook-dark);
}

.tile:nth-child(1) a:hover .fa-facebook-f,
.tile:nth-child(1) a:hover .platform-name {
    color: #ffffff;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

/* Twitter */
.tile:nth-child(2) a:hover {
    background: var(--twitter);
}

.tile:nth-child(2) a:hover::after {
    background: var(--twitter-dark);
}

.tile:nth-child(2) a:hover .fa-twitter,
.tile:nth-child(2) a:hover .platform-name {
    color: #ffffff;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

/* Instagram */
.tile:nth-child(3) a:hover {
    background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
}

.tile:nth-child(3) a:hover::after {
    background: var(--instagram-dark);
}

.tile:nth-child(3) a:hover .fa-instagram,
.tile:nth-child(3) a:hover .platform-name {
    color: #ffffff;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

/* LinkedIn */
.tile:nth-child(4) a:hover {
    background: var(--linkedin);
}

.tile:nth-child(4) a:hover::after {
    background: var(--linkedin-dark);
}

.tile:nth-child(4) a:hover .fa-linkedin-in,
.tile:nth-child(4) a:hover .platform-name {
    color: #ffffff;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

/* Discord */
.tile:nth-child(5) a:hover {
    background: var(--discord);
}

.tile:nth-child(5) a:hover::after {
    background: var(--discord-dark);
}

.tile:nth-child(5) a:hover .fa-discord,
.tile:nth-child(5) a:hover .platform-name {
    color: #ffffff;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

/* Focus states for accessibility */
.tile a:focus {
    outline: 3px solid rgba(255, 255, 255, 0.8);
    outline-offset: 5px;
}

@media (max-width: 768px) {
    .title {
        font-size: 2rem;
        margin-bottom: 40px;
    }
    
    .social-tiles {
        gap: 20px;
    }
    
    .tile a {
        width: 200px;
        height: 70px;
        padding-left: 20px;
    }
    
    .tile a .fa-facebook-f,
    .tile a .fa-twitter,
    .tile a .fa-instagram,
    .tile a .fa-linkedin-in,
    .tile a .fa-discord {
        font-size: 32px;
        margin-right: 14px;
    }
    
    .tile a .platform-name {
        font-size: 16px;
    }
}

@media (max-width: 480px) {
    .tile a {
        width: 180px;
        height: 65px;
    }
}
"""

with open('3_Enhanced_3D_Social_Tiles.txt', 'w', encoding='utf-8') as f:
    f.write(social_tiles_content)

print("✓ Created: 3_Enhanced_3D_Social_Tiles.txt")
