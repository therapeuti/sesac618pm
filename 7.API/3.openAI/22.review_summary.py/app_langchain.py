from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

load_dotenv()

# app = Flask(__name__, static_folder='static', static_url_path='static') 원래는 이거
app = Flask(__name__, static_folder='public', static_url_path='')
llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.7)

summary_prompt = PromptTemplate.from_template()
translate_prompt = PromptTemplate.from_template()


summary_chain = summary_prompt | llm
translate_chain = translate_prompt | llm

# 최종 원하는 체인
summary_then_translate_chain = (
    {
        'summary_ko': summary_prompt | llm | RunnableLambda(lambda m: m.content),
        'target_lang_name': RunnablePassthrough()}
        | translate_prompt
        | llm
        | RunnableLambda(lambda m: m.content)
)


reviews = [] # 사용자 후기 저장할 db

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
            'content': f'전체 리뷰 내용 {reviews_text}을 1~2 문장으로 간결하게 요약해서 summary를 키로 하는 딕셔너리 구조에 담아 출력한다.'
        }]
    )

    content = response.choices[0].message.content.strip()
    print('리뷰 요약 내용 : ', content)

    return jsonify({'contents': content, 'averagerating': average_rating})

if __name__=='__main__':
    app.run(debug=True)
