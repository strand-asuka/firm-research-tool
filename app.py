import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ITコンサルファーム 企業研究ツール",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================
# 企業データ
# ============================
COMPANIES = {
    "Dirbato": {
        "name": "株式会社Dirbato",
        "name_en": "Dirbato, Inc.",
        "logo_url": "https://dirbato.co.jp/assets/images/common/logo.svg",
        "website": "https://dirbato.co.jp/",
        "founded": "2018年10月",
        "ceo": "金山 泰英",
        "hq": "東京都港区赤坂9-7-1 ミッドタウン・タワー32階",
        "employees": "1,445名",
        "employees_date": "2025年3月期",
        "revenue": "430億円",
        "revenue_date": "2025年3月期",
        "accent": "#1a73e8",
        "mission": "テクノロジーで世界に喜びを。",
        "vision": "既存のコンサルティングファームの枠組みに捉われず、インキュベーション事業を通じてSDGsを含めた社会課題の解決を目指す「ハイブリッドファーム」",
        "strengths": [
            "IT戦略構築・プロジェクトマネジメント・セキュリティ施策",
            "生成AI関連サービス（内製AI「NeuraBeat」の開発・導入支援）",
            "DX戦略構想〜設計・開発・運用まで一貫支援",
            "Salesforce / SAP / ServiceNow等の導入支援",
            "AI・IoT・ビッグデータ活用の新規事業開発（インキュベーション）",
            "AWS・Salesforce認定パートナー",
        ],
        "culture": [
            "フラットな組織文化 — 役員との距離が近く風通しが良い",
            "若手への大きな裁量 — 20代中盤でマネージャー昇進の実績あり",
            "横のつながり重視 — 部活動・勉強会・ユニットプラン等の交流制度",
            "私服勤務OK — エンジニア出身者が多くカジュアルな雰囲気",
            "月残業20〜30時間（業界内では短い水準）",
            "リモートワーク・フレックスタイム制度あり",
            "D&I（ダイバーシティ＆インクルージョン）推進",
        ],
        "hiring_points": [
            "自ら考え行動・チャレンジができる人材を重視",
            "スキルより「成長したいという意志」が最重要",
            "面接では成長意欲・論理性・共感力・チーム経験を評価",
            "深掘りされる3点：「なぜ転職？」「なぜコンサル？」「なぜDirbato？」",
            "中途入社の約9割がコンサル未経験者（SE・SIer出身が多い）",
        ],
        "selection_flow": "書類選考 → 1次面接（人事面談）→ 最終面接（役員面談）",
        "interview_tips": [
            "「ハイブリッドファーム」構想への共感を具体的に語る",
            "テクノロジーへの関心を過去の行動ベースで示す",
            "経営幹部候補として事業に携わりたい意欲を伝える",
            "面接は和やかな雰囲気 — 逆質問の時間が長い傾向",
        ],
        "growth": {
            "labels": ["2022/3月期", "2023/3月期", "2024/3月期", "2025/3月期"],
            "revenue": [100, 180, 282, 430],
            "employees": [400, 761, 1100, 1445],
        },
    },
    "ノースサンド": {
        "name": "株式会社ノースサンド",
        "name_en": "Northsand, Inc.",
        "logo_url": "https://northsand.co.jp/wp-content/themes/vis/assets/common/img/logo.svg",
        "website": "https://northsand.co.jp/",
        "founded": "2015年7月",
        "ceo": "前田 知紘",
        "hq": "東京都中央区銀座4-12-15 歌舞伎座タワー7F",
        "employees": "1,646名",
        "employees_date": "2025年10月末",
        "revenue": "164.1億円",
        "revenue_date": "2025年1月期",
        "accent": "#0091da",
        "mission": "カッコいい会社を増やす",
        "vision": "世界をデザインする",
        "strengths": [
            "ITコンサルティング（売上の約8割）— IT中期計画策定・M&A後のシステム統合/PMI",
            "ERP/SaaS導入・クラウド移行・データ基盤構築",
            "ビジネスコンサルティング（売上の約2割）— 中期経営計画策定・業務改善",
            "生成AI実装支援・DX戦略立案",
            "戦略立案から実装・定着化まで一気通貫の「ハイブリッド型」",
            "社内ベンチャー支援・ノーコードツール導入",
        ],
        "culture": [
            "徹底した「人」中心の経営思想 — スキルだけでなく人間力を重視",
            "「愛嬌・素直さ・しつこさ」を持つ泥臭い人材を高く評価",
            "フラットな組織文化・透明性の高い評価制度",
            "離職率 約4.8%（業界平均約30%に対して圧倒的に低い）",
            "「働きがいのある会社」8年連続認定",
            "2025年11月 東証グロース市場に上場",
            "8つの行動指針「8 Rules」を全社で共有",
        ],
        "hiring_points": [
            "「人を大切にする」カルチャーへの共感が最重要",
            "素直さ・愛嬌・しつこさがある人物像を求める",
            "「なぜノースサンドなのか？」への明確な回答が必須",
            "5年後・3年後のキャリアプランの具体性を問われる",
            "人柄・価値観の一致が最重視（スキルより人物像）",
        ],
        "selection_flow": "書類選考 → 1次面接（人事面談）→ 最終面接（役員面談）",
        "interview_tips": [
            "8 Rulesを事前に理解し、自分の経験と紐づけて語る",
            "「カッコいい会社を増やす」への共感を具体的に伝える",
            "離職率の低さの背景にあるカルチャーを理解しておく",
            "論理×感情で人を動かした経験を用意すると効果的",
        ],
        "growth": {
            "labels": ["2023/1月期", "2024/1月期", "2025/1月期", "2026/1月期(予)"],
            "revenue": [51, 91.4, 164.1, 250],
            "employees": [600, 1000, 1400, 1646],
        },
    },
    "FLUX": {
        "name": "株式会社FLUX",
        "name_en": "FLUX Inc.",
        "logo_url": "https://flux.jp/wp-content/themes/flux_v3/assets/img/common/logo.svg",
        "website": "https://flux.jp/",
        "founded": "2018年5月",
        "ceo": "永井 元治",
        "hq": "東京都港区赤坂9-7-1 ミッドタウン・タワー24階",
        "employees": "492名",
        "employees_date": "2026年2月末・連結",
        "revenue": "非公開",
        "revenue_date": "累計調達100億円",
        "accent": "#6c5ce7",
        "mission": "日本経済に流れを",
        "vision": "AI時代における企業のベストパートナーになる",
        "strengths": [
            "FLUX Insight — AIコンサルティング（戦略〜実行〜改善の一気通貫）",
            "FLUX AutoStream — AIによるメディア・マーケティング支援",
            "FLUX Agent — AI活用の人材紹介サービス",
            "エンタープライズ企業のAI戦略立案・実装支援",
            "新規事業開発・業務効率化の伴走型コンサルティング",
            "デジタルマーケティング・広告収益最大化",
        ],
        "culture": [
            "プロスポーツチームのような組織 — 常に変化・成長し続ける環境",
            "フラットかつオープン — 雇用形態や年齢に関わらずValuesを体現",
            "多様なバックグラウンド — メルカリ・DeNA・三菱UFJ等からの転職者多数",
            "情報のオープン化 — Slack/Notionで全情報をドキュメント化",
            "成長重視 — 豊富な挑戦機会とフェアな評価制度",
            "社名「FLUX」＝ 絶え間ない変化を意味する",
        ],
        "hiring_points": [
            "自律性・主体性 — 自ら課題設定し取り組む姿勢",
            "変化への柔軟性 — 急成長環境を楽しめるマインド",
            "Mission/Valueへの共感度を重視",
            "前例のない課題への好奇心と思考力",
            "異なる専門知識を持つメンバーとの共創力",
        ],
        "selection_flow": "書類選考 → 1次面接（人事面談）→ 最終面接（役員面談）",
        "interview_tips": [
            "5つのValues（80/20, Quick and Small等）を理解し自分の言葉で語る",
            "AIやテクノロジーへの関心を具体的エピソードで示す",
            "スタートアップ環境での変化を楽しめる姿勢をアピール",
            "「日本経済に流れを」への自分なりの解釈を用意",
        ],
        "growth": {
            "labels": ["2022年", "2023年", "2024年", "2025年"],
            "revenue": [None, None, None, None],
            "employees": [120, 220, 350, 492],
        },
    },
    "アクティヴァーチ": {
        "name": "株式会社アクティヴァーチ・コンサルティング",
        "name_en": "Activarch Consulting, Inc.",
        "logo_url": "https://activarch.co.jp/home/wp-content/themes/activarch/assets/images/common/logo_activarch.svg",
        "website": "https://activarch.co.jp/",
        "founded": "2020年11月",
        "ceo": "福井 康司",
        "hq": "東京都港区虎ノ門2-6-1 虎ノ門ヒルズステーションタワー39階",
        "employees": "約200〜230名",
        "employees_date": "2026年時点",
        "revenue": "約11.1億円",
        "revenue_date": "2024年10月期",
        "accent": "#f39c12",
        "mission": "Activate your potential — 無限の可能性を解き放つ",
        "vision": "人と人をつなぐ「架け橋（arch）」となり、クライアントの可能性を最大限に引き出す",
        "strengths": [
            "ITコンサルティング — IT戦略立案・業務分析・要件定義・PMO支援",
            "DXコンサルティング — DX企画立案・AI/IoT実装支援",
            "AIコンサルティング — AI戦略策定〜セキュアな実装・内製化",
            "戦略/インキュベーション — 全社・事業戦略策定・CIOアドバイザリ",
            "現場密着型のハンズオン型コンサルティングが特徴",
            "セキュリティ対策支援",
        ],
        "culture": [
            "フランクでフラットなカルチャー — 殺伐とした競争文化ではないオープンな環境",
            "若くエネルギッシュ — 社員同士のコミュニケーションが活発",
            "ハイブリッド勤務・月残業20時間以内（業界トップクラスの働きやすさ）",
            "絶対評価制度 — 年次/役職に関係なくスキルと実績で評価",
            "大手外資コンサル・野村證券等出身者が経営陣を構成",
            "コアバリュー：Close Communication / Pursuing Quality / Fast & Flexible",
        ],
        "hiring_points": [
            "コミュニケーション能力 — 課題を引き出し整理するスキル",
            "向上心・主体的な学習姿勢を最重視",
            "新しい技術や情報を常にキャッチアップする姿勢",
            "ソリューションを伝えてプロジェクトを動かす力",
            "コンサル未経験者でも積極採用",
        ],
        "selection_flow": "書類選考 → 1次面接（人事面談）→ 最終面接（役員面談）",
        "interview_tips": [
            "コアバリュー3つを理解し、過去の行動で体現できた例を用意",
            "ハンズオン型コンサルへの共感を自分の言葉で語る",
            "急成長企業で挑戦したい理由を明確に",
            "働き方だけでなく成長意欲もアピール",
        ],
        "growth": {
            "labels": ["2022/10月期", "2023/10月期", "2024/10月期", "2025/10月期(予)"],
            "revenue": [2.3, 6.12, 11.1, 20],
            "employees": [30, 80, 143, 230],
        },
    },
    "ストラテジーテック": {
        "name": "株式会社ストラテジーテック・コンサルティング",
        "name_en": "StrategyTec Consulting, Inc.",
        "logo_url": "https://strategy-tec.com/common/logo/logo1.svg",
        "website": "https://strategy-tec.com/",
        "founded": "2019年11月",
        "ceo": "三浦 大地",
        "hq": "東京都中央区八重洲2-2-1 東京ミッドタウン八重洲 セントラルタワー8階",
        "employees": "約222名",
        "employees_date": "2025年11月時点",
        "revenue": "54億円",
        "revenue_date": "2023年10月期",
        "accent": "#e74c3c",
        "mission": "変革を通じて、より良い未来を創る",
        "vision": "世界中の叡智を集結し、新たなるイノベーションを描き続けるデジタルイノベーションプラットフォーマー",
        "strengths": [
            "戦略・ITコンサルティング — DX推進・新規事業開発（事業の約40%が戦略案件）",
            "AI・機械学習・IoT・5G通信技術の最先端テクノロジー",
            "サイバーセキュリティ・クラウド（AWS/Azure/Google）",
            "自社プロダクト「ContactEARTH」「セルキャリ」等のSaaS事業",
            "地方創生事業 — 自治体連携の地域経済活性化・スマートシティ構想",
            "弘前・秋田・仙台に地方拠点を展開",
        ],
        "culture": [
            "フラットな組織 — タイトルや経験に関わらずフラットに接する文化",
            "ワンプール制 — 領域を限定せず様々な業界・テーマを経験可能",
            "チャレンジ精神重視 — 自分の枠にとらわれず手を挙げる人が多い",
            "平均年齢34〜35歳 — BIG4・大手外資系出身者も在籍",
            "書籍執筆や新規プロダクト開発など多様な挑戦機会あり",
            "個を尊重するカルチャー",
        ],
        "hiring_points": [
            "論理的思考力とコミュニケーション能力（ベーススキル）",
            "IT素養 — SIer出身者・SE経験者のニーズが高い",
            "人柄重視 — 「Be Attractive（人として魅力的であろう）」",
            "主体性・積極性 — 最新トレンドを自ら学ぶ姿勢",
            "応募条件：大卒以上、コンサル経験 or 経営企画1年以上",
        ],
        "selection_flow": "書類選考 → 1次面接（人事面談）→ 最終面接（役員面談）",
        "interview_tips": [
            "戦略案件40%という強みに魅力を感じる理由を具体的に",
            "ワンプール制で幅広い経験を積みたい意欲をアピール",
            "地方創生事業やSaaS事業など独自路線への関心を示す",
            "行動指針「Be Attractive」「Work Positively」と自分の経験を紐づける",
        ],
        "growth": {
            "labels": ["2021/10月期", "2022/10月期", "2023/10月期", "2024年(推定)"],
            "revenue": [14.5, 34, 54, 70],
            "employees": [60, 120, 184, 222],
        },
    },
}

