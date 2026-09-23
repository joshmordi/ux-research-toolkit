const questions = [
  "I think that I would like to use this system frequently.",
  "I found the system unnecessarily complex.",
  "I thought the system was easy to use.",
  "I think that I would need the support of a technical person to be able to use this system.",
  "I found the various functions in this system were well integrated.",
  "I thought there was too much inconsistency in this system.",
  "I would imagine that most people would learn to use this system very quickly.",
  "I found the system very cumbersome to use.",
  "I felt very confident using the system.",
  "I needed to learn a lot of things before I could get going with this system."
];

const container = document.getElementById("questions");
questions.forEach((text, i) => {
  const div = document.createElement("div");
  div.className = "q";
  let opts = "";
  for (let v = 1; v <= 5; v++) {
    opts += `<label><input type="radio" name="q${i}" value="${v}"> ${v}</label>`;
  }
  div.innerHTML = `<p><strong>${i + 1}.</strong> ${text}</p><div class="opts">${opts}</div>`;
  container.appendChild(div);
});

function calculate() {
  let total = 0;
  for (let i = 0; i < 10; i++) {
    const checked = document.querySelector(`input[name="q${i}"]:checked`);
    if (!checked) {
      document.getElementById("result").textContent = "Please answer all 10 questions.";
      document.getElementById("interp").textContent = "";
      return;
    }
    const r = parseInt(checked.value, 10);
    total += (i % 2 === 0) ? (r - 1) : (5 - r);
  }
  const score = total * 2.5;
  document.getElementById("result").textContent = "SUS score: " + score.toFixed(1) + " / 100";
  let interp;
  if (score >= 80.3) interp = "Grade A: excellent usability.";
  else if (score >= 68) interp = "Grade B: above average. A score of 68 is the commonly cited average.";
  else if (score >= 51) interp = "Grade C: below average, worth improving.";
  else interp = "Grade D/F: poor usability, needs work.";
  document.getElementById("interp").textContent = interp;
}
