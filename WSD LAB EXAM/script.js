const fetchDogBtn = document.getElementById("fetchDogBtn");
const dogImage = document.getElementById("dogImage");

async function fetchRandomDogImage() {
    try {
        const response = await fetch("https://dog.ceo/api/breeds/image/random");
        if (!response.ok) {
            throw new Error("Failed to fetch dog image");
        }
        const imageData = await response.json();
        dogImage.src = imageData.message;
    } catch (error) {
        console.error(error);
        dogImage.src = "error.png";
    }
}
fetchDogBtn.addEventListener("click", fetchRandomDogImage);
fetchRandomDogImage();
