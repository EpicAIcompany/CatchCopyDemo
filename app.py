import streamlit as st
import os
import openai
from dotenv import load_dotenv

load_dotenv(".env")

openai.api_key = os.getenv('opn_api')

def generate_text(data):
    prompt = f"""
        次の情報に基づいて、広告のキャッチコピーを5個生成してください。

        商品サービスの概要: {data["product_service"]}
        広告の訴求軸: {data["appeal"]}
        商品サービスの特徴・強み: {data["features"]}
        ターゲットのニーズ・悩み・問題: {data["needs_challenges"]}
        解決策への期待: {data["solution_expectations"]}
        ターゲットの関心ごと・優先事項: {data["interests_priorities"]}
        メディア利用傾向: {data["media_usage"]}
        コピーのテーマ: {data["theme"]}
        アピールしたいポイント: {data["appeal_points"]}
        コピーの例: {data["copy_examples"]}

        これらの情報をもとに効果的なキャッチコピーを5個作成してください。"""

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=1000,
        temperature=0
    )
    return response.choices[0].text.strip()

# カスタムヘッダーのためのCSS
fixed_header_html = """
<style>
    .fixed-header {
        position: fixed; /* ヘッダーを固定 */
        top: 45px; /* ページの上部から45pxの位置に配置 */
        left: 0; /* ページの左端に配置 */
        width: 100%; /* 幅を画面全体に拡張 */
        background-color: white; /* ヘッダーの背景色 */
        color: black; /* テキスト色 */
        font-size: 24px;
        text-align: left; /* テキストを左寄せ */
        padding: 10px 20px; /* 上下のパディングと左右のパディング */
        border-bottom: 2px solid rgba(128, 128, 128, 0.5); /* 下端に灰色の線を追加 */
        z-index: 999; /* 他の要素より前面に表示 */
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* 下端に影を追加 */
    }

</style>

<div class="spacer"></div>
    <div class="fixed-header">
        <p style="font-size: 24px;">EpicAI：キャッチコピー自動生成デモ</p>
    </div>
<div class="spacer"></div>
"""

st.markdown(fixed_header_html, unsafe_allow_html=True)

css_style = """
<style>
.title-style {
    font-size: 26px;
    font-weight: bold;
    color: black;
    padding-left: 10px;
    border-left: 5px solid orange;
}

.required-label {
    color: red;
    font-weight: bold;
}

.help-icon {
    color: gray;
    font-size: 16px;
}

input[type="text"] {
    background-color: white;
    border: 1px solid #cccccc;
}
.small-text {
    font-size: smaller;
    color: gray;
    margin-bottom: 0px; /* 余白を減らす */
}
</style>
"""


# Streamlitのmarkdownでカスタムスタイルを適用
st.markdown(css_style, unsafe_allow_html=True)

# 商品・サービスの決定
st.markdown('<p class="title-style">1. 商品・サービスの設定</p>', unsafe_allow_html=True)
st.write("商品・サービスについての詳細をお書きください。")
# product_service = st.text_input("商品サービスの概要", "スカウト型転職サービス")
# appeal = st.text_input("広告の訴求軸", "仕事と育児を両立できる転職")
# features = st.text_input("商品・サービスの特徴・強み", "業界専門家によるカウンセリング")
st.markdown("""
    商品サービスの概要
    <br>
    <p class="small-text">ex: スカウト型転職サービス</p>
""", unsafe_allow_html=True)
product_service = st.text_input("", "")
# 広告の訴求軸
st.markdown("""
    広告の訴求軸
    <br>
    <p class="small-text">ex: 仕事と育児を両立できる転職</p>
""", unsafe_allow_html=True)
appeal = st.text_input("", "", key="appeal_input")

# 商品・サービスの特徴・強み
st.markdown("""
    商品・サービスの特徴・強み
    <br>
    <p class="small-text">ex: 業界専門家によるカウンセリング</p>
""", unsafe_allow_html=True)
features = st.text_input("", "", key="features_input")


# ターゲットの選定
st.markdown('<p class="title-style">2. ターゲットの選定</p>', unsafe_allow_html=True)
# product_service = st.text_input("", "", key="product_service_input")
st.write("ターゲットについての詳細をお書きください。")

