let rows = document.querySelectorAll('tr[data-id]');
rows.forEach(row => {
  row.addEventListener('click', () => {
    let id = row.dataset.id;
    window.location.href = `donation-info?id=${id}`;
  });
});