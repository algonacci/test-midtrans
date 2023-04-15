const priceElement = document.getElementById("price");
const priceText = priceElement.textContent;
const price = parseInt(priceText.substring(2).replace(/\./g, ""));

// Get the Checkout button element
const checkoutButton = document.querySelector("button");

// Add a click event listener to the Checkout button
checkoutButton.addEventListener("click", async () => {
  try {
    // Send a request to your Flask endpoint to create a transaction
    const response = await fetch("/", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: new URLSearchParams({
        price: price,
      }),
    });

    // Parse the response JSON data
    const data = await response.json();

    // Redirect the user to the payment Snap page
    window.location.href = `https://app.sandbox.midtrans.com/snap/v2/vtweb/${data.token}`;
  } catch (error) {
    console.error(error);
  }
});
