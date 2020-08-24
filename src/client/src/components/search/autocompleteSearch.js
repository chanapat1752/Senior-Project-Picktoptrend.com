import React from "react";
import { NavLink } from "react-router-dom";
import Autocomplete from 'react-autocomplete';
import './search.css'



class AutoCompleteSearch extends React.Component {
    constructor() {
        super();
        this.state = {
            list: [],
            val: '',
        };
    }
    renderMovieTitle(state, val) {
        return (
            state.name.toLowerCase().indexOf(val.toLowerCase()) !== -1
        );
    }

    componentDidMount() {
        fetch('/getAutoCompleteSearch')
            .then(res => res.json())
            .then(data => this.setState({ list: data })
            );
    }

    render() {
        return (
            <div class="collapse navbar-collapse">
                <form class="form-inline col-12">
                    {/* <input class="form-control mr-sm-2 col-11" type="search" placeholder="ค้นหามหาวิทยาลัยหรือแฮชแท็ก (e.g. ธรรมศาสตร์, #ทีมมธ)" aria-label="Search" /> */}
                    <div class="form-control mr-sm-2 col-11">
                        <div class="autocomplete-wrapper">
                        <Autocomplete
                            value={this.state.val}
                            items={this.state.list}
                            getItemValue={item => item.name}
                            shouldItemRender={this.renderMovieTitle}
                            renderMenu={item => (
                                <div className="dropdown">
                                    {item}
                                </div>
                            )}
                            renderItem={(item, isHighlighted) =>
                                <div className={`item ${isHighlighted ? 'selected-item' : ''}`}>
                                    {item.name}
                                </div>
                            }
                            onChange={(event, val) => this.setState({ val })}
                            onSelect={val => this.setState({ val })}
                            inputProps={{ placeholder: 'ค้นหามหาวิทยาลัยหรือแฮชแท็ก (e.g. ธรรมศาสตร์, #ทีมมธ)' }}
                        />
                        </div>
                    </div>
                        <NavLink to={`/university/${this.state.val.replace("#","")}`} className="btn btn-outline-light" style={{ width: "7%",height:"50px",marginLeft:'4px' }}><i class="fa fa-search fa-lg" aria-hidden="true" style={{marginTop:'13px'}}></i></NavLink>
                </form>
            </div>
        );
    }
}

export default AutoCompleteSearch;