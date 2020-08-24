import React from "react";
import './search.css'


class ResultSearch extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            list: [],
            list2:[],
            search : "",
            total: 1,
            loading: false,
            isOpen: false,
            data: {
                gte: '',
                lte: '',
                sortby: 'no',
                keyword:"",
                university: []
            },
            gteDate: {
                day: 'no',
                month: 'no',
                year: 'no',
                hour: '00',
                minute: '00'
            },
            lteDate: {
                day: 'no',
                month: 'no',
                year: 'no',
                hour: '00',
                minute: '00'
            },
            resultFilter: "",
            checkDirty: "",
            checkPicture: false
        };
    }

    componentDidMount(){
        this.setState({search:this.props.match.params.id})
        fetch(`/getSearch/${this.props.match.params.id}`)
            .then(res => res.json())
            .then(data => this.setState({resultFilter: "ผลการค้นหา " + data.length.toString() + " ทวีต", list: data,loading:true })
        );
    }

    componentDidUpdate(){
        setTimeout(() => {
            this.checkUpdate(this.props.match.params.id)
        }, 100);
        
    }

    checkUpdate(id){
        if(id!==this.state.search){
            console.log('test')
            this.setState({search:this.props.match.params.id})
            fetch(`/getSearch/${this.props.match.params.id}`)
            .then(res => res.json())
            .then(data => this.setState({ list: data })
        );
        } else {

        }
    }

    checkBox() {
        this.state.data.university = []
        this.setState({checkDirty:'',checkPicture:false})
        if (this.refs.dirty.checked){
            this.state.checkDirty = "dirty"
        } if (this.refs.picture.checked){
            this.setState({checkPicture:true})
        }
    }

    openReadmore = (userid, idstr) => {
        window.open('https://twitter.com/' + userid + '/status/' + idstr)
    }

    filter = () => {
        this.setState({ isOpen: !this.state.isOpen })
    }

    radioButton(event) {
        this.state.data.sortby = event.target.value
    }

    radioButton2(event) {
        this.state.filterMore = event.target.value
    }

    gteSelectDay = (event) => {
        this.state.gteDate.day = event.target.value
    }

    gteSelectMonth = (event) => {
        if (event.target.value == '0') {
            this.state.gteDate.month = '01'
        } else if (event.target.value == '1') {
            this.state.gteDate.month = '02'
        } else if (event.target.value == '2') {
            this.state.gteDate.month = '03'
        } else if (event.target.value == '3') {
            this.state.gteDate.month = '04'
        } else if (event.target.value == '4') {
            this.state.gteDate.month = '05'
        } else if (event.target.value == '5') {
            this.state.gteDate.month = '06'
        } else if (event.target.value == '6') {
            this.state.gteDate.month = '07'
        } else if (event.target.value == '7') {
            this.state.gteDate.month = '08'
        } else if (event.target.value == '8') {
            this.state.gteDate.month = '09'
        } else if (event.target.value == '9') {
            this.state.gteDate.month = '10'
        } else if (event.target.value == '10') {
            this.state.gteDate.month = '11'
        } else if (event.target.value == '11') {
            this.state.gteDate.month = '12'
        } else {
            this.state.gteDate.month = event.target.value
        }
    }

    gteSelectYear = (event) => {
        this.state.gteDate.year = event.target.value
    }

    gteSelectHour = (event) => {
        this.state.gteDate.hour = event.target.value
    }

    gteSelectMinute = (event) => {
        this.state.gteDate.minute = event.target.value
    }

    getGte() {
        this.state.data.gte = ''
        if (this.state.gteDate.day == 'no' || this.state.gteDate.month == 'no' || this.state.gteDate.year == 'no') {
            this.state.data.gte = ''
        } else {
            this.state.data.gte = this.state.gteDate.year + '-' + this.state.gteDate.month + '-' + this.state.gteDate.day + 'T' + this.state.gteDate.hour + ':' + this.state.gteDate.minute + ':00.000Z'
        }
    }

    lteSelectDay = (event) => {
        this.state.lteDate.day = event.target.value
    }

    lteSelectMonth = (event) => {
        if (event.target.value == '0') {
            this.state.lteDate.month = '01'
        } else if (event.target.value == '1') {
            this.state.lteDate.month = '02'
        } else if (event.target.value == '2') {
            this.state.lteDate.month = '03'
        } else if (event.target.value == '3') {
            this.state.lteDate.month = '04'
        } else if (event.target.value == '4') {
            this.state.lteDate.month = '05'
        } else if (event.target.value == '5') {
            this.state.lteDate.month = '06'
        } else if (event.target.value == '6') {
            this.state.lteDate.month = '07'
        } else if (event.target.value == '7') {
            this.state.lteDate.month = '08'
        } else if (event.target.value == '8') {
            this.state.lteDate.month = '09'
        } else if (event.target.value == '9') {
            this.state.lteDate.month = '10'
        } else if (event.target.value == '10') {
            this.state.lteDate.month = '11'
        } else if (event.target.value == '11') {
            this.state.lteDate.month = '12'
        } else {
            this.state.lteDate.month = event.target.value
        }
    }

    lteSelectYear = (event) => {
        this.state.lteDate.year = event.target.value
    }

    lteSelectHour = (event) => {
        this.state.lteDate.hour = event.target.value
    }

    lteSelectMinute = (event) => {
        this.state.lteDate.minute = event.target.value
    }

    getLte() {
        this.state.data.lte = ''
        if (this.state.lteDate.day == 'no' || this.state.lteDate.month == 'no' || this.state.lteDate.year == 'no') {
            this.state.data.lte = ''
        } else {
            this.state.data.lte = this.state.lteDate.year + '-' + this.state.lteDate.month + '-' + this.state.lteDate.day + 'T' + this.state.lteDate.hour + ':' + this.state.lteDate.minute + ':00.000Z'
        }
    }

    getKeyword(){
        this.state.data.university = []
        this.state.data.keyword = ""
        if(this.state.search == 'มหาวิทยาลัยธรรมศาสตร์'){
            this.state.data.university.push('Thammasat')
        } else if(this.state.search == 'จุฬาลงกรณ์มหาวิทยาลัย'){
            this.state.data.university.push('Chula')
        } else if(this.state.search == 'มหาวิทยาลัยมหิดล'){
            this.state.data.university.push('Mahidol')
        } else if(this.state.search == 'มหาวิทยาลัยเกษตรศาสตร์'){
            this.state.data.university.push('Kasetsart')
        }else if(this.state.search == 'มหาวิทยาลัยเชียงใหม่'){
            this.state.data.university.push('Chiang Mai')
        }else if(this.state.search == 'มหาวิทยาลัยขอนแก่น'){
            this.state.data.university.push('Khon Kaen')
        }else if(this.state.search == 'มหาวิทยาลัยศรีนครินทรวิโรฒ'){
            this.state.data.university.push('Srinakharinwirot')
        }else if(this.state.search == 'มหาวิทยาลัยมหาสารคาม'){
            this.state.data.university.push('Mahasarakham')
        }else if(this.state.search == 'มหาวิทยาลัยบูรพา'){
            this.state.data.university.push('Burapha')
        }else if(this.state.search == 'มหาวิทยาลัยแม่ฟ้าหลวง'){
            this.state.data.university.push('Mae Fah Luang')
        }else{
            this.state.data.keyword = this.state.search
        }
    }

    searchFilter = () => {
        this.checkBox()
        this.getKeyword()
        this.getGte()
        this.getLte()
        this.setState({ list: [], loading: false })
        if(this.state.checkDirty == 'dirty'){
            fetch('/filterTweetBySearch', {
                method: 'POST', // or 'PUT'
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(this.state.data),
            })
                .then(res => res.json())
                .then(data => this.setState({ list2: data})
                );
            setTimeout(() => {
                this.checkDirty()
            }, 5000);
        } else{
            fetch('/filterTweetBySearch', {
                method: 'POST', // or 'PUT'
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(this.state.data),
            })
                .then(res => res.json())
                .then(data => this.setState({ resultFilter: "ผลการค้นหา " + data.length.toString() + " ทวีต", list: data, loading: true, total: 1 })
                );
        }
    }

    checkDirty() {
        for (var i = 0; i < this.state.list2.length; i++) {
            try{
                if (this.state.list2[i].text.includes('เย็ด')) {
                    this.state.list2[i].text = "เซ็นเซอร์เนื้อหาที่มีคำหยาบคายโดย Picktoptrends.com"
                    this.state.list2[i].checkImg = false
                }
                if(this.state.list2[i].text.includes('เงี่ยน')){
                    this.state.list2[i].text = "เซ็นเซอร์เนื้อหาที่มีคำหยาบคายโดย Picktoptrends.com"
                    this.state.list2[i].checkImg = false
                }
                if(this.state.list2[i].text.includes('รับงาน')){
                    this.state.list2[i].text = "เซ็นเซอร์เนื้อหาที่มีคำหยาบคายโดย Picktoptrends.com"
                    this.state.list2[i].checkImg = false
                }
                if(this.state.list2[i].text.includes('ควย')){
                    this.state.list2[i].text = "เซ็นเซอร์เนื้อหาที่มีคำหยาบคายโดย Picktoptrends.com"
                    this.state.list2[i].checkImg = false
                }
            }
            catch{
                
            }
        }
        this.setState({ resultFilter: "ผลการค้นหา " + this.state.list2.length.toString() + " ทวีต", list: this.state.list2, loading: true, total: 1 })
    }
    
    renderTrends() {
        return this.state.list;
    }

    toggle = () => {
        this.setState({ total: this.state.total + 1 });
    }

    getRendersTweetBlockOne() {
        let tweet = this.state.list;
        return tweet.slice(0, 10 * this.state.total);
    }

    getRendersTweetBlockTwo() {
        let tweet = this.state.list;
        return tweet.slice(10 * this.state.total, 20 * this.state.total);
    }

    getRendersTweetBlockThree() {
        let tweet = this.state.list;
        return tweet.slice(20 * this.state.total, 30 * this.state.total);
    }

    getRendersTweetBlockFour() {
        let tweet = this.state.list;
        return tweet.slice(30 * this.state.total, 40 * this.state.total);
    }

    render() {
        let day = []
        let month = ['มกราคม', 'กุมภาพันธ์', 'มีนาคม', 'เมษายน', 'พฤษภาคม', 'มิถุนายน', 'กรกฏาคม', 'สิงหาคม', 'กันยายน', 'ตุลาคม', 'พฤศจิกายน', 'ธันวาคม']
        let hour = []
        let minute = []
        for (let i = 1; i <= 31; i++) {
            if (i < 10) { day.push(<option value={"0" + i}>{i}</option>) }
            else { day.push(<option value={i}>{i}</option>) }

        }
        for (let i = 0; i < 24; i++) {
            if (i < 10) { hour.push(<option value={"0" + i}>{i}</option>) }
            else { hour.push(<option value={i}>{i}</option>) }
        }
        for (let i = 0; i < 60; i++) {
            if (i < 10) { minute.push(<option value={"0" + i}>{i}</option>) }
            else { minute.push(<option value={i}>{i}</option>) }
        }
        return (
            <div>
                <nav class="navbar navbar-dark " style={{ height: '60px', backgroundColor: '#03396c', marginTop: '80px', marginLeft: "17px", marginRight: "17px" }}>
                    <a class="navbar-brand" >
                        <img src="https://pngimg.com/uploads/twitter/twitter_PNG3.png" width="30" height="30" class="d-inline-block align-top" alt="" />
                    ทวิตเตอร์ : {this.state.resultFilter}
                    </a>
                    <button className="btn btn-outline-light" onClick={this.filter} style={{ width: "8%", height: "40px", marginLeft: '4px' }}><i class="fa fa-sliders" aria-hidden="true"></i> ตัวกรองการค้นหา</button>
                </nav>
                {this.state.isOpen ? <div class="card" style={{ marginTop: '15px', marginLeft: "17px", marginRight: "17px", boxShadow: "0 1px 3px 0 #03396c , 0 0 0 2px #03396c" }}>
                    <div class="card-body">
                        <div class="row">
                            <div class="col-xl-4 col-sm-12">
                                <div class="row">
                                    <div class="col-6">
                                        <h3>
                                            จัดเรียงตาม:
                                        </h3>
                                        <div onChange={this.radioButton.bind(this)}>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios1" value="current" />
                                                <label class="form-check-label" for="exampleRadios1">
                                                    อัพเดทล่าสุด
                                            </label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios2" value="retweet" />
                                                <label class="form-check-label" for="exampleRadios2">
                                                    รีทวีตมากที่สุด
                                        </label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios3" value="favorite" />
                                                <label class="form-check-label" for="exampleRadios3">
                                                    ความชอบมากที่สุด
                                        </label>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-6">
                                        <h3>
                                            เพิ่มเติม:
                                        </h3>
                                        <div onChange={this.radioButton2.bind(this)}>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" ref="dirty" value="Srinakharinwirot" id="Srinakharinwirot" />
                                                <label class="form-check-label" for="defaultCheck1">
                                                    กรองคำหยาบ
                                                </label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" ref="picture" value="Srinakharinwirot" id="Srinakharinwirot" />
                                                <label class="form-check-label" for="defaultCheck1">
                                                    แสดงรูปภาพ
                                                </label>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                            </div>
                            <div class="col-xl-4 col-sm-12">
                                <h3>
                                    ตั้งแต่:
                                </h3>
                                <label class="my-1 mr-2" for="inlineFormCustomSelectPref">วันที่</label>
                                <select class="custom-select my-1 mr-sm-2" id="inlineFormCustomSelectPref" onChange={this.gteSelectDay}>
                                    <option selected value="no">เลือกวันที่</option>
                                    {day}
                                </select>
                                <label class="my-1 mr-2" for="inlineFormCustomSelectPref">เดือน</label>
                                <select class="custom-select my-1 mr-sm-2" id="inlineFormCustomSelectPref" onChange={this.gteSelectMonth}>
                                    <option selected value="no">เลือกเดือน</option>
                                    {month.map((object, i) => <option value={i}>{object}</option>)}
                                </select>
                                <label class="my-1 mr-2" for="inlineFormCustomSelectPref">ปี</label>
                                <select class="custom-select my-1 mr-sm-2" id="inlineFormCustomSelectPref" onChange={this.gteSelectYear}>
                                    <option selected value="no">เลือกปี</option>
                                    <option value="2020">2020</option>
                                    <option value="2021">2021</option>
                                    <option value="2022">2022</option>
                                </select>
                                <div class="row">
                                    <div class="col-6">
                                        <label class="my-1 mr-2" for="inlineFormCustomSelectPref">ชั่วโมง</label>
                                        <select class="custom-select my-1 mr-sm-2" id="inlineFormCustomSelectPref" onChange={this.gteSelectHour}>>
                                            <option selected value="no">เลือกชั่วโมง</option>
                                            {hour}
                                        </select>
                                    </div>
                                    <div class="col-6">
                                        <label class="my-1 mr-2" for="inlineFormCustomSelectPref">นาที</label>
                                        <select class="custom-select my-1 mr-sm-2" id="inlineFormCustomSelectPref" onChange={this.gteSelectMinute}>>
                                            <option selected value="no">เลือกนาที</option>
                                            {minute}
                                        </select>
                                    </div>
                                </div>
                            </div>
                            <div class="col-xl-4 col-sm-12">
                                <h3>
                                    ถึง:
                                </h3>
                                <label class="my-1 mr-2" for="inlineFormCustomSelectPref">วันที่</label>
                                <select class="custom-select my-1 mr-sm-2" id="inlineFormCustomSelectPref" onChange={this.lteSelectDay}>
                                    <option selected value="no">เลือกวันที่</option>
                                    {day}
                                </select>
                                <label class="my-1 mr-2" for="inlineFormCustomSelectPref">เดือน</label>
                                <select class="custom-select my-1 mr-sm-2" id="inlineFormCustomSelectPref" onChange={this.lteSelectMonth}>
                                    <option selected value="no">เลือกเดือน</option>
                                    {month.map((object, i) => <option value={i}>{object}</option>)}
                                </select>
                                <label class="my-1 mr-2" for="inlineFormCustomSelectPref">ปี</label>
                                <select class="custom-select my-1 mr-sm-2" id="inlineFormCustomSelectPref" onChange={this.lteSelectYear}>
                                    <option selected value="no">เลือกปี</option>
                                    <option value="2020">2020</option>
                                    <option value="2021">2021</option>
                                    <option value="2022">2022</option>
                                </select>
                                <div class="row">
                                    <div class="col-6">
                                        <label class="my-1 mr-2" for="inlineFormCustomSelectPref">ชั่วโมง</label>
                                        <select class="custom-select my-1 mr-sm-2" id="inlineFormCustomSelectPref" onChange={this.lteSelectHour}>
                                            <option selected value="no">เลือกชั่วโมง</option>
                                            {hour}
                                        </select>
                                    </div>
                                    <div class="col-6">
                                        <label class="my-1 mr-2" for="inlineFormCustomSelectPref">นาที</label>
                                        <select class="custom-select my-1 mr-sm-2" id="inlineFormCustomSelectPref" onChange={this.lteSelectMinute}>
                                            <option selected value="no">เลือกนาที</option>
                                            {minute}
                                        </select>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <br />
                        <button type="submit" onClick={this.searchFilter} class="btn btn-outline-info col-12" style={{ height: "45px" }}><i class="fa fa-sliders" aria-hidden="true"></i> กรองการค้นหา</button>
                    </div>
                </div> : ""}
                <div class="row" style={{ marginLeft: "3px", marginRight: "3px" }}>
                    <div class="col-xl-3 col-sm-12" style={{ marginTop: "15px" }}>
                        {this.getRendersTweetBlockOne().map((item, index) => (
                            <div>
                                <div class="card card-inverse card-info " style={{ marginTop: "10px" }}>
                                    <div class="card-block">
                                        <figure class="profile profile-inline" style={{ boxShadow: '0 1px 1px 0 #aaaaaa, 0 0 0 1px #aaaaaa' }}>
                                            <img src={item.user_img} class="profile-avatar" alt="" />
                                        </figure>
                                        <h4 class="card-title">{item.user_name}<br /><small>{item.created_at}</small></h4>
                                        <div class="card-text" >
                                            {item.text}
                                            {this.state.checkPicture ? <div style={{ width: 'auto' }}>
                                                <img src={item.img} style={{ width: '100%', height: 'auto' }} alt="" />
                                            </div> : ""}
                                        </div>
                                    </div>
                                    <div class="card-footer">
                                        <a style={{ fontSize: "16px" }}><i class="fa fa-retweet" style={{ color: "#0392cf" }} aria-hidden="true"></i> {item.retweet_count}<span style={{ fontSize: "12px"}}>(<i class="fa fa-arrow-up" style={{ color: "#66bb6a" }} aria-hidden="true"></i>{item.retweet_1Day})</span> <i class="fa fa-heart" aria-hidden="true" style={{ color: "red" }}></i> {item.favorite_count}</a>
                                        <button class="btn btn-info float-right btn-sm" onClick={() => this.openReadmore(item.user_id, item.id_str)}>อ่านเพิ่มเติม <i class="fa fa-info-circle" aria-hidden="true"></i></button>
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>
                    <div class="col-xl-3 col-sm-12" style={{ marginTop: "15px" }}>
                        {this.getRendersTweetBlockTwo().map((item, index) => (
                            <div>
                                <div class="card card-inverse card-info " style={{ marginTop: "15px" }}>
                                    <div class="card-block">
                                        <figure class="profile profile-inline" style={{ boxShadow: '0 1px 1px 0 #aaaaaa, 0 0 0 1px #aaaaaa' }}>
                                            <img src={item.user_img} class="profile-avatar" alt="" />
                                        </figure>
                                        <h4 class="card-title">{item.user_name}<br /><small>{item.created_at}</small></h4>
                                        <div class="card-text" >
                                            {item.text}
                                            {this.state.checkPicture ? <div style={{ width: 'auto' }}>
                                                <img src={item.img} style={{ width: '100%', height: 'auto' }} alt="" />
                                            </div> : ""}
                                        </div>
                                    </div>
                                    <div class="card-footer">
                                        <a style={{ fontSize: "16px" }}><i class="fa fa-retweet" style={{ color: "#0392cf" }} aria-hidden="true"></i> {item.retweet_count}<span style={{ fontSize: "12px"}}>(<i class="fa fa-arrow-up" style={{ color: "#66bb6a" }} aria-hidden="true"></i>{item.retweet_1Day})</span> <i class="fa fa-heart" aria-hidden="true" style={{ color: "red" }}></i> {item.favorite_count}</a>
                                        <button class="btn btn-info float-right btn-sm" onClick={() => this.openReadmore(item.user_id, item.id_str)}>อ่านเพิ่มเติม <i class="fa fa-info-circle" aria-hidden="true"></i></button>
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>
                    <div class="col-xl-3 col-sm-12" style={{ marginTop: "15px" }}>
                        {this.getRendersTweetBlockThree().map((item, index) => (
                            <div>
                                <div class="card card-inverse card-info" style={{ marginTop: "15px" }}>
                                    <div class="card-block">
                                        <figure class="profile profile-inline" style={{ boxShadow: '0 1px 1px 0 #aaaaaa, 0 0 0 1px #aaaaaa' }}>
                                            <img src={item.user_img} class="profile-avatar" alt="" />
                                        </figure>
                                        <h4 class="card-title">{item.user_name}<br /><small>{item.created_at}</small></h4>
                                        <div class="card-text" >
                                            {item.text}
                                            {this.state.checkPicture ? <div style={{ width: 'auto' }}>
                                                <img src={item.img} style={{ width: '100%', height: 'auto' }} alt="" />
                                            </div> : ""}
                                        </div>
                                    </div>
                                    <div class="card-footer">
                                        <a style={{ fontSize: "16px" }}><i class="fa fa-retweet" style={{ color: "#0392cf" }} aria-hidden="true"></i> {item.retweet_count}<span style={{ fontSize: "12px"}}>(<i class="fa fa-arrow-up" style={{ color: "#66bb6a" }} aria-hidden="true"></i>{item.retweet_1Day})</span> <i class="fa fa-heart" aria-hidden="true" style={{ color: "red" }}></i> {item.favorite_count}</a>
                                        <button class="btn btn-info float-right btn-sm" onClick={() => this.openReadmore(item.user_id, item.id_str)}>อ่านเพิ่มเติม <i class="fa fa-info-circle" aria-hidden="true"></i></button>
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>
                    <div class="col-xl-3 col-sm-12" style={{ marginTop: "15px" }}>
                        {this.getRendersTweetBlockFour().map((item, index) => (
                            <div>
                                <div class="card card-inverse card-info" style={{ marginTop: "15px" }}>
                                    <div class="card-block">
                                        <figure class="profile profile-inline" style={{ boxShadow: '0 1px 1px 0 #aaaaaa, 0 0 0 1px #aaaaaa' }}>
                                            <img src={item.user_img} class="profile-avatar" alt="" />
                                        </figure>
                                        <h4 class="card-title">{item.user_name}<br /><small>{item.created_at}</small></h4>
                                        <div class="card-text" >
                                            {item.text}
                                            {this.state.checkPicture ? <div style={{ width: 'auto' }}>
                                                <img src={item.img} style={{ width: '100%', height: 'auto' }} alt="" />
                                            </div> : ""}
                                        </div>
                                    </div>
                                    <div class="card-footer">
                                        <a style={{ fontSize: "16px" }}><i class="fa fa-retweet" style={{ color: "#0392cf" }} aria-hidden="true"></i> {item.retweet_count}<span style={{ fontSize: "12px"}}>(<i class="fa fa-arrow-up" style={{ color: "#66bb6a" }} aria-hidden="true"></i>{item.retweet_1Day})</span> <i class="fa fa-heart" aria-hidden="true" style={{ color: "red" }}></i> {item.favorite_count}</a>
                                        <button class="btn btn-info float-right btn-sm" onClick={() => this.openReadmore(item.user_id, item.id_str)}>อ่านเพิ่มเติม <i class="fa fa-info-circle" aria-hidden="true"></i></button>
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
                <div class="container-fluid" style={{ marginTop: "25px" }}>
                    <button type="button" class="btn btn-outline-info col-12" style={{ height: "45px" }} onClick={this.toggle}>{this.state.loading ? 'แสดงเพิ่มเติม' : <div><div class="spinner-grow spinner-border-sm" role="status">
                        <span class="sr-only">Loading...</span>
                    </div><span > กำลังโหลด</span></div>}</button>

                </div>

            </div>
        );
    }
}

export default ResultSearch;