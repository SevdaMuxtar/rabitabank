var searchIcon = document.getElementById("search-input")
var menu = document.getElementById("menus")
var layer = document.getElementById("layer")
var checkboxSliderInput = document.getElementById("checkbox")
var chekcboxSliderLabel = document.querySelectorAll(".cs-label")
var cash = document.getElementById("cash")
var cashless = document.getElementById("cashless")

function hideSearchInput() {
    searchIcon.classList.toggle("hide")
  }


function showMenu() {
  menu.classList.toggle("hide")
  layer.classList.toggle("hide")
}

layer.addEventListener("click", () => {
  menu.classList.toggle("hide")
  layer.classList.toggle("hide")
})

$(document).ready(function(){
  $('.sliders').slick({
    autoplay: true,
    autoplaySpeed: 3000,
    dots: true
  });
});

function checkboxSlider() {
  chekcboxSliderLabel.forEach(element => {
    element.classList.remove("active")
  });
  if(checkboxSliderInput.checked === false) {
    cashless.classList.add("active")
  }else {
    cash.classList.add("active")
  }
}