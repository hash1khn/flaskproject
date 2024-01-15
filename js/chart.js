// chart.js

document.addEventListener('DOMContentLoaded', function () {
    // Dummy data for demonstration
    var data = {
        labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        datasets: [{
            label: 'Food Left Over Today',
            data: [20, 30, 40, 50, 60, 70, 80], // Replace this array with your actual data
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    };

    // Get the canvas element
    var ctx = document.getElementById('chart2').getContext('2d');

    // Create and render the chart
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: data,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Function to update the chart data
    function updateChartData(newData) {
        myChart.data.datasets[0].data = newData;
        myChart.update();
    }

    // Listen for custom events to update the chart
    document.addEventListener('updateChart', function (event) {
        updateChartData(event.detail.updatedData);
    });
});
