// Function to play the initial sound when the page loads
window.onload = function() {
    const initialAudio = document.getElementById("initialAudio");
    initialAudio.play().catch((error) => {
        console.log("Initial audio file not found or failed to play.");
    });
};

// Function to determine if the user wins
function gameWin(comp, you) {
    if (comp === you) {
        return null;
    } else if ((comp === 'F' && you === 'M') || (comp === 'L' && you === 'F') || (comp === 'M' && you === 'L')) {
        return true;
    } else {
        return false;
    }
}

// Main game function
function playGame(userChoice) {
    const resultDiv = document.getElementById("result");
    const choices = ['F', 'L', 'M'];
    const compChoice = choices[Math.floor(Math.random() * choices.length)];

    const gameResult = gameWin(compChoice, userChoice);

    resultDiv.innerHTML = `
        <p>Computer chose: ${compChoice}</p>
        <p>You chose: ${userChoice}</p>
    `;

    if (gameResult === null) {
        resultDiv.innerHTML += `<p>The game is a tie!</p>`;
    } else if (gameResult) {
        resultDiv.innerHTML += `<p>You Win!</p>`;
        
        // Play winning sound
        const winningAudio = document.getElementById("winningAudio");
        winningAudio.play().catch((error) => {
            console.log("Winning audio file not found or failed to play.");
        });
    } else {
        resultDiv.innerHTML += `<p>You Lose!</p>`;
    }
}
