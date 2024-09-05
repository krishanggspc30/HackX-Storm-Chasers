function showCard() {
    const dropdown = document.getElementById('region-dropdown');
    const selectedRegion = dropdown.value;
    const card = document.getElementById('action-card');
    const regionTitle = document.getElementById('region-title');
  
    if (selectedRegion) {
      regionTitle.textContent = `Selected Region: ${selectedRegion}`;
      card.classList.remove('hidden');
    }
  }
  
  function submitForm(event) {
    event.preventDefault();
  
    const region = document.getElementById('region-dropdown').value;
    const time = document.getElementById('time').value;
  
    // Store the selected region and time in localStorage (to pass data to the next page)
    localStorage.setItem('region', region);
    localStorage.setItem('time', time);
  
    // Redirect to the admin page
    window.location.href = 'admin.html';
  }
  