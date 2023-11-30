// Add even listener on multiple elements
const addEventOnElements = function (elements, eventType, callback) {
	for (let i = 0, len = elements.length; i < len; i++) {
		elements[i].addEventListener(eventType, callback);
	}
};

// Navbar Toggle
const navTogglers = document.querySelectorAll("[data-nav-toggler]");
const navToggleBtn = document.querySelector("[data-nav-toggle-btn]");
const navbar = document.querySelector("[data-navbar]");
const overlay = document.querySelector("[data-overlay]");

const toggleNavbar = function () {
	navbar.classList.toggle("active");
	navToggleBtn.classList.toggle("active");
	overlay.classList.toggle("active");
	document.body.classList.toggle("nav-active");
};

addEventOnElements(navTogglers, "click", toggleNavbar);

// Swiper
var swiper = new Swiper(".mySwiper", {
	spaceBetween: 30,
	loop: true,
	autoplay: {
		delay: 2500,
		disableOnInteraction: false,
	},
	pagination: {
		el: ".swiper-pagination",
		clickable: true,
	},
	navigation: {
		nextEl: ".swiper-button-next",
		prevEl: ".swiper-button-prev",
	},
});

// Popup
// document.addEventListener("click", (e) => {
// 	if (e.target.classList.contains("dl-docs")) {
// 		togglePortfolioPopup();

// 		portfolioItemDetails(e.target.parentElement);
// 		// console.log(e.target.parentElement);
// 	}
// });

// function togglePortfolioPopup() {
// 	document.querySelector(".preview_popup").classList.toggle("open");
// }

// document.querySelector(".preview_popup-close").addEventListener("click", togglePortfolioPopup);

// function portfolioItemDetails(portfolioItem) {
// 	document.querySelector(".preview_popup-body").innerHTML = portfolioItem.querySelector(".preview_item-details").innerHTML;
// }
