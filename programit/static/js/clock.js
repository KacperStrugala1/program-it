document.addEventListener("DOMContentLoaded", () => {
  const display = document.getElementById("display");
  const startBtn = document.querySelector('button[name="action"][value="start"]');
  const stopBtn = document.querySelector('button[name="action"][value="stop"]');
  const recentList = document.querySelector("ul");

  let startTime = 0;
  let elapsedTime = 0;
  let timerInterval = null;
  let running = false;

  // ------------------------------
  // Formatowanie czasu
  // ------------------------------
  function formatTime(ms) {
    const totalSeconds = Math.floor(ms / 1000);
    const minutes = Math.floor(totalSeconds / 60);
    const seconds = totalSeconds % 60;
    return `${minutes.toString().padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;
  }

  function updateDisplay() {
    display.textContent = formatTime(elapsedTime);
  }

  // ------------------------------
  // Start / Stop / Reset
  // ------------------------------
  function startTimer() {
    if (running) return;
    running = true;
    startTime = Date.now() - elapsedTime;
    timerInterval = setInterval(() => {
      elapsedTime = Date.now() - startTime;
      updateDisplay();
    }, 100);
  }

  function stopTimer() {
    if (!running) return;
    running = false;
    clearInterval(timerInterval);

    // Zapisz czas do listy po zatrzymaniu
    const timeString = formatTime(elapsedTime);
    addRecentTime(timeString);
    saveTimes();
  }

  function resetTimer() {
    stopTimer();
    elapsedTime = 0;
    updateDisplay();
  }

  // ------------------------------
  // Tworzenie przycisku Reset
  // ------------------------------
  const resetBtn = document.createElement("button");
  resetBtn.textContent = "↺ Reset";
  resetBtn.className = "px-4 py-2 rounded bg-[#d19a66] text-[#1e1e1e] font-semibold hover:bg-[#c18456] transition";
  stopBtn.parentNode.appendChild(resetBtn);

  // ------------------------------
  // Obsługa zdarzeń
  // ------------------------------
  startBtn.addEventListener("click", (e) => {
    e.preventDefault();
    startTimer();
  });

  stopBtn.addEventListener("click", (e) => {
    e.preventDefault();
    stopTimer();
  });

  resetBtn.addEventListener("click", (e) => {
    e.preventDefault();
    resetTimer();
  });

  // ------------------------------
  // Recent Times — zapisywanie i ładowanie
  // ------------------------------
  function addRecentTime(time) {
    const li = document.createElement("li");
    li.textContent = `• ${time}`;
    li.className = "animate-pulse text-[#98c379]";
    recentList.prepend(li); // dodaj na górę listy
  }

  function saveTimes() {
    const times = Array.from(recentList.querySelectorAll("li")).map(li => li.textContent.replace("• ", ""));
    localStorage.setItem("recentTimes", JSON.stringify(times));
  }

  function loadTimes() {
    const stored = JSON.parse(localStorage.getItem("recentTimes") || "[]");
    stored.forEach(time => addRecentTime(time));
  }

  // ------------------------------
  // Inicjalizacja
  // ------------------------------
  loadTimes();
  updateDisplay();
});
