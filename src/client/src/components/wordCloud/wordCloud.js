import 'd3-transition';
import React from "react";
import { select } from 'd3-selection';
import ReactWordcloud from 'react-wordcloud';

const options = {
  colors: ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b','#d11141' , '#00b159' , '#00aedb' , '#f37735' , '#ffc425'],
  // colors: ['#edc951' , '#eb6841' , '#cc2a36' , '#4f372d' , '#00a0b0'],
  enableTooltip: true,
  deterministic: false,
  fontFamily: 'Prompt',
  fontSizes: [10, 150],
  fontStyle: 'italic',
  fontWeight: 'bold',
  padding: 1,
  rotations: 3,
  rotationAngles: [0, 0],
  scale: 'log', //log
  spiral: 'archimedean',
  transitionDuration: 1000,
};

const getCallback = callbackName => (word, event) => {
  const isActive = callbackName !== 'onWordMouseOut'
  const element = event.target
  const text = select(element)
  text
    .on('click', () => {
      if (isActive) {
        // window.location.href = `http://localhost:3000/university/${word.text}`
        window.location.href = `http://picktoptrends.com/university/${word.text}`
      }
    })
    .transition()
    .attr('background', 'white')
    // .attr('font-size', isActive ? '300%' : '100%')
    .attr('text-decoration', isActive ? 'underline' : 'none')
}

class wordCloud extends React.Component {
  constructor() {
    super();
    this.state = {
      list: []
    };
  }

  componentDidMount() {
      fetch('/getWordClouds')
      .then(res => res.json())
      .then(data => this.setState({ list: data })
      );
  }

  componentWillUpdate(){
      setTimeout(() => {
        fetch('/getWordClouds')
        .then(res => res.json())
        .then(data => this.setState({ list: data })
        );
      }, 120000);
  }

  render() {
    return (
      <div class="card card-wordcloud ">
        <div class="card-body">
          <h1 class="card-title" style={{ fontSize: "30px"}}>เทรนด์มาแรง</h1>
          <div style={{ height: 667, width: 'auto' }}>
            <ReactWordcloud options={options} words={this.state.list} callbacks={{
        onWordClick: getCallback('onWordClick'),
        onWordMouseOut: getCallback('onWordMouseOut'),
        onWordMouseOver: getCallback('onWordMouseOver'),
      }} />
          </div>
        </div>
      </div>
    );
  }
}

export default wordCloud;