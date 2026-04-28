const dino = document.getElementById('dino');
const world = document.getElementById('world');
const scoreElement = document.getElementById('score-val');
const hiScoreElement = document.getElementById('hi-val');
const startScreen = document.getElementById('start-screen');
const gameOverScreen = document.getElementById('game-over');
const ground = document.querySelector('.ground');

// Game state
let isGameStarted = false;
let isGameOver = false;
let score = 0;
let hiScore = localStorage.getItem('neonRunnerHiScore') || 0;
hiScoreElement.textContent = Math.floor(hiScore);

let lastTime;
let speedScale = 1;
const SPEED_SCALE_INCREASE = 0.00001;

// Dino physics
let isJumping = false;
let dinoY = 34; // starting ground position
let velocity = 0;
const GRAVITY = -0.06;
const JUMP_POWER = 12; // Initial upward speed

// Obstacles
let obstacles = [];
let spawnTimer = 0;
const MIN_SPAWN_TIME = 800; // ms
const MAX_SPAWN_TIME = 2000; // ms

// Handle Input
function handleInput(e) {
    // Only accept Space key or touch
    if ((e.type === 'keydown' && e.code === 'Space') || e.type === 'touchstart') {
        if (!isGameStarted) {
            startGame();
        } else if (isGameOver) {
            startGame();
        } else if (!isJumping) {
            jump();
        }
    }
}
document.addEventListener('keydown', handleInput);
document.addEventListener('touchstart', handleInput);

function jump() {
    isJumping = true;
    velocity = JUMP_POWER;
}

function startGame() {
    isGameStarted = true;
    isGameOver = false;
    startScreen.classList.add('hidden');
    gameOverScreen.classList.add('hidden');
    score = 0;
    obstacles.forEach(obs => obs.element.remove());
    obstacles = [];
    speedScale = 1;
    dinoY = 34;
    velocity = 0;
    isJumping = false;
    lastTime = null;
    requestAnimationFrame(update);
}

function spawnObstacle() {
    const obstacleEl = document.createElement('div');
    obstacleEl.classList.add('obstacle');
    
    // Randomize obstacle type
    const rand = Math.random();
    if (rand < 0.2) obstacleEl.classList.add('tall');
    else if (rand < 0.4) obstacleEl.classList.add('wide');

    world.appendChild(obstacleEl);
    
    const obs = {
        element: obstacleEl,
        x: 800, // starts at right edge of container
        width: obstacleEl.classList.contains('wide') ? 40 : 20,
        height: obstacleEl.classList.contains('tall') ? 60 : 40,
    };
    obstacleEl.style.left = obs.x + 'px';
    obstacles.push(obs);

    spawnTimer = Math.random() * (MAX_SPAWN_TIME - MIN_SPAWN_TIME) + MIN_SPAWN_TIME;
    spawnTimer /= speedScale; // spawn faster as game speeds up
}

function update(time) {
    if (isGameOver) return;
    if (lastTime == null) {
        lastTime = time;
        requestAnimationFrame(update);
        return;
    }

    const delta = time - lastTime;
    lastTime = time;

    updateDino(delta);
    updateObstacles(delta);
    
    // Update Score
    score += delta * 0.01 * speedScale;
    scoreElement.textContent = Math.floor(score);
    speedScale += delta * SPEED_SCALE_INCREASE;

    if (checkCollision()) {
        endGame();
    } else {
        requestAnimationFrame(update);
    }
}

function updateDino(delta) {
    if (isJumping) {
        velocity += GRAVITY * delta;
        dinoY += velocity * (delta * 0.05);

        if (dinoY <= 34) {
            dinoY = 34;
            isJumping = false;
            velocity = 0;
        }
    }
    dino.style.bottom = dinoY + 'px';
}

function updateObstacles(delta) {
    spawnTimer -= delta;
    if (spawnTimer <= 0) {
        spawnObstacle();
    }

    obstacles.forEach((obs, index) => {
        // Move obstacle left
        obs.x -= 0.4 * delta * speedScale;
        obs.element.style.left = obs.x + 'px';

        // Remove if off screen
        if (obs.x + obs.width < 0) {
            obs.element.remove();
            obstacles.splice(index, 1);
        }
    });
}

function checkCollision() {
    const dinoRect = dino.getBoundingClientRect();
    
    // Reduce hitbox slightly for fair gameplay
    const dinoHitbox = {
        left: dinoRect.left + 5,
        right: dinoRect.right - 5,
        top: dinoRect.top + 5,
        bottom: dinoRect.bottom - 5
    };

    return obstacles.some(obs => {
        const obsRect = obs.element.getBoundingClientRect();
        return (
            dinoHitbox.right > obsRect.left &&
            dinoHitbox.left < obsRect.right &&
            dinoHitbox.bottom > obsRect.top &&
            dinoHitbox.top < obsRect.bottom
        );
    });
}

function endGame() {
    isGameOver = true;
    gameOverScreen.classList.remove('hidden');
    
    const finalScore = Math.floor(score);
    if (finalScore > hiScore) {
        hiScore = finalScore;
        localStorage.setItem('neonRunnerHiScore', hiScore);
        hiScoreElement.textContent = hiScore;
    }
}
