---
hide: navigation
---
# Welcome to our Blog
<div class="md-content" data-md-component="content">
  <div class="md-content__inner">
    <link rel="stylesheet" href="../stylesheets/extra.css">
    <div id="posts"></div>
    <script>
    // Function to convert Markdown to HTML
    function markdownToHtml(text) {
      // Convert bold text
      text = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
      // Convert italic text
      text = text.replace(/\*(.*?)\*/g, '<em>$1</em>');
      // Convert unordered lists
      text = text.replace(/\- (.*?)\./gm, '<li>$1.</li>');
      // Interpret blockquotes
      text = text.replace(/\> (.*?)\$/gm, '<blockquote>$1</blockquote>');
      // Convert \n to line break
      text = text.replace(/\\n/g, '<br>');
      // Interpret images
      text = text.replace(/!\[(.*?)\]\((.*?)\)/g, '<img src="$2" alt="$1">');
      // Convert links
      text = text.replace(/\[(.*?)\]\((.*?)\)(\{:target="_blank"\})?/g, function(match, p1, p2, p3) {
        return `<a href="${p2}"${p3 ? ' target="_blank"' : ''}>${p1}</a>`;
      });
    return text;
    }
    // Function to format the date in a more readable format
    function formatDate(dateString) {
      const months = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"];
        const [year, month, day] = dateString.split('-');
        return `${months[parseInt(month) - 1]} ${parseInt(day)}, ${year}`;
    }
    // Load the JSON file and display the posts
    fetch('./posts.json')
      .then(response => response.json())
      .then(data => {
        const postsContainer = document.getElementById('posts');
        if (data.posts && Array.isArray(data.posts)) {
          data.posts.forEach(post => {
            const postElement = document.createElement('div');
            postElement.innerHTML = `
              <em style="display: block; margin-bottom: 0;">${formatDate(post.date)}</em>
              <h2 style="margin-top: 0;"><a href="/blog/posts/${post.link}/">${post.title}</a></h2>
              ${markdownToHtml(post.summary)}
              <p><a href="/blog/posts/${post.link}/">Continue reading</a></p>
              <br>
            `;
            postsContainer.appendChild(postElement);
          });
        } else {
          console.error('No posts available.');
        }
      })
      .catch(error => console.error('Error loading JSON:', error));
    </script>
  </div>
</div>