let flopStep = 0

const toggleCardVisibility = () => {
    flopStep += 1;
    const cardDisplay = document.getElementById("flop-" + flopStep);
    if (cardDisplay.style.display === "none") {
        cardDisplay.style.display = "flex";
        };
    if (flopStep === 3) {
        endGame();
        newGame();
        }
    }

const endGame = () => {
    const conclusion = document.getElementById("conclusion");
    const combinaison1 = document.getElementById("combinaison-1");
    const combinaison2 = document.getElementById("combinaison-2");
    if (conclusion.style.display === "none") {
        conclusion.style.display = "flex";
        }
    if (combinaison1.style.display === "none") {
        combinaison1.style.display = "flex";
        }
    if (combinaison2.style.display === "none") {
        combinaison2.style.display = "flex";
        }
    }

const newGame = () => {
    const buttonNewGame = document.getElementById("conclusion");
    if (buttonNewGame.style.display === "none") {
        buttonNewGame.style.display = "flex";
        }
    }