from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

# app = Flask(__name__, static_folder='static', static_url_path='static') 원래는 이거
app = Flask(__name__, static_folder='public', static_url_path='')

openai = OpenAI()


reviews = [] # 사용자 후기 저장할 dv

@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    rating = data.get('rating')
    opinion = data.get('opinion')

    print(rating, opinion)
    reviews.append({'rating': rating, 'opinion': opinion})
    print(reviews)
    return jsonify(reviews)


@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    # target_lang = request.args.get('lang', 'ko')
    # print(target_lang)

    # response = openai.chat.completions.create(
    #     model='gpt-3.5-turbo', 
    #     messages=[
    #         {'role':'system', 'content': '당신은 번역가입니다. 사용자가 요청한 언어로 번역을 해주세요'},
    #         {
    #         'role': 'user',
    #         'content': f'1. {target_lang} 언어로 {reviews}를 번역해줘.'
    #     }]
    # )

    # content = response.choices[0].message.content.strip()
    # print(content)


    return jsonify(reviews)


@app.route('/api/ai-summary')
def get_ai_summary():
    target_lang = request.args.get('lang', 'ko')
    print(target_lang)

    if not reviews:
        return jsonify({'summary': '리뷰가 없습니다.', 'averagerating': 0.0})

    average_rating = sum(r['rating'] for r in reviews) / len(reviews)
    reviews_text = '\n'.join([f'별점: {r["rating"]}, 리뷰내용: {r["opinion"]}' for r in reviews])
    print('리뷰내용 통합 : ')
    print(reviews_text)


    response = openai.chat.completions.create(
        model='gpt-4o', 
        messages=[
            {
            'role': 'user',
            'content': f'{reviews_text}을 한 문장으로 간결하게 요약하고 {target_lang}으로 번역해줘.'
        }]
    )

    content = response.choices[0].message.content.strip()
    print('리뷰 요약 내용 : ', content)

    return jsonify({'contents': content, 'averagerating': average_rating})

if __name__=='__main__':
    app.run(debug=True)
