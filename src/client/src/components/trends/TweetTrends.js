import React from "react";

class TweetTrends extends React.Component {
    constructor() {
        super();
        this.state = {
            list: []
        };
    }

    componentDidMount() {
        // var x = new Date()
        // var month = ''
        // var date = ''
        // var year = x.getFullYear().toString()
        // if(x.getMonth() == 0) month = '01'
        // else if(x.getMonth() == 1) month = '02'
        // else if(x.getMonth() == 2) month = '03'
        // else if(x.getMonth() == 3) month = '04'
        // else if(x.getMonth() == 4) month = '05'
        // else if(x.getMonth() == 5) month = '06'
        // else if(x.getMonth() == 6) month = '07'
        // else if(x.getMonth() == 7) month = '08'
        // else if(x.getMonth() == 8) month = '09'
        // else if(x.getMonth() == 9) month = '10'
        // else if(x.getMonth() == 10) month = '11'
        // else if(x.getMonth() == 11) month = '12'

        // if(x.getDate()<10){
        //     date = '0'+ x.getDate().toString()
        // } else{
        //     date = x.getDate().toString()
        // }

        // fetch('/getTweetTrends', {
        //     method: 'POST', 
        //     headers: {
        //         'Content-Type': 'application/json',
        //     },
        //     body: JSON.stringify({date:year+'-'+month+'-'+date+'T00:00:00.000Z'}),
        // })
        // .then(res => res.json())
        // .then(data => this.setState({ list: data })
        // );
        fetch('/getTweetTrends')
            .then(res => res.json())
            .then(data => this.setState({ list: data})
            );
    }

    renderTrends() {
        return this.state.list;
    }

    openReadmore = (userid,idstr) => {
        window.open('https://twitter.com/'+userid+'/status/'+idstr)
    }

    render() {
        return (
            <div>
                {this.renderTrends().map((item, index) => (
                    <div class="card card-inverse card-info" style={{ marginTop: "10px" }}>
                        <div class="card-block">
                            <figure class="profile profile-inline">
                                <img src={item.user_img} class="profile-avatar" alt="" />
                            </figure>
                            <h4 class="card-title">{item.user_name}<br /><small>{item.created_at}</small></h4>
                            <div class="card-text">
                                {item.text}
                                {/* {item.isImgOpen ?<div style={{width:'auto'}}>
                                                <img src={item.img} style={{width:'100%' , height:'auto'}} alt="" />
                                            </div> : ""} */}
                            </div>
                        </div>
                        <div class="card-footer">
                            <a style={{ fontSize: "16px"}}>
                                <i class="fa fa-retweet" style={{ color: "#0392cf" }} aria-hidden="true"></i> {item.retweet_count}<span style={{ fontSize: "12px"}}>(<i class="fa fa-arrow-up" style={{ color: "#66bb6a" }} aria-hidden="true"></i>{item.retweet_30min})</span> <i class="fa fa-heart" aria-hidden="true" style={{ color: "red" }}></i> {item.favorite_count}
                            </a>
                            <button class="btn btn-info float-right btn-sm" onClick={() => this.openReadmore(item.user_id,item.id_str)}>
                                อ่านเพิ่มเติม <i class="fa fa-info-circle" aria-hidden="true"></i>
                            </button>
                        </div>
                    </div>
                ))}
            </div>
        );
    }
}

export default TweetTrends;