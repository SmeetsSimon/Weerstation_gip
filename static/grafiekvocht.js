$(document).ready(function () {
    console.log("luchtvochtigheid");
    //line
    var ctxL = document.getElementById("lineChartvocht").getContext("2d");
    var myLineChart = new Chart(ctxL, {
      type: "line",
      data: {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [
          {
            label: "luchtvochtigheid",
            data: temperatuur,
            backgroundColor: ["rgba(161, 207, 252, 0.8)"],
            borderColor: ["rgba(6, 133, 254, 0.8)"],
            borderWidth: 2,
          },
          
        ],
      },
      options: {
        responsive: true,
      },
    });
  });
  