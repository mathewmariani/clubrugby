import Papa from 'papaparse';

export function parseCsv(text, rowTransform = (row) => row) {
  return new Promise((resolve, reject) => {
    Papa.parse(text, {
      header: true,
      skipEmptyLines: true,
      complete: ({ data }) => {
        resolve(data.map(rowTransform));
      },
      error: reject,
    });
  });
}

export function convertToISO(dateStr) {
  if (!dateStr) return '';
  const [day, month, year] = dateStr.split('/');
  if (!day || !month || !year) return '';
  return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`;
}
