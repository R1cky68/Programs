// Animating lines
document.addEventListener('DOMContentLoaded', function() {   
  var line1 = document.querySelector('.line1');   
  var line2 = document.querySelector('.line2');   
  var line3 = document.querySelector('.line3');   
  var line4 = document.querySelector('.line4');    

  // Function to move lines   
  function moveLineLeft() {       
  line1.style.transform = 'translateX(-1670px)';   
  }    

  function moveLineDown() {     
  line2.style.transform = 'translateY(760.5px)';   
  }    

  function moveLineUp() {     
  line3.style.transform = 'translateY(-850px)';   
  }   

  function moveLineRight(){     
  line4.style.transform ='translateX(1712px)';   
  }    
  
  // Trigger the animation when the page is fully loaded
  moveLineLeft(); 
  moveLineRight(); 
  setTimeout(moveLineUp, 1000);
  setTimeout(moveLineDown, 1000);    
});

// Clicking programs to flip
function flipCard(card) {
  card.classList.toggle('flipped');
}

// Collapisble FAQ buttons 
document.addEventListener('DOMContentLoaded', function() {
var qn = document.getElementsByClassName("Q");

for (var i = 0; i < qn.length; i++) {
    qn[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var A = this.nextElementSibling;

    if (A.style.maxHeight){
      A.style.maxHeight = null;
    } 

    else {
        A.style.maxHeight = A.scrollHeight + "px";
    } 
  });

}
});

// Email submission on homepage
document.getElementById('DOMContentLoaded', function() {
  document.getElementById('Subscribe').addEventListener('submit', function (event) {
    event.preventDefault();
    
  const email = document.getElementById('email').value;

    fetch(`/subscribe`, {
        method: 'POST',
        body: JSON.stringify({ email: email }),
        headers: {
          'Content-type': 'application/json'
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data.message);
        alert(data.message);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
  });
});

// Form submission contact
document.getElementById('DOMContentLoaded', function() {
  document.getElementById('filling').addEventListener('submit', function(event){
    event.preventDefault();

    const name = document.getElementById('name').value;
    const mail = document.getElementById('mail').value;
    const message = document.getElementById('paragraph').value;

    fetch(`/fill`, {
      method: 'POST',
      headers: {
        'Content-type': 'application/json'
      },
      body: JSON.stringify({ 
        name: name,
        mail: mail,
        message: message,
      }),
    })

    .then(response => response.json())
    .then(data => {
      console.log('Success:', data.message);
      alert(data.message);
  })

    .catch((error) => {
        console.error('Error:', error);
    });
  });

});

// for DOM, change to addEventListener instead of getElementById?
