import React from "react";
import './TweetTrends.css';
import TweetTrends from './TweetTrends'

class TrendsBox extends React.Component {
    constructor() {
        super();
        this.state = {
            list: [],
            date: ""
        };
    }

    componentDidMount() {
        var x = new Date()
        var hour = ""
        var minute = ""
        var yhour = ""
        var yminute = ""
        if(x.getHours()<10){
            hour = "0"+x.getHours().toString()
        } else{
            hour = x.getHours().toString()
        } if(x.getMinutes()<10){
            minute = "0"+x.getMinutes().toString()
        } else{
            minute = x.getMinutes().toString()
        }
        x.setMinutes(x.getMinutes()-60)
        if(x.getHours()<10){
            yhour = "0"+x.getHours().toString()
        } else{
            yhour = x.getHours().toString()
        } if(x.getMinutes()<10){
            yminute = "0"+x.getMinutes().toString()
        } else{
            yminute = x.getMinutes().toString()
        }
        this.setState({date:yhour+":"+yminute+" - "+hour+":"+minute+"น."})
        
    }
    render() {
        return (
            <div class="card example-1 square scrollbar-dusty-grass square thin border-success ">
                <div class="card-header " style={{backgroundColor:"#d62d20",fontWeight:"400",fontSize:"18px",color:"white"}}>10 ทวีตยอดนิยมใน 3 ชั่วโมงล่าสุด</div>
                <div class="card-body text-dark">
                    <TweetTrends/>
                </div>
            </div>
        );
    }
}

export default TrendsBox;