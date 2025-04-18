document.addEventListener("DOMContentLoaded", function() {
  var currentLanguage = document.documentElement.lang; //idioma actual 
  
  var observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
      if (mutation.type === "childList") {
        var searchResults = document.querySelectorAll('.md-search-result__item');
        searchResults.forEach(function(item) {
          var link = item.querySelector('a').href;
          if (currentLanguage === "en") {
            // Para inglés, oculta los resultados en español
            if (link.includes('/es/')) {
              item.style.display = 'none';
            }
          } else if (currentLanguage === "es") {
            // Para español, oculta los resultados en inglés
            if (!link.includes('/es/')) {
              item.style.display = 'none';
            }
          }
          else if (currentLanguage != "es" || currentLanguage != "en") {
            return ;
          }
        });
      }
    });
  });

  var config = { childList: true, subtree: true };
  observer.observe(document.body, config);
});
