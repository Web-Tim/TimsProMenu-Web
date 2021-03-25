const carouselSlide = document.querySelector('.carousel-slide')
const carouselImages = document.querySelectorAll('.carousel-slide img')
const infoIP = document.querySelector('.info-ip')
const infoViews = document.querySelector('.info-views')
const infoDownloads_PyLib = document.querySelector('.download-count-pylib');
const infoDownloads_Menu = document.querySelector('.download-count-menu')

//Btns
const prevBtn = document.querySelector('#prevBtn')
const nextBtn = document.querySelector('#nextBtn')
const downloadMenu = document.querySelector('#download-menu')
const downloadPyLib = document.querySelector('#download-pylib')

//Main initialization
getIP()
updateVisitCount()
showMenuDownloadCount()
showPyLibDownloadCount()

//SourceCode
const imgSource = document.querySelector('.git img')
var githubURL = "https://github.com/Web-Tim"

//Counter
let counter = 1;
const size = carouselImages[0].clientWidth;

carouselSlide.style.transform = 'translateX(' + (-size * counter) + 'px)'

//Listeners
nextBtn.addEventListener('click', () => {
    if(counter >= carouselImages.length -1) return
    carouselSlide.style.transition = 'transform 0.4s ease-in-out'
    counter++
    carouselSlide.style.transform = 'translateX(' + (-size * counter) + 'px)'
})

prevBtn.addEventListener('click', () => {
    if(counter <= 0) return
    
    carouselSlide.style.transition = 'transform 0.4s ease-in-out'
    counter--
    carouselSlide.style.transform = 'translateX(' + (-size * counter) + 'px)'
})

carouselSlide.addEventListener('transitionend', () => {
    if(carouselImages[counter].id === 'lastClone') {
        carouselSlide.style.transition = 'none'
        counter = carouselImages.length - 2
        carouselSlide.style.transform = 'translateX(' + (-size * counter) + 'px)'
    }
    if(carouselImages[counter].id === 'firstClone') {
        carouselSlide.style.transition = 'none'
        counter = carouselImages.length - counter
        carouselSlide.style.transform = 'translateX(' + (-size * counter) + 'px)'
    }
})

downloadMenu.addEventListener('click', () => {
    updateMenuDownloadCount()
})

downloadPyLib.addEventListener('click', () => {
    updatePyLibDownloadCount()
})  

imgSource.addEventListener('click', () => {
    window.open(githubURL, "_blank");
})

//functions
function updateVisitCount() {
    fetch('https://api.countapi.xyz/update/timsweb/visits?amount=1')
    .then(res => res.json())
    .then(res => {
        infoViews.textContent = 'Total Views: ' + res.value
    })
}

function updateMenuDownloadCount() {
    fetch('https://api.countapi.xyz/update/timsweb/downloadsMenu?amount=1')
    .then(res => res.json())
    .then(res => {
        infoDownloads_Menu.innerHTML = 'Total Downloads: ' + res.value
    })
}

function updatePyLibDownloadCount() {
    fetch('https://api.countapi.xyz/update/timsweb/downloadsPyLib?amount=1')
    .then(res => res.json())
    .then(res => {
        infoDownloads_PyLib.innerHTML = 'Total Downloads: ' + res.value
    })
}

function showMenuDownloadCount() {
    fetch('https://api.countapi.xyz/get/timsweb/downloadsMenu')
    .then(res => res.json())
    .then(res => {
        infoDownloads_Menu.innerHTML = 'Total Downloads: ' + res.value
    })
}

function showPyLibDownloadCount() {
    fetch('https://api.countapi.xyz/get/timsweb/downloadsPyLib')
    .then(res => res.json())
    .then(res => {
        infoDownloads_PyLib.innerHTML = 'Total Downloads: ' + res.value
    })
}

function resetAllCounts() {
    fetch('https://api.countapi.xyz/set/timsweb/visits?value=0')
    .then(res => res.json())
    .then(res => {
        infoViews.innerHTML = 'Total Views: ' + res.value
    })

    fetch('https://api.countapi.xyz/set/timsweb/downloadsMenu?value=0')
    .then(res => res.json())
    .then(res => {
        infoDownloads_Menu.innerHTML = 'Total Downloads: ' + res.value
    })
    
    fetch('https://api.countapi.xyz/set/timsweb/downloadsPyLib?value=0')
    .then(res => res.json())
    .then(res => {
        infoDownloads_PyLib.innerHTML = 'Total Downloads: ' + res.value
    })
}

function getIP() {
    fetch('https://api.ipify.org/?format=json')
    .then(results => results.json())
    .then(data => infoIP.textContent = 'Logged in IP: ' + data.ip)
}