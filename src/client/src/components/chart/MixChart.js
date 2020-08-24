import React from "react";
import ReactApexChart from "react-apexcharts";


class ChartViewer extends React.Component {
    constructor(props) {
        super(props);

        this.state = {

            series: [],
            options: {
                chart: {
                    height: 580,
                    type: 'line',
                },
                stroke: {
                    width: [0, 4]
                },
                title: {
                    text: 'จำนวนทวีตและรีทวีตสะสมใน 6 ชั่วโมง'
                },
                dataLabels: {
                    enabled: true,
                    enabledOnSeries: [1]
                },
                xaxis: {
                    categories: ['ม.ธรรมศาสตร์', 'จุฬาฯ', 'ม.มหิดล', 'ม.เกษตรศาสตร์',
                        'ม.เชียงใหม่', 'ม.ขอนแก่น','ม.ศรีนครินทรวิโรฒ','ม.มหาสารคาม',
                        'ม.บูรพา','ม.แม่ฟ้าหลวง'
                    ],
                },
                yaxis: [{
                    title: {
                        text: 'จำนวนทวีต',
                    },

                }, {
                    opposite: true,
                    title: {
                        text: 'จำนวนรีทวีต'
                    }
                }]
            },


        };
    }

    componentDidMount() {
        fetch('/getBarCountGraph')
        .then(res => res.json())
        .then(data => this.setState({ series: data })
      );
  }

    render() {
        return (


            <div id="chart">
                <ReactApexChart options={this.state.options} series={this.state.series} type="line" height={580} />
            </div>


        );
    }
}

export default ChartViewer;