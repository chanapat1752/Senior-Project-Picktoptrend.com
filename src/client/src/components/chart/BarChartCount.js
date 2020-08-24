import React from "react";
import ReactApexChart from "react-apexcharts";


class ChartViewer extends React.Component {
    constructor(props) {
        super(props);

        this.state = {

            series: [],
            series2: [],
            isMaxMore: false,
            university:[],
            options: {
                chart: {
                    type: 'bar',
                    fontFamily: 'Prompt',
                    height: 580,
                    stacked: true,
                },
                //colors:['#00E396' ,'#0057e7' ],
                colors: ['#35a79c', '#0392cf'],
                fill: {
                    opacity: 1,
                },
                plotOptions: {
                    bar: {
                        horizontal: true,
                    },
                },
                stroke: {
                    width: 1,
                    colors: ['#fff']
                },
                title: {
                    text: 'การกล่าวถึงในวันนี้'
                },
                xaxis: {
                    type:'category'
                },
                yaxis: {
                    title: {
                        text: undefined
                    },
                },
                legend: {
                    position: 'top',
                    horizontalAlign: 'left',
                    offsetX: 40
                }
            },
            options2: {
                chart: {
                    type: 'bar',
                    height: 580,
                    stacked: true,
                },
                //colors:['#00E396' ,'#0057e7' ],
                colors: ['#35a79c', '#0392cf'],
                fill: {
                    opacity: 1,
                },
                plotOptions: {
                    bar: {
                        horizontal: true,
                    },
                },
                stroke: {
                    width: 1,
                    colors: ['#fff']
                },
                xaxis: {
                    type:'category'
                },
                yaxis: {
                    title: {
                        text: undefined
                    },
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
        fetch('/getBarCountGraph')
            .then(res => res.json())
            .then(data => this.setState({ series: data ,isMaxMore:data[0].check})
        );
        fetch('/getBarCountGraph2')
            .then(res => res.json())
            .then(data => this.setState({ series2: data })
        ); 
    }

    render() {
        return (
            <div>
                {this.state.isMaxMore ? <div><div id="chart">
                    <ReactApexChart options={this.state.options} series={this.state.series2} type="bar" height={190} />
                </div>
                <div id="chart">
                    <ReactApexChart options={this.state.options2} series={this.state.series} type="bar" height={380} />
                </div></div> : <div id="chart">
                    <ReactApexChart options={this.state.options} series={this.state.series} type="bar" height={585} />
                </div>}
            </div>
        );
    }
}

export default ChartViewer;