import React from "react";
import './TweetTrends.css';
import TweetTrends from './TweetTrends';

class TrendsBox extends React.Component {
    constructor() {
        super();
        this.state = {
            list: []
        };
    }

    componentDidMount() {
        fetch('/getTopTrends')
            .then(res => res.json())
            .then(data => this.setState({ list: data })
            );
    }

    openReadmore = (trends) => {
        // window.location.href = `http://localhost:3000/university/${trends}`
        window.location.href = `http://picktoptrends.com/university/${trends}`
    }

    renderTrends() {
        return this.state.list;
    }

    render() {
        return (
            <div class="card" style={{ boxShadow: "0 1px 3px 0 #03396c , 0 0 0 2px #03396c"}}>
                <div class="card-header" style={{backgroundColor:"#03396c",fontWeight:"400",fontSize:"18px",color:"white"}}>
                    10 เทรนด์มาแรง
                </div>
                
                <ul class="list-group list-group-flush" >
                {this.renderTrends().map((item, index) => (
                    <button class="list-group-item trends text-left" onClick={() => this.openReadmore(item.text)} style={{fontSize:"18px",height:'70px'}}><span>#</span>{item.text}<br/><span style={{fontSize:"14px"}}>{item.tweet}</span><span style={{fontSize:"14px"}}> ทวีต  </span><span style={{fontSize:"14px"}}>{item.retweet}</span><span style={{fontSize:"14px"}}> รีทวีต</span></button>
                ))}
                </ul>
                
            </div>

        );
    }
}

export default TrendsBox;