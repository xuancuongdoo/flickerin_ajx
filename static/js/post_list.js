function load_posts(url) {
    console.log('Loading posts from', url);

    if (!url) {
        console.log('No more posts to load');
        return;
    }

    $.ajax({
        url: url,
        dataType: 'json',
        success: function (data) {
            console.log('Posts22321312 loaded:', data);
            console.log('Posts312312321 loaded:', data); 
            if (data && data.results) {
                data.results.forEach(post => {
                    let comments_html = '';
                    post.comments.forEach(comment => {
                        comments_html += `<p>${comment.partial_content}</p>`;
                        console.log(comments_html)
                    });

                    const post_html = `
                        <div class="post">
                            <h2>${post.title}</h2>
                            <p>Author: ${post.author_nickname}</p>
                            <p>${post.content}</p>
                          <p>${comments_html}
                        </p>
                        </div>  
                    `;

                    $('#post-list').append(post_html);
                });

                nextUrl = data.next;

                if (data.next) {
                    $('#load-more-button').appendTo('#post-list').show();
                } else {
                    $('#load-more-button').hide();
                }
                
            } else {
                console.error('Invalid response data:', data);
            }
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.error('AJAX request failed:', textStatus, errorThrown);
        }
    });
}