# カスタムラベルとヘルプアイコン
st.markdown('<p>ターゲットの性別 <span class="required-label">[必須]</span> <span class="help-icon">?</span></p>', unsafe_allow_html=True)

# 性別の選択

# 性別選択用の状態を保持する
if 'selected_gender' not in st.session_state:
    st.session_state['selected_gender'] = None

# 3つのボタンを表示
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("男性"):
        st.session_state['selected_gender'] = "男性"
with col2:
    if st.button("女性"):
        st.session_state['selected_gender'] = "女性"
with col3:
    if st.button("その他"):
        st.session_state['selected_gender'] = "その他"

# # 選択された性別を表示
# if st.session_state['selected_gender'] is not None:
#     st.write(f"選択された性別: {st.session_state['selected_gender']}")


# st.markdown('<p>ターゲットの年齢 <span class="required-label">[必須]</span> <span class="help-icon">?</span></p>', unsafe_allow_html=True)

# age = st.slider("ターゲットの年齢", 18, 65, 30)

# カスタムラベルでマークダウンを使用
st.markdown('<p>ターゲットの年齢 <span class="required-label">[必須]</span> <span class="help-icon">?</span></p>', unsafe_allow_html=True)

# スライダーのラベルを空にして、カスタムラベルを使用
age = st.slider("", 18, 65, 30)
challenges = st.text_input("ターゲットの悩み・課題")

# ペルソナの決定
st.markdown('<p class="title-style">3. ペルソナの決定</p>', unsafe_allow_html=True)
st.write("ペルソナを具体的にお書きください。")

# ターゲットのニーズ・悩み・問題、現状の不満や課題
st.markdown("""
    ターゲットのニーズ・悩み・問題、現状の不満や課題
    <br>
    <p class="small-text">ex: ワークライフバランスの改善を求めている</p>
""", unsafe_allow_html=True)
needs_challenges = st.text_input("", "", key="needs_challenges_input")

# 解決策への期待
st.markdown("""
    解決策への期待
    <br>
    <p class="small-text">ex: 柔軟な勤務時間の提供</p>
""", unsafe_allow_html=True)
solution_expectations = st.text_input("", "", key="solution_expectations_input")

# ターゲットの関心ごと・優先事項
st.markdown("""
    ターゲットの関心ごと・優先事項
    <br>
    <p class="small-text">ex: キャリアアップ、家族との時間</p>
""", unsafe_allow_html=True)
interests_priorities = st.text_input("", "", key="interests_priorities_input")

# メディア利用傾向
st.markdown("""
    メディア利用傾向
    <br>
    <p class="small-text">ex: ソーシャルメディアでの情報収集が多い</p>
""", unsafe_allow_html=True)
media_usage = st.text_input("", "", key="media_usage_input")
# 制約条件
st.markdown('<p class="title-style">4. コピーのテーマ</p>', unsafe_allow_html=True)
st.write("コピーのテーマ、方向性についてお書きください。")
# テーマ設定
st.markdown("""
    コピーのテーマ、方向性
    <br>
    <p class="small-text">ex: キャリア志向の強い親御さん向けの転職支援</p>
""", unsafe_allow_html=True)
theme = st.text_input("", "", key="theme_input")

# アピールしたいポイント
st.markdown("""
    アピールしたいポイント
    <br>
    <p class="small-text">ex: 仕事と育児の両立できる職場</p>
""", unsafe_allow_html=True)
appeal_points = st.text_input("", "", key="appeal_points_input")

# コピーの例
st.markdown("""
    コピーの例
    <br>
    <p class="small-text">ex: 「家庭も、キャリアも、あなたのスタイルで」</p>
""", unsafe_allow_html=True)
copy_examples = st.text_input("", "", key="copy_examples_input")
# コピーライティング生成
st.markdown('<p class="title-style">5. コピーライティング生成</p>', unsafe_allow_html=True)
if st.button("キャッチコピーを生成"):
    data = {
        "product_service": product_service,
        "appeal": appeal,
        "features": features,
        "needs_challenges": needs_challenges,
        "solution_expectations": solution_expectations,
        "interests_priorities": interests_priorities,
        "media_usage": media_usage,
        "theme": theme,
        "appeal_points": appeal_points,
        "copy_examples": copy_examples
    }
    generated_text = generate_text(data)
    st.write(generated_text)