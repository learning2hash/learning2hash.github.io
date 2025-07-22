---
layout: page
title: Contributing
description: How to contribute to this website.
---

### Adding a publication

Contributions of new or missing publications are very welcome. To contribute, simply fill in the form below and your paper will appear in front of **thousands** of researchers in the field:

<form id="contribution-form" class="contribution-form">
  <input type="email" name="email" class="contribution-input" placeholder="Your Email Address" required><br><br>
  <input type="text" name="title" class="contribution-input" placeholder="Paper Title" required><br><br>
  <input type="text" name="authors" class="contribution-input" placeholder="Paper Authors" required><br><br>
  <input type="text" name="conference" class="contribution-input" placeholder="Conference Name" required><br><br>
  <input type="text" name="date" class="contribution-input" placeholder="Year" required><br><br>
  <input type="url" name="paper" class="contribution-input" placeholder="Link to paper PDF" required><br><br>
  <input type="url" name="code" class="contribution-input" placeholder="Link to code (e.g. GitHub)" required><br><br>
  <textarea name="abstract" class="contribution-textarea" placeholder="Paper Abstract" required></textarea><br><br>
  <button type="submit" class="contribution-button">Submit</button>
  <p id="contribution-message" style="margin-top: 20px; font-weight: bold;"></p>
</form>

<style>
  .contribution-form {
    width: 90%;
    margin: auto;
    max-width: 700px;
  }

  .contribution-input {
    width: 100%;
    font-weight: bold;
    border: 2px solid #000;
    padding: 10px;
    box-sizing: border-box;
  }

  .contribution-textarea {
    width: 100%;
    height: 300px;
    font-weight: bold;
    border: 2px solid #000;
    padding: 10px;
    box-sizing: border-box;
  }

  .contribution-button {
    font-weight: bold;
    color: black;
    border: 2px solid #000;
    padding: 10px 20px;
    background-color: #f5f5f5;
    cursor: pointer;
  }

  @media (max-width: 768px) {
    .contribution-input, .contribution-textarea, .contribution-button {
      width: 100%;
      max-width: none;
    }
  }
</style>

<script>
document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("contribution-form");
  const message = document.getElementById("contribution-message");

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const formData = new FormData(form);
    const payload = new URLSearchParams();

    for (const pair of formData.entries()) {
      payload.append(pair[0], pair[1]);
    }

    fetch("https://awesome-llm-papers.tinyapps.run/contribute", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: payload
    })
    .then(response => response.json())
    .then(data => {
      if (data.status === "success") {
        message.textContent = "✅ Submission successful!";
        message.style.color = "green";
        form.reset();
      } else {
        message.textContent = "⚠️ " + (data.error || "Submission failed.");
        message.style.color = "red";
      }
    })
    .catch(error => {
      console.error("Error submitting contribution:", error);
      message.textContent = "❌ Something went wrong. Please try again.";
      message.style.color = "red";
    });
  });
});
</script>