# ============================
# CSS - ホワイトベース
# ============================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;600;700;900&display=swap');

.stApp {
    background: #f5f6fa;
    color: #333;
    font-family: 'Noto Sans JP', sans-serif;
}
.block-container { padding: 1rem 2rem 2rem; max-width: 1100px; margin: 0 auto; }
header, footer, #MainMenu { visibility: hidden; }
section.stMain { overflow: auto !important; }
[data-testid="stAppViewContainer"] { overflow: auto !important; }
[data-testid="stSidebar"] { display: none; }
[data-testid="stSidebarCollapsedControl"] { display: none; }

/* ──── Header ──── */
.app-header {
    background: #111;
    padding: 16px 0 14px;
    margin: -1rem -2rem 0 -2rem;
    text-align: center;
}
.app-header .brand {
    font-family: 'Georgia', 'Times New Roman', serif;
    font-size: 1.3rem;
    font-weight: 400;
    color: #fff;
    letter-spacing: 6px;
    margin: 0;
}
.app-sub-header {
    background: #fff;
    border-bottom: 1px solid #e0e0e0;
    padding: 14px 0;
    margin: 0 -2rem 24px -2rem;
    text-align: center;
}
.app-sub-header h1 {
    font-size: 1.3rem;
    font-weight: 700;
    color: #222;
    margin: 0;
}
.app-sub-header p {
    font-size: 0.82rem;
    color: #888;
    margin: 4px 0 0;
}

