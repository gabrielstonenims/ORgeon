$(function() {
  setTimeout(function() {
    $(".alert").slideUp(3000);
  }, 5000);


  $(document).on("submit", ".post-comment-form", function(event) {
    event.preventDefault();
    $.ajax({
      type: "POST",
      url: $(this).attr("action"),
      data: $(this).serialize(),
      dataType: "json",
      success: function(response) {
        $(".main-comment-section").html(response["form"]);
        $("textarea").val("");
      },
      error: function(rs, e) {
        console.log(rs.responseText);
      }
    });
  });
  // reply-instant message
  $(document).on("submit", ".instant-form", function(event) {
    event.preventDefault();
    $.ajax({
      type: "POST",
      url: $(this).attr("action"),
      data: $(this).serialize(),
      dataType: "json",
      success: function(response) {
        $(".main-reply-section").html(response["form"]);
        $("textarea").val("");
      },
      error: function(rs, e) {
        console.log(rs.responseText);
      }
    });
  });

  var usr = document.querySelector("#users").innerHTML;
  var subs = document.querySelector("#sub").innerHTML;
  var vols = document.querySelector("#voluns").innerHTML;
  var partners = document.querySelector("#parts").innerHTML;
  var clients = document.querySelector("#clients").innerHTML;
  // for the charts
  var ctx = document.getElementById("myChart");
  Chart.defaults.global.defaultFontFamily = "Lato";
  Chart.defaults.global.defaultFontSize = 15;
  Chart.defaults.global.defaultFontColor = "#fff";
  var myChart = new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: [
        "Employees",
        "Subscribers",
        "Volunteers",
        "Partners",
        // "Messaging",
        "Clients"
      ],
      datasets: [
        {
          label: "#",
          data: [usr, subs, vols, partners,clients],
          backgroundColor: [
            "rgba(255,99,132,0.6)",
            "rgba(54,162,235,0.6)",
            "rgba(255,206,86,0.6)",
            "rgba(75,192,192,0.6)",
            // "rgba(153,102,255,0.6)",
            "rgba(153,302,455,0.8)",
          ],
          borderColor: "#777",
          borderWidth: 1,
          hoverBorderWidth: 3,
          hoverBorderColor: "#000"
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: "ORgeon of stars' Activities",
        fontSize: 20,
        fontColor: "#fff"
      },
      legend: {
        display: true,
        position: "right",
        labels: {
          fontColor: "#fff"
        }
      },
      tooltips: {
        // enable:false
      },
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true
            }
          }
        ]
      }
    }
  });

//  students activity
  var students = document.querySelector("#students").innerHTML;
  var gradeschool = document.querySelector("#gradeschool").innerHTML;
  var preschool = document.querySelector("#preschool").innerHTML;
  var kindergarten = document.querySelector("#kindergarten").innerHTML;
  // for the charts
  var ctx = document.getElementById("myChart2");
  Chart.defaults.global.defaultFontFamily = "Lato";
  Chart.defaults.global.defaultFontSize = 15;
  Chart.defaults.global.defaultFontColor = "#fff";
  var myChart1 = new Chart(ctx, {
//    type: "doughnut",
    type: "pie",
    data: {
      labels: [
        "Total Students",
        "GradeSchool",
        "PreSchool",
        "Kindergarten",
        // "Messaging",
      ],
      datasets: [
        {
          label: "#",
          data: [students, gradeschool, preschool, kindergarten],
          backgroundColor: [
            "rgba(255,99,132,0.6)",
            "rgba(54,162,235,0.6)",
            "rgba(255,206,86,0.6)",
            "rgba(75,192,192,0.6)",

          ],
          borderColor: "#777",
          borderWidth: 1,
          hoverBorderWidth: 3,
          hoverBorderColor: "#000"
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: "Summer Tutoring Activities",
        fontSize: 20,
        fontColor: "#fff"
      },
      legend: {
        display: true,
        position: "right",
        labels: {
          fontColor: "#fff"
        }
      },
      tooltips: {
        // enable:false
      },
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true
            }
          }
        ]
      }
    }
  });
});
