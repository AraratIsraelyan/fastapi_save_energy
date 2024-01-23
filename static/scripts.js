function self_devices_Input() {
    var selectElement = document.getElementById("self_service_devices");
    var inputElement = document.getElementById("self_service_devices_count");

    // Если выбрано "Есть" (значение 1), показываем поле ввода, в противном случае скрываем
    inputElement.style.display = (selectElement.value === "1") ? "block" : "none";
}