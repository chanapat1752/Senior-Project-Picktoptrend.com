import React from "react";
import './TweetTrends.css';
import TULogo from './img/Thammasat.png'

class cardsBox extends React.Component {
    constructor() {
        super();
        this.state = {
            list: []
        };
    }

    componentDidMount() {
        fetch('/getCard')
            .then(res => res.json())
            .then(data => this.setState({ list: data })
            );
    }

    renderCards() {
        return this.state.list;
    }


    render() {
        return (
            <div style={{ marginTop: "60px" }}>
                {this.renderCards().map((item, index) => (
                    <div class="row" style={{ marginLeft: "3px", marginRight: "3px" }}>

                        <div class="col-xl-3 col-sm-12" style={{ marginTop: "15px" }}>
                            <div class="card-counter primary">
                                <i style={{marginTop:'-10px'}} class="fa fa-university"></i>
                                <span class="count-head">มหาวิทยาลัยถูกกล่าวถึงมากที่สุด</span>
                                <span class="count-numbers">{item.university}</span>
                                <span class="count-name">จำนวน {item.retweet} รีทวีต</span>
                            </div>
                        </div>

                        <div class="col-xl-3 col-sm-12" style={{ marginTop: "15px" }}>
                            <div class="card-counter danger">
                                <i style={{marginTop:'-5px'}} class="fa fa-exclamation-triangle"></i>
                                <span class="count-head">เหตุการณ์ถูกกล่าวถึงมากที่สุด</span>
                                <span class="count-numbers">#{item.hashtag}</span>
                                <span class="count-name">จำนวน {item.hashtagCount} รีทวีต</span>
                            </div>
                        </div>

                        <div class="col-xl-3 col-sm-12" style={{ marginTop: "15px" }}>
                            <div class="card-counter success">
                                <i style={{marginTop:'-10px'}} class="fa fa-twitter"></i>
                                <span class="count-head">จำนวนกล่าวถึงวันที่ {item.date}</span>
                                <span class="count-numbers">{item.retweetInThisDay} รีทวีต</span>
                                <span class="count-name">และ {item.tweetInThisDay} ทวีต</span>
                            </div>
                        </div>

                        <div class="col-xl-3 col-sm-12" style={{ marginTop: "15px" }}>
                            <div class="card-counter info">
                                <i ><img src={TULogo} width='120px' height="120px" style={{marginTop:'-85px'}}/></i>
                                <span class="count-head">ม.ธรรมศาสตร์ถูกกล่าวถึง</span>
                                <span class="count-numbers">{item.thammasatRetweet} รีทวีต</span>
                                <span class="count-name">และ {item.thammasatTweet} ทวีต</span>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        );
    }
}

export default cardsBox;