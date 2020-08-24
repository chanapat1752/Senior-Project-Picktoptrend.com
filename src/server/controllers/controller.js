var express = require('express');
var config = require('../config/database');
var mongoose = require('mongoose');
const MongoClient = require('mongodb').MongoClient;
var Graph = require('../models/graphModel');
var connect;
const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

mongoose.connect(config.db, { useNewUrlParser: true }, function (err, con) {
    connect = con
});
mongoose.Promise = global.Promise;
mongoose.connection.once('open', function () {
    console.log('connect');
}).on('error', function (error) {
    console.log('Error is: ', error);
});

module.exports = {
    getTweetData: function (req, res, next) {
        connect.collection('master_data').find({ "trendInDay": {$gte:1} }).sort({ trendInDay: 1 }).toArray(function (err, results) {
            res.setHeader('Content-Type', 'application/json');
            res.json(results);
        });
    },
    getMoreTweet: function (req, res, next) {
        connect.collection('master_data').find({ "timeCreate": { $gte: new Date(req.body.date) } }).sort({ retweet_count: -1 }).toArray(function (err, results) {
            res.setHeader('Content-Type', 'application/json');
            res.json(results);
        });
    },
    getTweetTrends: function (req, res, next) {
        // console.log(req.body.date)
        connect.collection('master_data').find({ "trend": {$gte:1} }).sort({ trend: 1 }).limit(10).toArray(function (err, results) {
            res.setHeader('Content-Type', 'application/json');
            res.json(results);
        });
    },
    getRetweetGraph: function (req, res, next) {
        connect.collection('graph_retweet_UI').find().toArray(function (err, results) {
            res.setHeader('Content-Type', 'application/json');
            res.json(results);
        });
    },
    getTweetGraph: function (req, res, next) {
        connect.collection('graph_tweet_UI').find().toArray(function (err, results) {
            res.setHeader('Content-Type', 'application/json');
            res.json(results);
        });
    },
    getRetweetPerMinGraph: function (req, res, next) {
        connect.collection('graph_retweetpermin_UI').find().toArray(function (err, results) {
            res.setHeader('Content-Type', 'application/json');
            res.json(results);
        });
    },
    getBarCountGraph: function (req, res, next) {
        connect.collection('graph_barcount_UI').find({typeOfGraph:1}).toArray(function (err, results) {
            res.setHeader('Content-Type', 'application/json');
            res.json(results);
        });
    },
    getBarCountGraph2: function (req, res, next) {
        connect.collection('graph_barcount_UI').find({typeOfGraph:2}).toArray(function (err, results) {
            res.setHeader('Content-Type', 'application/json');
            res.json(results);
        });
    },
    getWordClouds: function (req, res, next) {
        connect.collection('wordCloud_UI').find().sort({ value: -1 }).limit(50).toArray(function (err, results) {
            res.setHeader('Content-Type', 'application/json');
            res.json(results);
        });
    },
    getTopTrends: function (req, res, next) {
        connect.collection('wordCloud_UI').find().sort({ value: -1 }).limit(10).toArray(function (err, results) {
            res.setHeader('Content-Type', 'application/json');
            res.json(results);
        });
    },
    getAutoCompleteSearch: function (req, res, next) {
        connect.collection('autocomplete_search').find().toArray(function (err, results) {
            res.setHeader('Content-Type', 'application/json');
            res.json(results);
        });
    },
    getAnnotation: function (req, res, next) {
        // connect.collection('autocomplete_search').find().toArray(function (err, results) {
        //     res.setHeader('Content-Type', 'application/json');
        //     res.json(results);
        // });
        res.setHeader('Content-Type', 'application/json');
        res.json({
            x: 1587930600000,
            strokeDashArray: 1,
            borderColor: '#775DD0',
            borderWidth: 2,
            label: {
              borderColor: '#775DD0',
              style: {
                color: '#fff',
                fontSize:'15px',
                fontFamily: 'Prompt',
                background: '#775DD0',
              },
              text: '#มช',
            }
          });
    },
    getSearchByKeyword: function (req, res) {
        if (req.params.keyword == 'มหาวิทยาลัยธรรมศาสตร์') {
            console.log(req.params.keyword)
            connect.collection('master_data').find({ university: 'Thammasat' }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                res.setHeader('Content-Type', 'application/json');
                res.json(results);
            });
        } else if (req.params.keyword == 'จุฬาลงกรณ์มหาวิทยาลัย') {
            console.log(req.params.keyword)
            connect.collection('master_data').find({ university: 'Chula' }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                res.setHeader('Content-Type', 'application/json');
                res.json(results);
            });
        } else if (req.params.keyword == 'มหาวิทยาลัยมหิดล') {
            console.log(req.params.keyword)
            connect.collection('master_data').find({ university: 'Mahidol' }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                res.setHeader('Content-Type', 'application/json');
                res.json(results);
            });
        }
        else if (req.params.keyword == 'มหาวิทยาลัยเกษตรศาสตร์') {
            console.log(req.params.keyword)
            connect.collection('master_data').find({ university: 'Kasetsart' }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                res.setHeader('Content-Type', 'application/json');
                res.json(results);
            });
        }
        else if (req.params.keyword == 'มหาวิทยาลัยเชียงใหม่') {
            console.log(req.params.keyword)
            connect.collection('master_data').find({ university: 'Chiang Mai' }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                res.setHeader('Content-Type', 'application/json');
                res.json(results);
            });
        }
        else if (req.params.keyword == 'มหาวิทยาลัยขอนแก่น') {
            console.log(req.params.keyword)
            connect.collection('master_data').find({ university: 'Khon Kaen' }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                res.setHeader('Content-Type', 'application/json');
                res.json(results);
            });
        }
        else if (req.params.keyword == 'มหาวิทยาลัยศรีนครินทรวิโรฒ') {
            console.log(req.params.keyword)
            connect.collection('master_data').find({ university: 'Srinakharinwirot' }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                res.setHeader('Content-Type', 'application/json');
                res.json(results);
            });
        }
        else if (req.params.keyword == 'มหาวิทยาลัยมหาสารคาม') {
            console.log(req.params.keyword)
            connect.collection('master_data').find({ university: 'Mahasarakham' }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                res.setHeader('Content-Type', 'application/json');
                res.json(results);
            });
        }
        else if (req.params.keyword == 'มหาวิทยาลัยบูรพา') {
            console.log(req.params.keyword)
            connect.collection('master_data').find({ university: 'Burapha' }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                res.setHeader('Content-Type', 'application/json');
                res.json(results);
            });
        }
        else if (req.params.keyword == 'มหาวิทยาลัยแม่ฟ้าหลวง') {
            console.log(req.params.keyword)
            connect.collection('master_data').find({ university: 'Mae Fah Luang' }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                res.setHeader('Content-Type', 'application/json');
                res.json(results);
            });
        }
        else {
            console.log(req.params.keyword)
            connect.collection('master_data').find({ "hashtags.text": req.params.keyword }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                res.setHeader('Content-Type', 'application/json');
                res.json(results);
            });
        }
    },
    getGraphSearchByKeyword: function (req, res) {
        connect.collection('autocomplete_search').find().toArray(function (err, results) {
            res.setHeader('Content-Type', 'application/json');
            res.json({ name: "test", data: [[10000000000000, 30], [10000000000000, 35], [10000000000000, 31]] });
        });
    },
    getCard: function (req, res) {
        connect.collection('card_UI').find().toArray(function (err, results) {
            res.setHeader('Content-Type', 'application/json');
            res.json(results);
        });
    },
    filterTweet: function (req, res, next) {
        console.log(req.body)
        if (req.body.university.length > 0) {
            if (req.body.sortby === 'no') {
                if (req.body.gte === '') {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({ "university": { $in: req.body.university } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $lte: new Date(req.body.lte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                } else {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $gte: new Date(req.body.gte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $gte: new Date(req.body.gte), $lte: new Date(req.body.lte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                }
            } else if (req.body.sortby === 'retweet') {
                if (req.body.gte === '') {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({ "university": { $in: req.body.university } }).sort({ retweet_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $lte: new Date(req.body.lte) } }).sort({ retweet_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                } else {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $gte: new Date(req.body.gte) } }).sort({ retweet_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $gte: new Date(req.body.gte), $lte: new Date(req.body.lte) } }).sort({ retweet_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                }
            } else if (req.body.sortby === 'favorite') {
                if (req.body.gte === '') {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({ "university": { $in: req.body.university } }).sort({ favorite_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $lte: new Date(req.body.lte) } }).sort({ favorite_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                } else {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $gte: new Date(req.body.gte) } }).sort({ favorite_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $gte: new Date(req.body.gte), $lte: new Date(req.body.lte) } }).sort({ favorite_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                }
            } else if (req.body.sortby === 'current') {
                if (req.body.gte === '') {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({ "university": { $in: req.body.university } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $lte: new Date(req.body.lte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                } else {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $gte: new Date(req.body.gte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $gte: new Date(req.body.gte), $lte: new Date(req.body.lte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                }
            }
        } else {
            if (req.body.sortby === 'no') {
                if (req.body.gte === '') {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({}).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "timeCreate": { $lte: new Date(req.body.lte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                } else {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({ "timeCreate": { $gte: new Date(req.body.gte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "timeCreate": { $gte: new Date(req.body.gte), $lte: new Date(req.body.lte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                }
            } else if (req.body.sortby === 'retweet') {
                if (req.body.gte === '') {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({}).sort({ retweet_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "timeCreate": { $lte: new Date(req.body.lte) } }).sort({ retweet_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                } else {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({ "timeCreate": { $gte: new Date(req.body.gte) } }).sort({ retweet_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "timeCreate": { $gte: new Date(req.body.gte), $lte: new Date(req.body.lte) } }).sort({ retweet_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                }
            } else if (req.body.sortby === 'favorite') {
                if (req.body.gte === '') {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({}).sort({ favorite_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "timeCreate": { $lte: new Date(req.body.lte) } }).sort({ favorite_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                } else {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({ "timeCreate": { $gte: new Date(req.body.gte) } }).sort({ favorite_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "timeCreate": { $gte: new Date(req.body.gte), $lte: new Date(req.body.lte) } }).sort({ favorite_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                }
            } else if (req.body.sortby === 'current') {
                if (req.body.gte === '') {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({}).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "timeCreate": { $lte: new Date(req.body.lte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                } else {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({ "timeCreate": { $gte: new Date(req.body.gte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "timeCreate": { $gte: new Date(req.body.gte), $lte: new Date(req.body.lte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                }
            }
        }

    },
    filterTweetBySearch: function (req, res, next) {
        console.log(req.body)
        if (req.body.university.length > 0) {
            if (req.body.sortby === 'no') {
                if (req.body.gte === '') {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({ "university": { $in: req.body.university } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $lte: new Date(req.body.lte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                } else {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $gte: new Date(req.body.gte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $gte: new Date(req.body.gte), $lte: new Date(req.body.lte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                }
            } else if (req.body.sortby === 'retweet') {
                if (req.body.gte === '') {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({ "university": { $in: req.body.university } }).sort({ retweet_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $lte: new Date(req.body.lte) } }).sort({ retweet_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                } else {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $gte: new Date(req.body.gte) } }).sort({ retweet_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $gte: new Date(req.body.gte), $lte: new Date(req.body.lte) } }).sort({ retweet_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                }
            } else if (req.body.sortby === 'favorite') {
                if (req.body.gte === '') {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({ "university": { $in: req.body.university } }).sort({ favorite_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $lte: new Date(req.body.lte) } }).sort({ favorite_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                } else {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $gte: new Date(req.body.gte) } }).sort({ favorite_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $gte: new Date(req.body.gte), $lte: new Date(req.body.lte) } }).sort({ favorite_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                }
            } else if (req.body.sortby === 'current') {
                if (req.body.gte === '') {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({ "university": { $in: req.body.university } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $lte: new Date(req.body.lte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                } else {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $gte: new Date(req.body.gte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({ "university": { $in: req.body.university }, "timeCreate": { $gte: new Date(req.body.gte), $lte: new Date(req.body.lte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                }
            }
        } else {
            if (req.body.sortby === 'no') {
                if (req.body.gte === '') {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({"hashtags.text": req.body.keyword}).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({"hashtags.text": req.body.keyword, "timeCreate": { $lte: new Date(req.body.lte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                } else {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({"hashtags.text": req.body.keyword, "timeCreate": { $gte: new Date(req.body.gte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({"hashtags.text": req.body.keyword, "timeCreate": { $gte: new Date(req.body.gte), $lte: new Date(req.body.lte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                }
            } else if (req.body.sortby === 'retweet') {
                if (req.body.gte === '') {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({"hashtags.text": req.body.keyword}).sort({ retweet_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({"hashtags.text": req.body.keyword, "timeCreate": { $lte: new Date(req.body.lte) } }).sort({ retweet_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                } else {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({"hashtags.text": req.body.keyword, "timeCreate": { $gte: new Date(req.body.gte) } }).sort({ retweet_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({"hashtags.text": req.body.keyword, "timeCreate": { $gte: new Date(req.body.gte), $lte: new Date(req.body.lte) } }).sort({ retweet_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                }
            } else if (req.body.sortby === 'favorite') {
                if (req.body.gte === '') {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({"hashtags.text": req.body.keyword}).sort({ favorite_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({"hashtags.text": req.body.keyword, "timeCreate": { $lte: new Date(req.body.lte) } }).sort({ favorite_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                } else {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({"hashtags.text": req.body.keyword, "timeCreate": { $gte: new Date(req.body.gte) } }).sort({ favorite_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({"hashtags.text": req.body.keyword, "timeCreate": { $gte: new Date(req.body.gte), $lte: new Date(req.body.lte) } }).sort({ favorite_count: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                }
            } else if (req.body.sortby === 'current') {
                if (req.body.gte === '') {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({"hashtags.text": req.body.keyword}).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({"hashtags.text": req.body.keyword, "timeCreate": { $lte: new Date(req.body.lte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                } else {
                    if (req.body.lte === '') {
                        connect.collection('master_data').find({"hashtags.text": req.body.keyword, "timeCreate": { $gte: new Date(req.body.gte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    } else {
                        connect.collection('master_data').find({"hashtags.text": req.body.keyword, "timeCreate": { $gte: new Date(req.body.gte), $lte: new Date(req.body.lte) } }).sort({ timeCreate: -1 }).toArray(function (err, results) {
                            res.setHeader('Content-Type', 'application/json');
                            res.json(results);
                        });
                    }
                }
            }
        }

    },
};
