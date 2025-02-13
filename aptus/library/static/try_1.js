function searchSection() {
    const searchBar = document.getElementById('search-bar');
    const filter = searchBar.value.toLowerCase();
    const list = document.getElementById('sections-list');
    const sections = list.getElementsByTagName('li');
  
    for (let i = 0; i < sections.length; i++) {
      const text = sections[i].innerText.toLowerCase();
      if (text.includes(filter)) {
        sections[i].classList.remove('hidden');
      } else {
        sections[i].classList.add('hidden');
      }
    }
  }
  