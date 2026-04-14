document.addEventListener("DOMContentLoaded", function () {

    /* ===============================
       Risk Probability Chart
       =============================== */
    const riskCanvas = document.getElementById("riskChart");
    if (riskCanvas) {
        const riskValue = parseFloat(riskCanvas.dataset.risk);

        new Chart(riskCanvas, {
            type: "bar",
            data: {
                labels: ["Heart Disease Risk"],
                datasets: [{
                    label: "Risk Probability (%)",
                    data: [riskValue],
                    backgroundColor: riskValue < 35
                        ? "#198754"     // green
                        : riskValue < 65
                        ? "#ffc107"     // orange
                        : "#dc3545"     // red
                }]
            },
            options: {
                indexAxis: "y",
                scales: {
                    x: {
                        min: 0,
                        max: 100,
                        ticks: {
                            callback: value => value + "%"
                        }
                    }
                },
                plugins: {
                    legend: { display: false }
                }
            }
        });
    }

    /* ===============================
       Top Risk Factors Chart
       =============================== */
    const factorCanvas = document.getElementById("factorChart");
    if (factorCanvas) {
        const labels = JSON.parse(factorCanvas.dataset.labels);
        const values = JSON.parse(factorCanvas.dataset.values);

        new Chart(factorCanvas, {
            type: "bar",
            data: {
                labels: labels,
                datasets: [{
                    label: "Impact Score",
                    data: values,
                    backgroundColor: "#0d6efd"
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                },
                plugins: {
                    legend: { display: false }
                }
            }
        });
    }

});
