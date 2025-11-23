console.log("script.js loaded");
const BASE_URL = "https://smart-drive-bucket-365649411877.asia-south1.run.app";

// ------------------ SIGNUP ------------------
async function signup() {
    alert("signup function running!");
    console.log("Signup clicked!");
    let email = document.getElementById("signupEmail").value;
    let password = document.getElementById("signupPassword").value;

    let res = await fetch(`${BASE_URL}/signup`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
    });

    let data = await res.json();
    alert(data.message);
}

// ------------------ LOGIN ------------------
async function login() {
    let email = document.getElementById("loginEmail").value;
    let password = document.getElementById("loginPassword").value;

    let res = await fetch(`${BASE_URL}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
    });

    let data = await res.json();

    if (data.token) {
        localStorage.setItem("token", data.token);
        window.location.href = "dashboard.html";
    } else {
        alert("Login failed");
    }
}

// ------------------ LOGOUT ------------------
function logout() {
    localStorage.removeItem("token");
    window.location.href = "index.html";
}

// ------------------ UPLOAD FILE ------------------
async function uploadFile() {

    let token = localStorage.getItem("token");
    if (!token) return window.location.href = "index.html";

    let fileInput = document.getElementById("fileInput");
    if (fileInput.files.length === 0) {
        return alert("Select a file!");
    }

    let form = new FormData();
    form.append("file", fileInput.files[0]);

    let res = await fetch(`${BASE_URL}/upload`, {
        method: "POST",
        headers: { "Authorization": "Bearer " + token },
        body: form
    });

    let data = await res.json();
    alert(data.message);
    fetchFiles();
}

// ------------------ FETCH FILES ------------------
async function fetchFiles() {
    let token = localStorage.getItem("token");

    let res = await fetch(`${BASE_URL}/files`, {
        headers: { "Authorization": "Bearer " + token }
    });

    let data = await res.json();

    let fileList = document.getElementById("fileList");
    fileList.innerHTML = "";

    data.files.forEach(file => {
        fileList.innerHTML += `
        <div class="file-item">
            <div>
                <strong>${file.file_name}</strong><br>
                <a href="${file.file_url}" target="_blank">Download</a>
            </div>
        </div>
        `;
    });
}

// ------------------ DELETE FILE ------------------
async function deleteFile(id) {

    let token = localStorage.getItem("token");

    let res = await fetch(`${BASE_URL}/delete/${id}`, {
        method: "DELETE",
        headers: { "Authorization": "Bearer " + token }
    });

    let data = await res.json();
    alert(data.message);

    fetchFiles();
}