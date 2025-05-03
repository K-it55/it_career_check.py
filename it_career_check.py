import streamlit as st

st.set_page_config(page_title="IT適職診断", layout="wide")

st.title("💻 IT業界 適職診断（未経験・キャリアチェンジ対応）")

st.write("以下の20の質問に答えて、あなたに向いているIT職種を診断しましょう。")

# -----------------------------
# 質問と選択肢の定義
# -----------------------------
questions = [
    "新しい技術やツールに触れるのが好きですか？",
    "数字やデータを見て分析するのが好きですか？",
    "他人の課題を聞いて、解決方法を考えるのが好きですか？",
    "アイデアを形にすることにやりがいを感じますか？",
    "パソコン操作やIT製品の設定をよく頼まれますか？",
    "コツコツと作業を続けるのが得意ですか？",
    "論理的に考えるのが好きですか？",
    "チームで協力して進めるのが好きですか？",
    "どちらかというと人と話すより、一人で作業する方が落ち着きますか？",
    "トラブルや問題に対して冷静に対処できる方ですか？",
    "長時間パソコンの前にいてもあまり苦になりませんか？",
    "将来的に在宅勤務やリモートワークを希望しますか？",
    "安定した収入よりも、自分のスキルを伸ばす環境を重視しますか？",
    "成果が数字や結果として見える仕事を好みますか？",
    "今後もIT業界でキャリアアップしたいと考えていますか？",
    "プログラミングの経験（学習含む）はありますか？",
    "Excelなどで関数や簡単な分析を使ったことがありますか？",
    "Webサイトやアプリを作ってみたいと思ったことがありますか？",
    "機械やネットワークの仕組みに興味がありますか？",
    "ITや業務効率化のアイデアを出したことがありますか？"
]

choices = ["まったく当てはまらない", "あまり当てはまらない", "どちらとも言えない", "やや当てはまる", "とても当てはまる"]
answers = []

st.subheader("📝 質問に答えてください")

with st.form("it_diagnosis_form"):
    for i, q in enumerate(questions):
        answer = st.radio(f"{i+1}. {q}", choices, key=f"q{i}")
        answers.append(choices.index(answer))  # 0〜4のスコア
    submitted = st.form_submit_button("診断する")

# -----------------------------
# 診断ロジック（簡易スコアリング）
# -----------------------------
if submitted:
    st.subheader("🔍 診断結果")

    # 各職種に対するスコア（仮ロジック）
    scores = {
        "フロントエンドエンジニア": answers[3] + answers[18],
        "バックエンドエンジニア": answers[6] + answers[0] + answers[15],
        "データサイエンティスト": answers[1] + answers[16] + answers[13],
        "インフラエンジニア": answers[9] + answers[19],
        "ITサポート": answers[4] + answers[2] + (4 - answers[8]),
        "QAエンジニア": answers[5] + answers[9],
        "IT営業・コンサル": answers[2] + answers[7] + (4 - answers[8]),
        "プロダクトマネージャー": answers[7] + answers[14] + answers[12],
    }

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    st.write("あなたに向いている職種は以下の通りです：")

    for i, (job, score) in enumerate(sorted_scores[:3]):
        st.markdown(f"**{i+1}. {job}**（適性スコア: {score}）")

    st.bar_chart({k: v for k, v in sorted_scores})
