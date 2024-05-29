from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
data =  [
    {
      "profileImg": "1.jpg",
      "profileName": "test",
      "postImg": "2.jpg",
      "postMainTitle": "test",
      "postSubTitle": "test",
      "postDate": "May 05, 2023"
    },
    {
      "profileImg": "3.jpg",
      "profileName": "JinYoung",
      "postImg": "4.jpg",
      "postMainTitle": "새로운 시작",
      "postSubTitle": "희망찬 출발",
      "postDate": "June 12, 2023"
    },
    {
      "profileImg": "5.jpg",
      "profileName": "MinSoo",
      "postImg": "6.jpg",
      "postMainTitle": "여행의 즐거움",
      "postSubTitle": "자연 속으로",
      "postDate": "July 21, 2023"
    },
    {
      "profileImg": "7.jpg",
      "profileName": "HyeJin",
      "postImg": "8.jpg",
      "postMainTitle": "맛있는 음식",
      "postSubTitle": "미식 탐방",
      "postDate": "August 03, 2023"
    },
    {
      "profileImg": "9.jpg",
      "profileName": "JiWon",
      "postImg": "1.jpg",
      "postMainTitle": "즐거운 만남",
      "postSubTitle": "친구와 함께",
      "postDate": "September 15, 2023"
    },
    {
      "profileImg": "2.jpg",
      "profileName": "DongHyun",
      "postImg": "3.jpg",
      "postMainTitle": "운동의 기쁨",
      "postSubTitle": "건강한 생활",
      "postDate": "October 10, 2023"
    },
    {
      "profileImg": "4.jpg",
      "profileName": "SoYeon",
      "postImg": "5.jpg",
      "postMainTitle": "책 읽는 시간",
      "postSubTitle": "지식의 나눔",
      "postDate": "November 22, 2023"
    },
    {
      "profileImg": "6.jpg",
      "profileName": "YoungJae",
      "postImg": "7.jpg",
      "postMainTitle": "산책의 즐거움",
      "postSubTitle": "자연을 느끼다",
      "postDate": "December 19, 2023"
    },
    {
      "profileImg": "8.jpg",
      "profileName": "EunJi",
      "postImg": "9.jpg",
      "postMainTitle": "예술의 세계",
      "postSubTitle": "창의적 표현",
      "postDate": "January 05, 2024"
    },
    {
      "profileImg": "3.jpg",
      "profileName": "test",
      "postImg": "6.jpg",
      "postMainTitle": "test",
      "postSubTitle": "test",
      "postDate": "February 28, 2024"
    }
]

@app.route('/api/post',methods=['GET'])
def get_post():
    return data

if __name__ == '__main__':
    app.run(debug=True)