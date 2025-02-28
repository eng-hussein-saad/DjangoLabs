// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
  // Handle loading transition
  const loadingOverlay = document.getElementById("loading-overlay");
  const content = document.querySelector(".content");

  // Simulate loading time (you can remove this setTimeout if you want it to load instantly)
  setTimeout(() => {
    // Hide loading overlay
    loadingOverlay.style.opacity = "0";
    loadingOverlay.style.visibility = "hidden";

    // Show content with fade in
    content.style.opacity = "1";

    // Add animation to the title
    const title = document.querySelector(".title");
    if (title) {
      title.style.opacity = "0";
      title.style.transform = "translateY(-20px)";
      setTimeout(() => {
        title.style.transition = "all 0.5s ease";
        title.style.opacity = "1";
        title.style.transform = "translateY(0)";
      }, 100);
    }
  }, 1500); // 1.5 seconds loading time

  // Add click animation to list items
  const listItems = document.querySelectorAll("li");
  listItems.forEach((item) => {
    item.addEventListener("click", function () {
      this.style.transition = "background-color 0.3s ease";
      this.style.backgroundColor = "#e8f4fc";
      setTimeout(() => {
        this.style.backgroundColor = "#fff";
      }, 300);
    });
  });
});
