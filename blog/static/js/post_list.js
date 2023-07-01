const pageSize = 10;
let currentPage = $('#post-list .post').length >= pageSize ? 2 : 1;
let nextUrl = `/api/posts/?page=${currentPage}`;

function load_posts(url) {
    if (!url) {
        return;
    }
    $.ajax({
        url: url,
        dataType: 'json',
        success: function (data) {
            // Iterate over the posts
            console.log('Posts loaded:', data);

            if (data && data.results) {
                data.results.sort((a, b) => new Date(b.created_at) - new Date(a.created_at));

                data.results.forEach(post => {
                    let commentsHtml = '';
                    post.comments.sort((a, b) => new Date(b.created_at) - new Date(a.created_at)); // Sort comments by most recent

                    let displayedComments = 0; // Counter for displayed comments
                    post.comments.forEach(comment => {
            if (displayedComments < 12) { // Display only 3 comments
                        commentsHtml += `
                            <div class="comment">
                                <span class="comment-content">${comment.partial_content}</span>
                                <span class="comment-date">(Created at: ${comment.created_at})</span>
                            </div>
                        `;
                        displayedComments++;
                    }
                    });

                    const post_html = `
                        <div class="post">
                            <h2><b>Title</b> :${post.title}</h2>
                            <p><b>Author</b> :${post.author_nickname}</p>
                            <div class="comments" style="border: 1px solid black; max-height: 200px; overflow-y: auto;">
                            <h3>Comments</h3>
                                ${commentsHtml}
                            </div>
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


load_posts(nextUrl);