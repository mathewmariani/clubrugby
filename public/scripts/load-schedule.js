function formatDateString(dateStr) {
  // Assumes DD/MM/YYYY input
  const [day, month, year] = dateStr.split('/');
  const date = new Date(`${year}-${month}-${day}`);
  return new Intl.DateTimeFormat('en-US', {
    weekday: 'long',
    month: 'long',
    day: 'numeric'
  }).format(date);
}

document.addEventListener("DOMContentLoaded", async () => {
  const [clubsRes, scheduleRes] = await Promise.all([
    fetch('/data/qc/2025/clubs.csv').then(res => res.text()),
    fetch('/data/qc/2025/schedule.csv').then(res => res.text())
  ]);

  const clubs = {};
  Papa.parse(clubsRes, {
    header: true,
    skipEmptyLines: true,
    complete: ({ data }) => {
      data.forEach(club => {
        clubs[club.id] = club.name;
      });

      // Now that clubs are loaded, parse the schedule
      Papa.parse(scheduleRes, {
        header: true,
        skipEmptyLines: true,
        complete: ({ data }) => {
          const container = document.getElementById('schedule-container');

          // Group matches by date
          const matchesByDate = {};
          data.forEach(match => {
            const date = match.date;
            if (!matchesByDate[date]) {
              matchesByDate[date] = [];
            }
            matchesByDate[date].push(match);
          });

          // Create a table for each date
          Object.entries(matchesByDate).forEach(([date, matches]) => {
            const section = document.createElement('section');
            section.className = 'mb-5';

            const heading = document.createElement('h2');
            heading.textContent = formatDateString(date);
            section.appendChild(heading);

            const table = document.createElement('table');
            table.className = 'table table-striped';

            table.innerHTML = `
              <thead>
                <tr>
                  <th>Time</th>
                  <th>Home Team</th>
                  <th>Away Team</th>
                  <th>Venue</th>
                </tr>
              </thead>
              <tbody>
                ${matches.map(match => `
                  <tr>
                    <td>${match.time}</td>
                    <td>${clubs[match.home_id] || match.home_id}</td>
                    <td>${clubs[match.away_id] || match.away_id}</td>
                    <td>${match.venue}</td>
                  </tr>
                `).join('')}
              </tbody>
            `;

            section.appendChild(table);
            container.appendChild(section);
          });
        }
      });
    }
  });
});
