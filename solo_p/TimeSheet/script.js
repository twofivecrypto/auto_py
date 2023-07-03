document.getElementById("submit-btn").addEventListener("click", function() {
    var date = document.getElementById("date").value;
    var startTime = document.getElementById("start-time").value;
    var endTime = document.getElementById("end-time").value;
  
    var totalHours = calculateTotalHours(startTime, endTime);
    document.getElementById("total").textContent = totalHours.toFixed(2);
  });
  
  document.addEventListener("DOMContentLoaded", function() {
    flatpickr(".time-input", {
      enableTime: true,
      noCalendar: true,
      dateFormat: "H:i",
      time_24hr: true,
    });
  });
  
  function calculateTotalHours(startTime, endTime) {
    var start = new Date("2000-01-01 " + startTime);
    var end = new Date("2000-01-01 " + endTime);
  
    var totalMilliseconds = end - start;
    var totalHours = totalMilliseconds / 1000 / 60 / 60;
  
    return totalHours;
  }
  