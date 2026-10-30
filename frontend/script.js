// sends the url to the flask server and shows the answer
async function checkUrl() {
  const url = document.getElementById("url").value;
  const box = document.getElementById("result");
  box.style.display = "block";

  const res = await fetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url: url }),
  });
  const data = await res.json();

  if (data.error) {
    box.className = "bad";
    box.textContent = data.error;
    return;
  }

  box.className = data.label === "Suspicious" ? "bad" : "good";
  box.textContent = data.label + " (" + data.probability + "% chance of phishing)";

  // show the features the model looked at
  let rows = "<tr><th>Feature</th><th>Value</th></tr>";
  for (const key in data.features) {
    rows += "<tr><td>" + key + "</td><td>" + data.features[key] + "</td></tr>";
  }
  document.getElementById("features").innerHTML = rows;
}

// load the model results when the page opens
async function loadMetrics() {
  const res = await fetch("/metrics");
  const data = await res.json();

  let rows = "<tr><th>Model</th><th>Accuracy</th><th>Precision</th><th>Recall</th><th>F1</th></tr>";
  for (const name in data.results) {
    const r = data.results[name];
    rows += "<tr><td>" + name + "</td><td>" + r.accuracy + "</td><td>" + r.precision +
            "</td><td>" + r.recall + "</td><td>" + r.f1 + "</td></tr>";
  }
  const cm = data.confusion_matrix;
  rows += "<tr><td colspan='5'>Confusion matrix (Random Forest): " +
          "TN=" + cm[0][0] + ", FP=" + cm[0][1] + ", FN=" + cm[1][0] + ", TP=" + cm[1][1] + "</td></tr>";
  document.getElementById("metrics").innerHTML = rows;
}

loadMetrics();
