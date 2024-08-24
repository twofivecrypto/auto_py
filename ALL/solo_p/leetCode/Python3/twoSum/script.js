document.addEventListener("DOMContentLoaded", function () {
    const saveButtons = document.querySelectorAll(".save-button");
    saveButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            const lesson = button.parentElement;
            const lessonText = lesson.querySelector("pre").innerText;
            saveLesson(lessonText);
        });
    });

    function saveLesson(lessonText) {
        // Your implementation to save the lesson goes here
        console.log("Lesson saved:", lessonText);
    }
});
