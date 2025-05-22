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
    fetch('/data/qc/2025/results.csv').then(res => res.text())
  ]);

  const clubs = {};
  Papa.parse(clubsRes, {
    header: true,
    skipEmptyLines: true,
    complete: ({ data }) => {
      data.forEach(club => {
        clubs[club.id] = {name: club.name, logo: club.logo_url};
      });

      console.log(clubs)

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
                  <th>Match</th>
                </tr>
              </thead>
              <tbody>
              ${matches.map(match => {
                const homeName = clubs[match.home_id].name || match.home_id;
                const awayName = clubs[match.away_id].name || match.away_id;
                const homeLogo = clubs[match.home_id].logo || '';
                const awayLogo = clubs[match.away_id].logo || '';
                const homeScore = parseInt(match.home_score, 10);
                const awayScore = parseInt(match.away_score, 10);
              
                // Determine score classes
                let homeClass = '', awayClass = '';
                if (!isNaN(homeScore) && !isNaN(awayScore)) {
                  if (homeScore > awayScore) {
                    homeClass = 'text-success';
                    awayClass = 'text-danger';
                  } else if (homeScore < awayScore) {
                    homeClass = 'text-danger';
                    awayClass = 'text-success';
                  }
                }
              
                return `
                  <tr>
                    <td>${match.time}</td>
                    <td>
        <div class="d-flex justify-content-between align-items-center">
          <div class="d-flex align-items-center">
            <img src="${homeLogo}" alt="${homeName}" width="32" height="32" class="me-2">
            <span>${homeName}</span>
          </div>
          <strong class="${homeClass}">${match.home_score || ''}</strong>
        </div>
        <div class="d-flex justify-content-between align-items-center mt-1">
          <div class="d-flex align-items-center">
            <img src="${awayLogo}" alt="${awayName}" width="32" height="32" class="me-2">
            <span>${awayName}</span>
          </div>
          <strong class="${awayClass}">${match.away_score || ''}</strong>
        </div>
      </td>
                  </tr>
                `;
              }).join('')}
              
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