/* ──── Company Card (top page) ──── */
.company-card {
    background: #fff;
    border: 1px solid #e8e8e8;
    border-radius: 12px;
    padding: 24px 16px 16px;
    text-align: center;
    transition: box-shadow 0.2s, transform 0.15s;
    min-height: 180px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}
.company-card:hover {
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    transform: translateY(-2px);
}
.company-card img {
    max-height: 40px;
    max-width: 140px;
    object-fit: contain;
    margin-bottom: 12px;
}
.company-card .card-name {
    font-weight: 700;
    font-size: 0.95rem;
    color: #222;
    margin-bottom: 2px;
}
.company-card .card-sub {
    font-size: 0.72rem;
    color: #999;
}

/* ──── Detail page ──── */
.detail-header {
    background: #fff;
    border: 1px solid #e8e8e8;
    border-radius: 14px;
    padding: 32px;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 28px;
}
.detail-header img {
    max-height: 50px;
    max-width: 180px;
    object-fit: contain;
}
.detail-header .info .name {
    font-size: 1.6rem;
    font-weight: 700;
    color: #222;
}
.detail-header .info .name-en {
    font-size: 0.82rem;
    color: #999;
    margin-top: 2px;
}
.detail-header .info .mission-q {
    margin-top: 10px;
    font-size: 0.95rem;
    color: #555;
    font-style: italic;
    padding-left: 12px;
    border-left: 3px solid #1a73e8;
}

