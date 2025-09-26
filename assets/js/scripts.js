// Tab switching
const tabs = document.querySelectorAll('.tab-link');
const pages = document.querySelectorAll('.page');

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    const target = tab.dataset.tab;
    pages.forEach(p => p.classList.remove('active'));
    document.getElementById(target).classList.add('active');

    tabs.forEach(t => t.classList.remove('active'));
    tab.classList.add('active');
  });
});

// Recommendation form
function getRecommendation() {
  const category = document.getElementById('category').value;
  const product = document.getElementById('productInput').value;
  const results = document.getElementById('rec-results');
  results.innerHTML = `<p>🔎 Showing recommendations for <b>${product || category}</b></p>`;
  return false;
}

// Contact form
function submitForm(event) {
  event.preventDefault();
  alert("✅ Thank you! Your message has been sent.");
  return false;
}

// Lottie Animations
lottie.loadAnimation({
  container: document.getElementById('shoppingAnim'),
  renderer: 'svg',
  loop: true,
  autoplay: true,
  path: 'assets/animations/shopping.json'
});

lottie.loadAnimation({
  container: document.getElementById('contactAnim'),
  renderer: 'svg',
  loop: true,
  autoplay: true,
  path: 'assets/animations/contact.json'
});

// Function to show tab programmatically
function showTab(tabName) {
  document.querySelector(`.tab-link[data-tab="${tabName}"]`).click();
}
