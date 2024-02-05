function togglePopup(popupId) {
	var popup = document.getElementById(popupId);
	popup.classList.toggle("hidden");
}

function addPhoneField() {
	var addButton = document.getElementById("add-phone-button");

	var phoneContainer = document.getElementById("phone-container");
	var fieldWrapper = document.createElement("div");
	fieldWrapper.className = "phone-field mt-2";

	var newField = document.createElement("input");
	newField.setAttribute("type", "text");
	newField.setAttribute("name", "phone[]");
	newField.setAttribute(
		"class",
		"p-2 bg-white rounded border border-gray-400 mr-2"
	);

	var deleteButton = document.createElement("button");
	deleteButton.innerText = "Supprimer";
	deleteButton.setAttribute("type", "button");
	deleteButton.setAttribute("onclick", "deleteField(this)");
	deleteButton.setAttribute(
		"class",
		"py-2 px-4 bg-red-500 text-white rounded hover:bg-red-700"
	);

	fieldWrapper.appendChild(newField);
	fieldWrapper.appendChild(deleteButton);
	phoneContainer.appendChild(fieldWrapper);
}

function deleteField(button) {
	button.parentElement.remove();
}
