import React from "react";
import ReactApexChart from "react-apexcharts";


class ChartViewer extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      series: [],
      options: {
        chart: {
          type: 'area',
          stacked: false,
          fontFamily: 'Prompt',
          height: 580,
          zoom: {
            type: 'x',
            enabled: true,
            autoScaleYaxis: true
          },
          toolbar: {
            autoSelected: 'zoom'
          }
        },
        dataLabels: {
          enabled: false
        },
        markers: {
          size: 0,
        },
        title: {
          text: 'จำนวนทวีตแต่ละนาที',
          align: 'left'
        },
        fill: {
          type: 'gradient',
          gradient: {
            shadeIntensity: 1,
            inverseColors: false,
            opacityFrom: 0.5,
            opacityTo: 0,
            stops: [0, 90, 100]
          },
        },
        yaxis: {
          title: {
            text: 'จำนวนทวีต'
          },
        },
        xaxis: {
          type: 'datetime'
        },
        colors: ['#008FFB'  , '#00E396' ,  '#FEB019' ,  '#FF4560' ,  '#775DD0','#ee4035' , '#f37736' , '#be9b7b' , '#7bc043' , '#0392cf'],
        stroke: {
          curve: 'smooth',
        },
        tooltip: {
          shared: true,
          x: {
            format: 'dd MMMM yyyy HH:mm'
          }
        },
        legend: {
          position: 'top',
          horizontalAlign: 'left',
          offsetX: 40
      }
      },


    };
  }

  componentDidMount() {
      fetch('/getTweetGraph')
      .then(res => res.json())
      .then(data => this.setState({ series: data })
    );
}

  render() {
    return (


      <div id="chart">
        <ReactApexChart options={this.state.options} series={this.state.series} type="area" height={585} />
      </div>


    );
  }
}

export default ChartViewer;