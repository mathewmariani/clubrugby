document.addEventListener("DOMContentLoaded", () => {
    fetch('/data/qc/2025/clubs.csv')
      .then(res => res.text())
      .then(text => {
        Papa.parse(text, {
          header: true,
          skipEmptyLines: true,
          complete: function(results) {
            const container = document.getElementById("clubs-list");
            results.data.forEach(club => {
              const card = document.createElement("div");
              card.className = "col";
  
              card.innerHTML = `
                <div class="card d-flex flex-row align-items-center p-2">
                  <img src="${club.logo_url}" alt="${club.name}" class="me-3" style="width: 64px; height: 64px; object-fit: contain;">
                  <div class="card-body p-0">
                    <h5 class="card-title mb-0">${club.name}</h5>
                    <a href="schedule.html?id=${club.id}">Schedule</a><br />
                    <a href="dashboard.html?id=${club.id}">Dashboard</a>
                  </div>
                </div>
              `;
  
              container.appendChild(card);
            });
          }
        });
      });
  });
  