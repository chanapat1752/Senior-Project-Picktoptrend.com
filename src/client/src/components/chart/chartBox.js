import React, { Fragment } from 'react';
import { BrowserRouter as Router, Switch, Route, NavLink } from 'react-router-dom';
import LineRetweet from './LineChartRetweetCount';
// import LineRetweetPermin from './LineChartRetweetPerMinute';
import LineTweet from './LineChartTweetCount';
import BarCount from './BarChartCount';
// import Bar7Days from './ChartOverAll7Days';
import { createBrowserHistory as history } from 'history';

class chart extends React.Component {
    render() {
        return (
            <div>
                <Fragment>
                    <Router history={history}>
                            <div class="card card-chart text-center border-dark ">
                                <div class="card-header card-header-chart">
                                    <ul class="nav nav-pills card-header-pills">
                                        <li class="nav-item">
                                            <NavLink exact className="nav-link nv-link" activeClassName="nav-link active bg-info" to="/university"><i class="fa fa-bar-chart"></i> การกล่าวถึงในวันนี้</NavLink>
                                        </li>
                                        <li class="nav-item">
                                            <NavLink exact className="nav-link nv-link" activeClassName="nav-link active bg-info" to="/university/tweetCount"><i class="fa fa-line-chart"></i> ทวีตแต่ละนาที</NavLink>
                                        </li>
                                        {/* <li class="nav-item">
                                            <NavLink exact className="nav-link nv-link" activeClassName="nav-link active bg-info" to="/retweetPerMinute"><i class="fa fa-area-chart"></i> จำนวนรีทวีตแต่ละนาที</NavLink>
                                        </li> */}
                                        <li class="nav-item">
                                        <NavLink exact className="nav-link nv-link" activeClassName="nav-link active bg-info" to="/university/retweetCount"><i class="fa fa-line-chart"></i> รีทวีตแต่ละนาที</NavLink>
                                        </li>
                                        {/* <li class="nav-item">
                                        <NavLink exact className="nav-link nv-link" activeClassName="nav-link active bg-info" to="/university/Count7Days"><i class="fa fa-bar-chart"></i> จำนวนการกล่าวถึงใน 7 วัน</NavLink>
                                        </li> */}
                                    </ul>
                                </div>
                                <div class="card-body">
                                    <Switch>
                                        <Route exact path="/university" component={BarCount} />
                                        <Route path="/university/tweetCount" component={LineTweet} />
                                        {/* <Route path="/retweetPerMinute" component={LineRetweetPermin} /> */}
                                        <Route path="/university/retweetCount" component={LineRetweet}/>
                                        {/* <Route path="/university/Count7Days" component={Bar7Days}/> */}
                                    </Switch>
                                </div>
                            </div>
                    </Router>
                </Fragment>
            </div>
        );
    }
}

export default chart;