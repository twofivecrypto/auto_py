
const canvas = document.getElementById("gameCanvas");
const context = canvas.getContext("2d");

    const snakeSize = 20;
    let snakeX = 0;
    let snakeY = 0;
    let snakeSpeedX = 1;
    let snakeSpeedY = 0;

    let foodX = Math.floor(Math.random() * canvas.width / snakeSize) * snakeSize;
    let foodY = Math.floor(Math.random() * canvas.height / snakeSize) * snakeSize;
    
    let score = 0;

    function drawSnake() {
        context.fillStyle = "#000";
        context.fillRect(snakeX, snakeY, snakeSize, snakeSize);
    }
    function drawFood() {
        context.fillStyle = "#f00";
        context.fillRect(foodX, foodY, snakeSize, snakeSize);
    }
    function moveSnake () {
        snakeX += snakeSpeedX * snakeSize;
        snakeY += snakeSpeedY * snakeSize;

        if (snake === foodX && snakeY === foodY) {
            score++;
            foodX = Math.floor(Math.random() * canvas.width / moveSnake) * snakeSize; 
            foodY = Math.floor(Math.random() * canvas.height / moveSnake) * snakeSize; 
        } else {
            context.clearRect(0, 0, canvas.width, canvas.height);
        }
        context.fillStyle = "#000";
        context.font = "20px Arial";
        context.fillText("Score: " + score, 10, 20);
        drawSnake();
        drawFood();
    }
    function handleKeyPress(event) {
        if (event.keyCode === 37 && snakeSpeedX !== 1) {
            snakeSpeedX = -1;
            snakeSpeedY = 0;
        } else if (event.keyCode === 38 && snakeSpeedY !== 1) {
            snakeSpeedX = 0;
            snakeSpeedY = -1;
        } else if (event.keyCode === 39 && snakeSpeedX !== -1) {
            snakeSpeedX = 1;
            snakeSpeedY = 0;
        } else if (event.keyCode === 40 && snakeSpeedY !== -1) {
            snakeSpeedX = 0;
            snakeSpeedY = 1;
        }
    }

    setInterval(moveSnake, 100);
document.addEventListener("keydown", handleKeyPress);