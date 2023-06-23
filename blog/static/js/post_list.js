const pageSize = 10;
let currentPage = $('#post-list .post').length >= pageSize ? 2 : 1;
let nextUrl = `/api/posts/?page=${currentPage}`;

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
            console.log('Posts loaded:', data);

            if (data && data.results) {
                data.results.forEach(post => {
                    const post_html = `
                        <div class="post">
                            <h2>${post.title}</h2>
                            <p>Author: ${post.author}</p>
                            <p>${post.content}</p>
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

$('#load-more-button').click(function () {
    console.log('button trigger');
    load_posts(nextUrl);
});
