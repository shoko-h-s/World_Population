import pandas as pd
import streamlit as st

# 1. ページの基本設定
st.set_page_config(
    page_title="世界人口データビューア (1960-2025)", page_icon="📈", layout="wide"
)

st.title("📈 世界人口データビューア (1960-2025)")
st.write(
    "1960年から2025年までの5年ごとの人口データを使って、気になる国々の推移を比較・確認できるアプリです。"
)


# 2. データの読み込み＆前処理（キャッシュを使って効率化）
@st.cache_data
def load_data():
    df = pd.read_csv("df_quinquennial.csv")
    return df


try:
    df_quinquennial = load_data()
except FileNotFoundError:
    st.error(
        "データファイルが見つかりません。"
    )
    st.stop()

# 3. サイドバー：国や表示スタイルの選択
st.sidebar.header("🎛️ 表示設定")

# 国名のリストを取得
country_list = df_quinquennial["Country Name"].tolist()

# デフォルトで選択しておく国（例：日本、アメリカ、中国、インド）
default_countries = [
    country
    for country in ["Japan", "United States", "China", "India"]
    if country in country_list
]

# マルチセレクトボックスでユーザーに国を選ばせる
selected_countries = st.sidebar.multiselect(
    "比較したい国を選択してください（複数選択可）",
    options=country_list,
    default=default_countries,
)

# 4. メイン画面の処理
if not selected_countries:
    st.warning("👈 サイドバーから少なくとも1つの国を選択してください。")
else:
    # 選択された国のデータだけをフィルタリング
    df_filtered = df_quinquennial[
        df_quinquennial["Country Name"].isin(selected_countries)
    ]

    # グラフ描画用に「縦持ち（Long形式）」に変換（年を横軸、人口を縦軸にするため）
    year_cols = [
        str(y) for y in range(1960, 2026, 5)
    ]  # ['1960', '1965', ..., '2025']

    # pandas の melt で整形の魔法
    df_melted = df_filtered.melt(
        id_vars=["Country Name", "Country Code"],
        value_vars=year_cols,
        var_name="Year",
        value_name="Population",
    )

    # Streamlitのラインチャート用にデータをピボット（行：年、列：国名）
    df_chart = df_melted.pivot(
        index="Year", columns="Country Name", values="Population"
    )

    # 数値を整数から見やすいように万人・億人単位にするか、そのままにするか
    # ここではそのままの数値をグラフ化
    st.subheader("📊 選択した国の人口推移グラフ (1960 - 2025年)")
    st.line_chart(df_chart, height=500)

    # 5. 生データ（テーブル）の確認用タブまたはセクション
    with st.expander("📋 選択した国の詳細データを表示する"):
        # 見やすいように転置して表示
        st.dataframe(
            df_filtered.set_index("Country Name")[year_cols].style.format(
                "{:,.0f}"
            )
        )