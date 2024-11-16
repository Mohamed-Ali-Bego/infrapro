let SearchToggle = document.querySelector(".search-btn");
let SearchBtns = document.querySelector(".search-btns");
// let togglerBtn = document.querySelector(".toggle-btn");
// let togglelist = document.querySelector(".toggle-list");
// let toggleX = document.querySelector(".toggle-x");
let toggleXs = document.querySelector(".toggle-xs");


// togglerBtn.addEventListener('click',()=>{
// togglerBtn.classList.remove('open')
// toggleX.classList.add('open')
// togglelist.classList.add('open')
// })
// toggleX.addEventListener('click',()=>{
// togglerBtn.classList.add('open')
// toggleX.classList.remove('open')
// togglelist.classList.remove('open')
// })

SearchToggle.addEventListener('click',()=>{
SearchToggle.classList.add('close')
SearchBtns.classList.add('open')
toggleXs.classList.remove('close')
})
toggleXs.addEventListener('click',()=>{
SearchToggle.classList.remove('close')
SearchBtns.classList.remove('open')
toggleXs.classList.add('close')
})





$('.owl-carousel').owlCarousel({
    center: true,
    items:2,
    loop:true,
    margin:30,
    responsive: {
        0:{
            items: 2,
        },
        768:{
            items: 3,
        },
        1100:{
            items: 4,
        },
        1400:{
            items: 4,
            loop: false,
        }
    }
});






$(document).ready(function () {
    $('.nav-toggle').click(function () {
        var collapse_content_selector = $(this).attr('href');
        var toggle_switch = $(this);
        $(collapse_content_selector).toggle(function () {
            if ($(this).css('display') == 'none') {
                toggle_switch.html('Read More');
            } else {
                toggle_switch.html('Read Less');
            }
        });
    });
    

});


