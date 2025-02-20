function calculateResult() {
    // Count the answers
    const answers = { shinchan: 0, misae: 0, himawari: 0, hiroshi: 0 };
    
    const q1 = document.querySelector('input[name="q1"]:checked');
    const q2 = document.querySelector('input[name="q2"]:checked');
    const q3 = document.querySelector('input[name="q3"]:checked');

    if (q1) answers[q1.value]++;
    if (q2) answers[q2.value]++;
    if (q3) answers[q3.value]++;

    // Determine the result
    let result = Object.keys(answers).reduce((a, b) => answers[a] > answers[b] ? a : b);

    // Show result text and image
    const resultText = document.getElementById("result-text");
    const resultImage = document.getElementById("result-image");
    const resultContainer = document.getElementById("result");

    if (result === "shinchan") {
        resultText.textContent = "You are Shinchan! Playful, mischievous, and full of energy!";
        resultImage.src = "images/shin.png";  // Updated path
    } else if (result === "misae") {
        resultText.textContent = "You are Misae! Caring, responsible, but can lose your temper!";
        resultImage.src = "images/mixie.png";     // Updated path
    } else if (result === "himawari") {
        resultText.textContent = "You are Himawari! Cute, curious, and loves adorable things!";
        resultImage.src = "images/himawari.png";  // Updated path
    } else if (result === "hiroshi") {
        resultText.textContent = "You are Hiroshi! Hardworking, patient, and a bit lazy!";
        resultImage.src = "images/harry.png";   // Updated path
    }

    resultContainer.style.display = "block";
}
