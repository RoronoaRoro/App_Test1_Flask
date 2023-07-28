Highcharts.chart("container-donation", {
    chart: {
      type: "bar",
    },
    title: {
      text: "Número de donaciones por tipo",
    },
    xAxis: {
      title: {
        text: "Tipo",
      },
    },
    yAxis: {
      title: {
        text: "Número de donaciones",
      },
      categories: [],
    },
    legend: {
      align: "right",
      verticalAlign: "top",
      borderWidth: 0,
    },
  
    tooltip: {
      shared: true,
      crosshairs: true,
    },
  
    series: [
      {
        name: "Donaciones",
        data: [],
        lineWidth: 1,
        marker: {
          enabled: true,
          radius: 4,
        },
        color: "#FF4000",
      },
    ],
});

fetch("http://localhost:5000/stats-donation")
  .then((response) => response.json())
  .then((data) => {
    let parsedData = data.map((item) => {
        // Info from bd (type & amount of requests)
        return [item[0], item[1]];
    });

    console.log(parsedData);
    // Get the chart that then will be updated
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "container-donation"
    );

    // Update value of the categories
    chart.xAxis[0].setCategories(parsedData.map((item) => item[0]))

    // Update with info from the bd
    chart.update({
      series: [
        {
          data: parsedData,
        },
      ],
    });
  });

  Highcharts.chart("container-request", {
    chart: {
      type: "bar",
    },
    title: {
      text: "Número de pedidos por tipo",
    },
    xAxis: {
      title: {
        text: "Tipo",
      },
    },
    yAxis: {
      title: {
        text: "Número de pedidos",
      },
      categories: [],
    },
    legend: {
      align: "right",
      verticalAlign: "top",
      borderWidth: 0,
    },
  
    tooltip: {
      shared: true,
      crosshairs: true,
    },
  
    series: [
      {
        name: "Pedidos",
        data: [],
        lineWidth: 1,
        marker: {
          enabled: true,
          radius: 4,
        },
        color: "#0B614B",
      },
    ],
});

fetch("http://localhost:5000/stats-request")
  .then((response) => response.json())
  .then((data) => {
    let parsedData = data.map((item) => {
        // Info from the bd (type & amount of requests)
        return [item[0], item[1]];
    });

    // get the chart that then will be updated
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "container-request"
    );

    // Update value of the categories
    chart.xAxis[0].setCategories(parsedData.map((item) => item[0]))

    // Update with info from the bd
    chart.update({
      series: [
        {
          data: parsedData,
        },
      ],
    });
  });