/* ──── KPI row ──── */
.kpi-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    margin-bottom: 24px;
}
.kpi-card {
    background: #fff;
    border: 1px solid #e8e8e8;
    border-radius: 10px;
    padding: 18px 14px;
    text-align: center;
}
.kpi-label {
    font-size: 0.7rem;
    color: #999;
    letter-spacing: 0.5px;
    margin-bottom: 4px;
}
.kpi-value {
    font-size: 1.35rem;
    font-weight: 700;
    color: #222;
}
.kpi-sub {
    font-size: 0.68rem;
    color: #bbb;
    margin-top: 2px;
}

/* ──── Section ──── */
.section-box {
    background: #fff;
    border: 1px solid #e8e8e8;
    border-radius: 12px;
    padding: 24px;
    margin-bottom: 18px;
}
.section-heading {
    font-size: 1rem;
    font-weight: 700;
    color: #222;
    margin-bottom: 14px;
    padding-bottom: 8px;
    border-bottom: 2px solid #1a73e8;
    display: inline-block;
}

/* ──── List items ──── */
.list-item {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    padding: 7px 0;
    font-size: 0.88rem;
    color: #444;
    line-height: 1.6;
}
.list-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    margin-top: 8px;
    flex-shrink: 0;
}

/* ──── Tip cards ──── */
.tip-item {
    background: #f8f9ff;
    border-left: 3px solid;
    border-radius: 0 8px 8px 0;
    padding: 10px 14px;
    margin-bottom: 8px;
    font-size: 0.86rem;
    color: #444;
    line-height: 1.6;
}

