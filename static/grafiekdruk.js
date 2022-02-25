$(document).ready(function () {
  console.log("luchtdruk");
  //line
  var ctxL = document.getElementById("lineChartdruk").getContext("2d");
  var myLineChart = new Chart(ctxL, {
    type: "line",
    data: {
      labels: ["January", "February", "March", "April", "May", "June", "July"],
      datasets: [
        {
          label: "luchtdruk",
          data: luchtdruk,
          backgroundColor: ["rgba(201, 255, 232, 0.8)"],
          borderColor: ["rgba(0, 255, 146, 0.8)"],
          borderWidth: 2,
        },
       
      ],
    },
    options: {
      responsive: true,
    },
  });
});
