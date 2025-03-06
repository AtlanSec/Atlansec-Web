---
hide:
  - navigation
---
# Bienvenido a nuestro Blog
<div class="md-content" data-md-component="content">
  <div class="md-content__inner">
    <link rel="stylesheet" href="../stylesheets/extra.css">
    <div id="posts"></div>
    <script>
    // Función para convertir Markdown a HTML
    function markdownToHtml(text) {
      // Convierte listas no ordenadas
      text = text.replace(/\- (.*?)\./gm, '<li>$1.</li>');
      // Convertir negrita
      text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
      // Convertir cursiva
      text = text.replace(/\*(.*?)\*/g, '<em>$1</em>');
      text = text.replace(/\_(.*?)\_/g, '<em>$1</em>');
      // Convertir \n en salto de linea
      text = text.replace(/\\n/g, '<br>');
      // Interpretar imágenes
      text = text.replace(/!\[(.*?)\]\((.*?)\)/g, '<img src="$2" alt="$1">');
      // Convertir enlaces
      text = text.replace(/\[(.*?)\]\((.*?)\)(\{:target="_blank"\})?/g, function(match, p1, p2, p3) {
        return `<a href="${p2}"${p3 ? ' target="_blank"' : ''}>${p1}</a>`;
      });
      return text;
      }
    // Cargar el archivo JSON y mostrar los posts
    fetch('./posts.json')
      .then(response => response.json())
      .then(data => {
        const postsContainer = document.getElementById('posts');
        if (data.posts && Array.isArray(data.posts)) {
          data.posts.forEach(post => {
            const postElement = document.createElement('div');
            postElement.innerHTML = `
              <em style="display: block; margin-bottom: 0;">${post.date}</em>
              <h2 style="margin-top: 0;"><a href="/es/blog/posts/${post.link}/">${post.title}</a></h2>
              <p>${markdownToHtml(post.summary)}</p>
              <p><a href="/es/blog/posts/${post.link}/">Continue leyendo</a></p>
              <br>
            `;
            postsContainer.appendChild(postElement);
          });
        } else {
          console.error('No posts available.');
        }
      })
      .catch(error => console.error('Error al cargar el JSON:', error));
    </script>
  </div>
</div>