/* ──── Flow badge ──── */
.flow-badge {
    display: inline-block;
    background: #f0f4ff;
    border: 1px solid #d0dcf0;
    border-radius: 20px;
    padding: 6px 18px;
    font-size: 0.82rem;
    color: #1a73e8;
}

/* ──── Link button ──── */
.site-link {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 8px 20px;
    border-radius: 8px;
    background: #1a73e8;
    color: #fff;
    text-decoration: none;
    font-weight: 600;
    font-size: 0.85rem;
    transition: background 0.2s;
}
.site-link:hover { background: #1557b0; color: #fff; }

/* ──── Streamlit overrides ──── */
.stButton > button {
    background: #1a73e8;
    color: #fff;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    padding: 8px 0;
    transition: background 0.2s;
}
.stButton > button:hover {
    background: #1557b0;
    color: #fff;
    border: none;
}
/* back button */
.back-button > button {
    background: #fff !important;
    color: #666 !important;
    border: 1px solid #ddd !important;
}
.back-button > button:hover {
    background: #f5f5f5 !important;
    color: #333 !important;
}

@media (max-width: 768px) {
    .kpi-row { grid-template-columns: repeat(2, 1fr); }
    .detail-header { flex-direction: column; text-align: center; }
}
</style>
""", unsafe_allow_html=True)


# ============================
# 状態管理
# ============================
if "selected_company" not in st.session_state:
    st.session_state.selected_company = None


def show_company(key):
    st.session_state.selected_company = key


def go_back():
    st.session_state.selected_company = None


# ============================
# トップページ
# ============================
def render_landing():
    st.markdown("""
    <div class="app-header">
        <div class="brand">STRAND PARTNERS</div>
    </div>
    <div class="app-sub-header">
        <h1>ITコンサルファーム 企業研究ツール</h1>
        <p>面接前に押さえておくべきポイントを網羅的にチェック</p>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(len(COMPANIES))
    for i, (key, data) in enumerate(COMPANIES.items()):
        with cols[i]:
            st.markdown(f"""
            <div class="company-card">
                <img src="{data['logo_url']}" alt="{key}"
                     onerror="this.style.display='none';this.nextElementSibling.style.display='block';">
                <div style="display:none; font-size:1.2rem; font-weight:900; color:{data['accent']}; margin-bottom:12px;">{key}</div>
                <div class="card-name">{key}</div>
                <div class="card-sub">{data['name']}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("詳細を見る", key=f"btn_{key}", use_container_width=True):
                show_company(key)
                st.rerun()


# ============================
# 企業詳細ページ（一覧表示）
# ============================
def render_company(key):
    d = COMPANIES[key]
    accent = d["accent"]

    # Brand header
    st.markdown("""
    <div class="app-header">
        <div class="brand">STRAND PARTNERS</div>
    </div>
    <div style="background:#fff; border-bottom:1px solid #e0e0e0; padding:10px 0; margin:0 -2rem 20px -2rem; text-align:center;">
        <span style="font-size:0.9rem; font-weight:600; color:#222;">ITコンサルファーム 企業研究ツール</span>
    </div>
    """, unsafe_allow_html=True)

    # Back button
    st.markdown('<div class="back-button">', unsafe_allow_html=True)
    if st.button("← 企業一覧に戻る", key="back"):
        go_back()
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # Header with logo
    st.markdown(f"""
    <div class="detail-header">
        <img src="{d['logo_url']}" alt="{key}"
             onerror="this.style.display='none'">
        <div class="info">
            <div class="name">{d['name']}</div>
            <div class="name-en">{d['name_en']}</div>
            <div class="mission-q">「{d['mission']}」</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # KPI cards
    st.markdown(f"""
    <div class="kpi-row">
        <div class="kpi-card">
            <div class="kpi-label">従業員数</div>
            <div class="kpi-value">{d['employees']}</div>
            <div class="kpi-sub">{d['employees_date']}</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">売上高</div>
            <div class="kpi-value">{d['revenue']}</div>
            <div class="kpi-sub">{d['revenue_date']}</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">設立</div>
            <div class="kpi-value" style="font-size:1.1rem;">{d['founded']}</div>
            <div class="kpi-sub">代表: {d['ceo']}</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-label">本社</div>
            <div class="kpi-value" style="font-size:0.8rem; line-height:1.4;">{d['hq']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── ビジョン・ミッション ──
    st.markdown(f"""
    <div class="section-box">
        <div class="section-heading" style="border-color:{accent};">ビジョン・ミッション</div>
        <div style="margin-bottom:10px;">
            <span style="font-size:0.75rem; color:#999; font-weight:600;">VISION</span>
            <p style="color:#333; font-size:0.92rem; margin:4px 0 0; line-height:1.7;">{d['vision']}</p>
        </div>
        <div>
            <span style="font-size:0.75rem; color:#999; font-weight:600;">MISSION</span>
            <p style="color:#222; font-size:1.1rem; font-weight:700; margin:4px 0 0;">「{d['mission']}」</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── 得意領域 ──
    st.markdown(f'<div class="section-box"><div class="section-heading" style="border-color:{accent};">得意領域・サービス</div>', unsafe_allow_html=True)
    for item in d["strengths"]:
        st.markdown(f'<div class="list-item"><div class="list-dot" style="background:{accent};"></div>{item}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ── 社風・カルチャー ──
    st.markdown(f'<div class="section-box"><div class="section-heading" style="border-color:{accent};">社風・カルチャー</div>', unsafe_allow_html=True)
    for item in d["culture"]:
        st.markdown(f'<div class="list-item"><div class="list-dot" style="background:{accent};"></div>{item}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ── 採用で見ているポイント ──
    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown(f'<div class="section-box"><div class="section-heading" style="border-color:{accent};">採用で見ているポイント</div>', unsafe_allow_html=True)
        for p in d["hiring_points"]:
            st.markdown(f'<div class="list-item"><div class="list-dot" style="background:{accent};"></div>{p}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="margin-top:14px;"><span style="font-size:0.75rem; color:#999;">選考フロー</span><div class="flow-badge" style="margin-top:6px;">{d["selection_flow"]}</div></div></div>', unsafe_allow_html=True)

    with col_r:
        st.markdown(f'<div class="section-box"><div class="section-heading" style="border-color:{accent};">面接対策のヒント</div>', unsafe_allow_html=True)
        for t in d["interview_tips"]:
            st.markdown(f'<div class="tip-item" style="border-left-color:{accent};">{t}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ── 成長推移 ──
    growth = d["growth"]
    st.markdown(f'<div class="section-box"><div class="section-heading" style="border-color:{accent};">成長推移</div></div>', unsafe_allow_html=True)

    col_chart1, col_chart2 = st.columns(2)
    with col_chart1:
        revenue_data = growth["revenue"]
        if any(v is not None for v in revenue_data):
            st.markdown("**売上高推移（億円）**")
            chart_df = pd.DataFrame({
                "期": growth["labels"],
                "売上高": [v if v is not None else 0 for v in revenue_data],
            }).set_index("期")
            st.bar_chart(chart_df, color=accent)
        else:
            st.info("売上高データは非公開です")

    with col_chart2:
        st.markdown("**従業員数推移（名）**")
        emp_df = pd.DataFrame({
            "期": growth["labels"],
            "従業員数": growth["employees"],
        }).set_index("期")
        st.bar_chart(emp_df, color=accent)

    # Website link
    st.markdown(f'<a href="{d["website"]}" target="_blank" class="site-link">🌐 公式サイトを見る</a>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)


# ============================
# メイン
# ============================
if st.session_state.selected_company is None:
    render_landing()
else:
    render_company(st.session_state.selected_company)
