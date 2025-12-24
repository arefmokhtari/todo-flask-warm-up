
const terminal = document.getElementById("terminal");
const input = document.getElementById("commandInput");
const runBtn = document.getElementById("runBtn");
const leaveBtn = document.getElementById("leaveBtn");

function printLine(text, cls="line", tag='div') {
    const line = document.createElement(tag);
    line.className = cls;
    line.textContent = text;
    terminal.appendChild(line);
    terminal.scrollTop = terminal.scrollHeight;
}

async function executeCommand() {
    const cmd = input.value.trim();
    if (!cmd) return;
    const res = await fetch("/runner", {
        method: 'POST',
        body: JSON.stringify({ cmd, }),
    });
    if(!res.ok)
        printLine("server error!", "output");
    else if (['cls', 'clear'].includes(cmd)) 
        terminal.innerHTML = "";
    else {
        const data = await res.json();
        printLine("aref@ubuntu:~$ " + cmd, "line");
        printLine(data.data, "output", 'pre');
    }

    input.value = "";
}

input.addEventListener("keydown", function(e) {
    if (e.key === "Enter") {
    executeCommand();
    }
});

runBtn.addEventListener("click", executeCommand);

leaveBtn.addEventListener("click", async () => {
    const res = await fetch("/leave-master", { method: "POST" });
    if(res.ok)
    window.location.href = '/login';
});