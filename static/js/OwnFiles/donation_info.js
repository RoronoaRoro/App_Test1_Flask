function showImage() {
    let modal = document.getElementById("myModal");
    let modalImage = document.getElementById("modalImage");
    let caption = document.getElementById("caption");
    let image = document.getElementById("myImage");
    
    modal.style.display = "block";
    modalImage.src = image.src;
    caption.innerHTML = image.alt;
    
    let close = document.getElementsByClassName("close")[0];
    close.onclick = function() {
      modal.style.display = "none";
    }
}   

let button = document.getElementById('change-photo');
let image = document.getElementById('myImage');

// Get the list of phos from the attribute data of the button
let photos = button.getAttribute('data-photos').split(',');

// Actual index of the photo
let currentPhotoIndex = 0;

// Function to change the photo
function changePhoto() {
    // Increase the index
    currentPhotoIndex++;
    
    // Verify if the max size of the photo list has been reached
    if (currentPhotoIndex >= photos.length) {
        // Reset the index
        currentPhotoIndex = 0;
    }
    // Change the url of the image according to the actual index
    image.src = photos[currentPhotoIndex];
}

button.addEventListener('click', changePhoto);