async function sendToPython(fq) {
  try {
    const response = await fetch("/add-q",{
      method: "POST",
      headers: {
        "Content-Type":"application/json"
      },
      body: JSON.stringify({
        fq
      })
    });

    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const result = await response.json();
    console.log(result);
  } catch (error) {
    console.error(error.message);
  }
}

const element = document.getElementById("final_qoutes")
let i = 0

document.querySelectorAll("button").forEach((button) => {
button.addEventListener("click", (event) => {

    if (event.target.textContent.toLowerCase() === "next"){
      i++;
      element.innerText = jsq[i];
    }
    if (event.target.textContent.toLowerCase() === "back"){
      i--;
      element.innerText = jsq[i];
    }
    if (event.target.textContent.toLowerCase() === "add"){
      sendToPython(jsq[i])
      i++;
      element.innerText = jsq[i];
    }
    if (event.target.textContent.toLowerCase() === "dismiss"){
      i++;
      element.innerText = jsq[i];
    }
  });
});

