async function submitReview() {
    const rating = document.querySelector('input[name="rating"]:checked')
    const opinion = document.getElementById('opinion').value
    console.log(rating)
    console.log(opinion)
    if (!rating || !opinion.trim()) {
        alert('평점 또는 후기 내용이 입력되지 않았습니다.')
        return;
    }

    const review = {
        rating: parseInt(rating.value),
        opinion //객체 리터럴에서 key와 변수명이 같을 경우 축약해서 opinion만 써도 opinion: opinion과 동일하게 작동
    }
    

    const response = await fetch('/api/reviews', {
        method: 'POST',
        headers: {'content-type': 'application/json'},
        body: JSON.stringify(review)
    })
    const data = await response.json()
    
    fetchReviews();
    fetchAISummary();

    
}

async function fetchReviews() {
    // try catch
    const response = await fetch('/api/reviews');
    if (!response.ok) {
        throw new Error('요청 올')
    }

    const data = await response.json()

    displayReviews(data)
}


function displayReviews(data) {
    const reviewsContainer = document.getElementById('reviews-container')
    const reviewboxes = document.querySelectorAll('.review-box')
    reviewboxes.forEach(box => box.remove())

    
    for (const review of data) {
        console.log(review)
        const reviewbox = document.createElement('div')
        reviewbox.classList.add('review-box')
        reviewbox.innerHTML = `<p><strong>평점: ${review.rating}</strong></p><p>${review.opinion}</p>`
        reviewsContainer.appendChild(reviewbox)
    }
    
}



async function fetchAISummary() {
    const lang = document.getElementById('languageSelect').value;

    const response = await fetch(`/api/ai-summary?lang=${lang}`)
    const data = await response.json()
    console.log(data)
    displayAISummary(data)
}

async function displayAISummary(data) {
    
    const summarybox = document.getElementById('ai-summary')
    summarybox.innerHTML = `<p><strong>AI요약: </strong> ${data.contents}</p>
                            <p><strong>평균 별점:</strong> ${data.averagerating}</p>`
}   



window.onload = async () => {
    await fetchReviews()
}