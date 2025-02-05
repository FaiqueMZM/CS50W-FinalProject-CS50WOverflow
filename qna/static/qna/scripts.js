document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.vote-btn').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const url = this.href;

            fetch(url, {
                method: 'GET',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Find the closest card-body element
                    const cardBody = this.closest('.card-body');

                    // Find the upvotes and downvotes count elements within the card-body
                    const upvotesElement = cardBody.querySelector('.upvotes');
                    const downvotesElement = cardBody.querySelector('.downvotes');

                    // Update the vote counts in the UI
                    upvotesElement.textContent = `Upvotes: ${data.upvotes}`;
                    downvotesElement.textContent = `Downvotes: ${data.downvotes}`;
                }
            });
        });
    });
});