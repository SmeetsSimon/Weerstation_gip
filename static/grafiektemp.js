$(document).ready(function () {
  console.log("tempera");
  //line
  var ctxL = document.getElementById("lineCharttemp").getContext("2d");
  var myLineChart = new Chart(ctxL, {
    type: "line",
    data: {
      labels: ["January", "February", "March", "April", "May", "June", "July"],
      datasets: [
        {
          label: "temperatuur",
          data: temperatuur,
          backgroundColor: ["rgba(255, 174, 124, 0.8)"],
          borderColor: ["rgba(255, 98, 0, 0.8)"],
          borderWidth: 2,
        },
        
      ],
    },
    options: {
      responsive: true,
    },
  });
});
