// document.addEventListener('DOMContentLoaded', function () {
//     let currentSlideIndex = 0;
//     let slides = document.querySelectorAll('.slider');
//     let prevArrow = document.querySelector('.left');
//     let nextArrow = document.querySelector('.right');
//     let slideInterval;
//
//     function showSlide(index) {
//         slides.forEach((slide, i) => {
//             slide.classList.remove('active', 'prev', 'next');
//
//             if (i === index) {
//                 slide.classList.add('active');
//             } else if (i < index) {
//                 slide.classList.add('prev');
//             } else {
//                 slide.classList.add('next');
//             }
//         });
//     }
//
//     function startSlideShow() {
//         slideInterval = setInterval(() => {
//             currentSlideIndex = (currentSlideIndex + 1) % slides.length;
//             showSlide(currentSlideIndex);
//         }, 1222000);
//     }
//
//     function resetSlideInterval() {
//         clearInterval(slideInterval);
//         startSlideShow();
//     }
//
//     prevArrow.addEventListener('click', function() {
//         currentSlideIndex = (currentSlideIndex - 1 + slides.length) % slides.length;
//         showSlide(currentSlideIndex);
//         resetSlideInterval();
//     });
//
//     nextArrow.addEventListener('click', function() {
//         currentSlideIndex = (currentSlideIndex + 1) % slides.length;
//         showSlide(currentSlideIndex);
//         resetSlideInterval();
//     });
//
//     startSlideShow();
// });


let isAnimating = false;

document.getElementById('drop-show-lang').addEventListener('click', function(event) {
    event.preventDefault();

    if (isAnimating) return;

    let langsList = document.getElementById('langs-list-id');

    $(this).find(".fa-chevron-down, .fa-chevron-up").toggleClass("fa-chevron-down fa-chevron-up");

    if (langsList.classList.contains('active')) {
        langsList.classList.remove('active');
        langsList.classList.add('closing');
        isAnimating = true;

        setTimeout(() => {
            langsList.classList.remove('closing');
            langsList.style.visibility = 'hidden';
            langsList.style.pointerEvents = 'none';
            isAnimating = false;
        }, 600);
    } else {
        langsList.style.visibility = 'visible';
        langsList.style.pointerEvents = 'auto';
        isAnimating = true;

        setTimeout(() => {
            langsList.classList.add('active');
            isAnimating = false;
        }, 10);
    }
});

