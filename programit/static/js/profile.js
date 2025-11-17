document.addEventListener("DOMContentLoaded", () => {
  const editBtn = document.getElementById("edit-toggle");
  const form = document.getElementById("edit-form");

  editBtn.addEventListener("click", () => {
    form.classList.toggle("hidden");
    editBtn.textContent = form.classList.contains("hidden")
      ? "Edit"
      : "Cancel";
  });
});
document.addEventListener("DOMContentLoaded", () => {
    const terminal = document.querySelector(".terminal");

    const commands = {
        help: [
            "Available commands:",
            " help .............. show this help",
            " about ............. info about the user",
            " github ............ GitHub profile link",
            " score ............. show user score",
            " projects .......... list of projects",
            " clear ............. clear terminal",
        ].join("\n"),

        about: `User: {{ profile.username }}\nDescription: {{ profile.description }}`,
        github: `GitHub: https://github.com/{{ profile.github_username }}`,
        score: `Your score: {{ profile.points }}`,
        projects: "User projects:\n - programIT-app\n - AI-engine\n - portfolio-site\n - dev-tools",
        clear: "!!clear!!"
    };

    let input = "";
    let currentPromptLine = null;

    // === AUTO SCROLL ===
    function autoScroll() {
        terminal.scrollTop = terminal.scrollHeight;
    }
    document.addEventListener("keydown", function (e) {
    const isBackspace = e.key === "Backspace";

    // If terminal is active, prevent browser navigation
    if (isBackspace) {
        e.preventDefault(); 
    }
    });
    // === CREATE PROMPT ===
    function createPrompt() {
        const line = document.createElement("div");
        line.classList.add("terminal-line");

        line.innerHTML =
            `<span class="user">programit@{{ profile.username }}</span>:~$ ` +
            `<span class="typed"></span><span class="cursor-block"></span>`;

        terminal.appendChild(line);
        currentPromptLine = line;
        autoScroll();
    }

    // === OUTPUT ===
    function printLine(text) {
        const line = document.createElement("div");
        line.classList.add("terminal-line", "text-[#abb2bf]");
        line.textContent = text;
        terminal.appendChild(line);
        autoScroll();
    }

    // === EXECUTE ===
    function execute(inputText) {
        const typedSpan = currentPromptLine.querySelector(".typed");
        const cursor = currentPromptLine.querySelector(".cursor-block");
        cursor.remove();

        typedSpan.textContent = inputText;

        if (commands[inputText]) {
            if (commands[inputText] === "!!clear!!") {
                terminal.innerHTML = "";
                input = "";
                createPrompt();
                return;
            }

            commands[inputText].split("\n").forEach(line => printLine(line));
        } else {
            printLine("Unknown command: " + inputText);
        }

        input = "";
        createPrompt();
    }

    // === INPUT HANDLING ===
    document.addEventListener("keydown", (event) => {
        if (!currentPromptLine) return;

        const typedSpan = currentPromptLine.querySelector(".typed");

        if (event.key === "Enter") {
            execute(input);
            return;
        }

        if (event.key === "Backspace") {
            input = input.slice(0, -1);
            typedSpan.textContent = input;
            return;
        }

        if (event.key.length === 1) {
            input += event.key;
            typedSpan.textContent = input;
        }
    });

    // === CURSOR STYLE ===
    const style = document.createElement("style");
    style.innerHTML = `
        .cursor-block {
            display: inline-block;
            width: 0.6ch;
            height: 1em;
            background-color: #98c379;
            margin-left: 2px;
            transform: translateY(2px);
            animation: blinkCursor 0.9s steps(1) infinite;
        }
        @keyframes blinkCursor {
            50% { opacity: 0; }
        }
    `;
    document.head.appendChild(style);

    // === INITIAL LOAD ===
    createPrompt();
    commands["help"].split("\n").forEach(line => printLine(line));
});