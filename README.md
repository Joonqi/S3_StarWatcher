# StarWatcher
[Star Watcher](https://www.notion.so/S3_Star-Watcher-120e7a6350ce4ff699caf96c55015987)

KOSPI와 NASDAQ에 상장된 주식 정보로 나만의 워치리스트를 구성하고 각 기업에 대한 주가 추이,  
머신러닝을 통한 매매 추천 기능을 하는 웹 애플리케이션을 개발했습니다.

Deployment : [🔗https://app-star-watcher.herokuapp.com/](https://app-star-watcher.herokuapp.com/)

- Flask, PostgreSQL을 활용하여 CRUD 기능의 웹 애플리케이션을 개발
- pmdarima 라이브러리의 ARIMA 모델을 이용하여 추천 기능 구현
- Heroku 서버를 통해 배포

## 세부 기능
Star Watcher는 3가지 탭으로 기능이 구분되어 있습니다.
1. Watchlist<br>
관심 종목을 검색하고 리스트에 추가하는 페이지입니다.  
NASDAQ, KOSPI 상장 종목들을 기업 이름이나 종목코드를 통해 검색할 수 있습니다.  
각 종목들에 메모를 작성해서 등록할 수 있습니다.  
한국 기업의 경우 이름은 영어로 작성해야하고 코드는 6자리코드에 '.KS'를 붙여야 합니다.<br> (eg. 'Samsung SDI' or '006405.KS')  

2. Graphics<br>
관심종목에 등록된 기업의 최근 주가 데이터를 그래프로 나타내는 페이지입니다.  
그래프는 2015년 이후 매 개장일의 종가가 그려집니다
3. Predict<br>
리스트에 등록된 종목의 다음날 상승률을 예측을 확인할 수 있는 페이지입니다.  
예측은 ARIMA 회귀 모델을 통해 이루어집니다.  
NASDAQ 기업의 경우 Yahoo Finance 에 등록된 Recommendation 정보도 확인할 수 있습니다.
_________
inner database schema:
![Dataframe_Schema](https://user-images.githubusercontent.com/83646259/127981228-b21ecffc-a0dd-484a-bb24-9a0c16768d52.png)
