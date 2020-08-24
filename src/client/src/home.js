import React from 'react';
import ChardBox from './components/chart/chartBox';
import TrendsBox from './components/trends/TrendsBox';
import WordCloud from './components/wordCloud/wordCloud';
import Cards from './components/trends/cards';
import TrendsList from './components/trends/HashtagTrends';
import TweetBox from './components/tweet/TweetBox';
// import Fade from 'react-reveal/Fade';

import "./styles.css";

function FadeInSection(props) {
  const [isVisible, setVisible] = React.useState(false);
  const domRef = React.useRef();
  React.useEffect(() => {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => setVisible(entry.isIntersecting));
    });
    observer.observe(domRef.current);
  }, []);
  return (
    <div
      className={`fade-in-section ${isVisible ? "is-visible" : ""}`}
      ref={domRef}
    >
      {props.children}
    </div>
  );
}

function Home() {
  return (
    <div>
      <Cards />
      <div class="row" style={{ marginLeft: "3px", marginRight: "3px"}}>
        <div class="col-xl-9 col-sm-12" style={{ marginTop: "10px" }}>
          <ChardBox />
        </div>
        <div class="col-xl-3 col-sm-12" style={{ marginTop: "10px" }}>
          <TrendsBox />
        </div>
      </div>
      <FadeInSection>
        <div class="row" style={{ marginLeft: "3px", marginRight: "3px"}}>
          <div class="col-xl-3 col-sm-12" style={{ marginTop: "20px" }}>
            <TrendsList />
          </div>
          <div class="col-xl-9 col-sm-12" style={{ marginTop: "20px" }}>
            <WordCloud />
          </div>
        </div>
      </FadeInSection>
      <FadeInSection>
        <TweetBox />
      </FadeInSection>
      <br />
    </div>
  );
}

export default Home;