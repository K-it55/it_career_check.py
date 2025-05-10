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

import streamlit as st  
# -----------------------------
# 職種ごとの解説とロードマップ
# -----------------------------
roadmaps = {
    "フロントエンドエンジニア": {
        "学習ステップ": [
            "HTML & CSS を習得し、Webページの基本構造とデザインを理解する。",
            "JavaScript で動的な機能を実装。",
            "React, Vue.js などのフレームワークを学習。",
            "Webpack, Vite などの開発環境を整備。",
            "REST API / GraphQL でデータ取得を習得。",
        ],
        "転職活動": [
            "ポートフォリオサイトを作成し、GitHub でプロジェクトを公開。",
            "JavaScriptのアルゴリズム問題に挑戦。",
        ],
    },
    "バックエンドエンジニア": {
        "学習ステップ": [
            "Python, Java, Node.js などの言語を習得。",
            "Django, Spring Boot, Express などのフレームワークを学習。",
            "SQL / NoSQL を利用したデータベース設計。",
            "RESTful API, GraphQL の構築と運用。",
            "セキュリティ対策（認証・エラー処理など）。",
        ],
        "転職活動": [
            "Webサービスを構築しポートフォリオに追加。",
            "技術ブログを執筆し、開発プロセスを紹介。",
        ],
    },
    "データサイエンティスト": {
        "学習ステップ": [
            "Python / SQL を習得し、データ分析の基礎を学ぶ。",
            "統計学（回帰分析・確率論）の知識を強化。",
            "Scikit-learn, TensorFlow を活用した機械学習を実践。",
            "データ可視化ライブラリ（Matplotlib, Seaborn, Plotly）を使いこなす。",
            "ビッグデータ処理（Spark, Hadoop）を学ぶ。",
        ],
        "転職活動": [
            "Kaggle の課題に挑戦し、GitHub で成果を公開。",
            "データ分析のプレゼンスキルを鍛える。",
        ],
    },
    "インフラエンジニア": {
        "学習ステップ": [
            "Linux の基本操作を習得。",
            "ネットワーク設計（TCP/IP, DNS, VPN）を学ぶ。",
            "クラウド技術（AWS, Azure, GCP）を活用。",
            "コンテナ技術（Docker, Kubernetes）を実践。",
            "CI/CD 環境（Jenkins, GitHub Actions）を構築。",
        ],
        "転職活動": [
            "仮想環境を構築し、クラウドスキルをアピール。",
            "AWS Certified, LPIC などの資格取得を目指す。",
        ],
    },
    "ITサポート": {
        "学習ステップ": [
            "Windows や Mac の基本操作を習得。",
            "ITヘルプデスク業務の知識を学ぶ。",
            "ネットワークやセキュリティの基礎を理解。",
        ],
        "転職活動": [
            "サポート業務の経験を積み、技術ブログを執筆。",
            "問題解決力をアピールする事例を用意。",
        ],
    },
    "QAエンジニア": {
        "学習ステップ": [
            "テスト技法（単体テスト・統合テスト）を学ぶ。",
            "品質管理の基礎を習得。",
            "自動化テスト（Selenium, pytest）を活用。",
            "バグ管理ツール（JIRA, TestRail）の使い方を学ぶ。",
        ],
        "転職活動": [
            "テスト計画を作成し、プロジェクトに適用。",
            "QAのフレームワークを活用した事例をポートフォリオに追加。",
        ],
    },
    "IT営業・コンサル": {
        "学習ステップ": [
            "IT業界の基礎知識を習得。",
            "営業スキル（プレゼン、交渉術）を身につける。",
            "ビジネス戦略・マーケティングを理解。",
        ],
        "転職活動": [
            "プレゼン資料を作成し、実績を強調。",
            "過去の営業事例をポートフォリオとしてまとめる。",
        ],
    },
    "プロダクトマネージャー": {
        "学習ステップ": [
            "プロジェクト管理ツール（JIRA, Trello）を活用。",
            "UX/UI の基礎を学ぶ。",
            "チームマネジメントやアジャイル開発を理解。",
        ],
        "転職活動": [
            "自作アプリやサービスをポートフォリオとして活用。",
            "ユーザーインタビューを行い、改善提案をまとめる。",
        ],
    },
    
}

import streamlit as st

st.title("🎯 職種解説とロードマップ")

# まず職種を選択
selected_job = st.selectbox("職種を選択してください", list(roadmaps.keys()))

# ユーザーが選択した職種のロードマップを表示
if selected_job:
    roadmap_info = roadmaps.get(selected_job, None)
    
    if roadmap_info:
        st.subheader(f"📌 {selected_job} のロードマップ")

        st.markdown("### 🛠 学習ステップ")
        for step in roadmap_info["学習ステップ"]:
            st.write(f"- {step}")

        st.markdown("### 🚀 転職活動")
        for tip in roadmap_info["転職活動"]:
            st.write(f"- {tip}")
    else:
        st.write("ロードマップ情報がありません。")
