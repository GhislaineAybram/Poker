let flopStep = 0
let gameOver = false

const toggleCardVisibility = () => {
    flopStep += 1;
    const cardDisplay = document.getElementById("flop-" + flopStep);
    if (cardDisplay.style.display === "none") {
        cardDisplay.style.display = "flex";
        };
    if (flopStep === 3) {
        gameOver = true;
        endGame();
        newGame();
        }
    }

const endGame = () => {
    const conclusions = document.querySelectorAll(".conclusion");
    const opponents = document.querySelectorAll(".card-opponent");
    const opponentValues = document.querySelectorAll(".card-opponent-value");
    conclusions.forEach(conclusion => {
        conclusion.style.display = gameOver ? "flex" : "none";
        });
    opponents.forEach(opponent => {
        opponent.style.backgroundImage = gameOver ? "" : "url('{{ url_for('static', filename='img/Lotus_back.jpg') }}')";
        });
    opponentValues.forEach(opponentValue => {
        opponentValue.style.display = gameOver ? "block" : "none";
        });
    }

const newGame = () => {
    const buttonNewGame = document.getElementById("button-new-game");
    if (buttonNewGame.style.display === "none") {
        buttonNewGame.style.display = "flex";
        }
    }