import streamlit as st

st.set_page_config(page_title="IT適職診断", layout="centered")

st.title("🔍 IT業界 適職診断（簡易版）")
st.write("以下の質問に答えると、あなたに向いているIT職種がわかります。")

# 質問
q1 = st.radio("Q1. コードを書くのは好きですか？", ["はい", "いいえ", "興味はあるが未経験"])
q2 = st.radio("Q2. チームで作業するのは得意ですか？", ["はい", "どちらともいえない", "一人の方が好き"])
q3 = st.radio("Q3. 細かい作業・設定が得意ですか？", ["はい", "あまり得意でない", "わからない"])
q4 = st.radio("Q4. 興味があるのは？", ["Webサイト制作", "アプリ開発", "データ分析", "ITインフラ", "特に決まっていない"])

if st.button("診断する"):
    st.subheader("🎯 あなたにおすすめの職種")

    if q1 == "はい":
        if q4 == "Webサイト制作":
            st.success("👉 フロントエンドエンジニア")
        elif q4 == "アプリ開発":
            st.success("👉 バックエンドエンジニア")
        elif q4 == "データ分析":
            st.success("👉 データアナリスト / データサイエンティスト")
        else:
            st.success("👉 プログラマー / システムエンジニア")
    elif q1 == "興味はあるが未経験":
        if q4 == "ITインフラ" or q3 == "はい":
            st.success("👉 ITサポート / インフラエンジニア（未経験向き）")
        else:
            st.success("👉 IT事務 / テスター / 学習からスタート")
    else:
        if q2 == "はい":
            st.success("👉 IT営業 / ITコンサルタント")
        else:
            st.success("👉 IT事務 / テクニカルサポート")

    st.write("※ 診断結果は参考としてご活用ください。")