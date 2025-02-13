document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-menu a');
    const contentItems = document.querySelectorAll('.content-item');

    
    showContent('books');

    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            navLinks.forEach(link => link.classList.remove('active'));
            
            this.classList.add('active');
            
            const category = this.getAttribute('href').substring(1);
            
            showContent(category);
        });
    });

    function showContent(category) {
        
        contentItems.forEach(item => {
            item.classList.remove('active');
        });

        const selectedItems = document.querySelectorAll(`.${category}`);
        selectedItems.forEach(item => {
            item.classList.add('active');
        });
    }
});
