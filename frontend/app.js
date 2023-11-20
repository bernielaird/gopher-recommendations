// main.js

// Function to fetch and populate classes from JSON file
function populateClasses() {
    var classListContainer = document.getElementById("classList");

    // Fetch the JSON data from classes.json
    fetch('classes.json')
        .then(response => response.json())
        .then(data => {
            // Iterate through the classes data and create HTML elements
            data.classes.forEach(function (classItem) {
                var classElement = document.createElement("div");
                classElement.classList.add("class-item");

                classElement.innerHTML = `
                    <h2>${classItem.name}</h2>
                    <p><strong>Professor:</strong> ${classItem.professor}</p>
                    <p><strong>Description:</strong> ${classItem.description}</p>
                    <p><strong>Schedule:</strong> ${classItem.schedule.day} at ${classItem.schedule.time}</p>
                    <hr>
                `;

                classListContainer.appendChild(classElement);
            });
        })
        .catch(error => console.error('Error fetching JSON:', error));
}

// Call the function to populate the classes on page load
populateClasses();
