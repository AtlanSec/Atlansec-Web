---
hide: navigation
---
# Welcome to our Blog
  <div class="md-content" data-md-component="content">
    <div class="md-content__inner">
      <link rel="stylesheet" href="../stylesheets/extra.css">
      <div id="posts"></div>
      <script>
  // Cargar el archivo JSON y mostrar los posts
  fetch('./postsEn.json')
    .then(response => response.json())
    .then(data => {
      const postsContainer = document.getElementById('posts');
      if (data.posts && Array.isArray(data.posts)) {
        data.posts.forEach(post => {
          const postElement = document.createElement('div');
          postElement.innerHTML = `
            <em style="display: block; margin-bottom: 0;">${post.date}</em>
            <h2 style="margin-top: 0;"><a href="/blog/posts/${post.link}/">${post.title}</a></h2>
            <p>${post.description}</p>
            <p><a href="/blog/posts/${post.link}/">Continue reading</a></p>
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
