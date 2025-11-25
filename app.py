import streamlit as st
import pandas as pd

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Nepal Premier League 2024-25",
    page_icon="🏏",
    layout="wide"
)

# -------------------------------------------------
# LOAD DATA
# -------------------------------------------------
df_points = pd.read_csv("ptables.csv")
final_matches = pd.read_csv("npl_final_matches.csv")
most_runs = pd.read_csv("NPL/Batting Records/most_runs.csv")
most_wickets = pd.read_csv("NPL/Bowling Records/most_wickets.csv")
best_striker = pd.read_csv("NPL/Batting Records/highest_strike_rates.csv")
best_economy = pd.read_csv("NPL/Bowling Records/best_economy_rates.csv")

# -------------------------------------------------
# CLEAN DATA
# -------------------------------------------------
most_runs['runs'] = pd.to_numeric(most_runs['runs'], errors='coerce')
most_wickets['wicket'] = pd.to_numeric(most_wickets['wicket'], errors='coerce')
best_striker['strike_rate'] = pd.to_numeric(best_striker['strike_rate'], errors='coerce')
best_economy['economy'] = pd.to_numeric(best_economy['economy_rate'], errors='coerce')

df_points_small = df_points.drop(columns=['For', 'Against'], errors='ignore')

# -------------------------------------------------
# GET LATEST EDITION INFO
# -------------------------------------------------
latest = final_matches.sort_values('season ', ascending=False).iloc[0]
winner = latest['winner']
runner_up = latest['runner_up']
season = latest['season ']

# top performers
top_run = most_runs.sort_values('runs', ascending=False).iloc[0]
top_wkt = most_wickets.sort_values('wicket', ascending=False).iloc[0]
top_strike = best_striker.sort_values('strike_rate', ascending=False).iloc[0]
top_econ = best_economy.sort_values('economy', ascending=True).iloc[0]

# -------------------------------------------------
# SIDEBAR NAVIGATION
# -------------------------------------------------

st.sidebar.title("Select Page")
page = st.sidebar.radio("Navigation", 
    ["Home", "Points Table", "Batting Records", "Bowling Records", "Player Records"])


import base64
import streamlit as st

image_path = r"C:\Users\ACER\OneDrive\Documents\Desktop\AI-ML\Practice\Basic Web\NPL\download1.jpg"

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_base64 = get_base64_image(image_path)

st.markdown(f"""
<style>
    /* FULL PAGE BACKGROUND */
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}

    /* SIDEBAR BACKGROUND */
    [data-testid="stSidebar"] > div:first-child {{
        background: rgba(255, 255, 255, 0.0); /* fully transparent */
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: cover;
        background-position: center;
    }}

    /* Optional: remove sidebar default box */
    .css-1d391kg, .css-1lcbmhc {{
        background-color: rgba(255, 255, 255, 0) !important;
    }}

    /* CARD STYLING */
    .card {{
        padding: 20px;
        border-radius: 16px;
        background: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        text-align: center;
        transition: 0.2s ease-in-out;
        border: 1px solid #e6e6e6;
    }}

    .card:hover {{
        transform: scale(1.03);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }}

    .card h3 {{
        font-size: 18px;
        color: #444;
        margin-bottom: 6px;
    }}

    .card-value {{
        font-size: 26px;
        font-weight: 700;
        color: #002b80;
    }}

    .card-delta {{
        font-size: 16px;
        color: #008000;
        margin-top: 4px;
    }}
</style>
""", unsafe_allow_html=True)




# =====================================================
# 🏠 HOME PAGE
# =====================================================
if page == "Home":
    st.title("🏏 Nepal Premier League 2024-25")
    st.write("Welcome to the official NPL analytics dashboard.")

    # Winner - Runner Up Cards
    col1, colgap, col2 = st.columns([3,1,3])

    with col1:
        st.markdown(f"""
        <div class='card'>
            <h3>🏆 Winner</h3>
            <div class='card-value'>{winner}</div>
            <div class='card-delta'>{season}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class='card'>
            <h3>🥈 Runner-Up</h3>
            <div class='card-value'>{runner_up}</div>
            <div class='card-delta'>{season}</div>
        </div>
        """, unsafe_allow_html=True)

    # Points Table Preview
    st.subheader("📊 League Stage Points Table")

    st.dataframe(
        df_points_small,
        use_container_width=True,
        height=260
    )

    # Top Performers
    st.subheader("🔥 Top Performers (NPL 2024-25)")

    colA, colB, colC, colD = st.columns(4)

    with colA:
        st.markdown(
            f"""
            <div class='card'>
                <h3>Most Runs</h3>
                <div class='card-value'>{top_run['player']}</div>
                <div class='card-delta'>{int(top_run['runs'])} Runs</div>
            </div>
            """, unsafe_allow_html=True)

    with colB:
        st.markdown(
            f"""
            <div class='card'>
                <h3>Most Wickets</h3>
                <div class='card-value'>{top_wkt['player']}</div>
                <div class='card-delta'>{int(top_wkt['wicket'])} Wickets</div>
            </div>
            """, unsafe_allow_html=True)

    with colC:
        st.markdown(
            f"""
            <div class='card'>
                <h3>Best Strike Rate</h3>
                <div class='card-value'>{top_strike['player']}</div>
                <div class='card-delta'>{top_strike['strike_rate']}</div>
            </div>
            """, unsafe_allow_html=True)

    with colD:
        st.markdown(
            f"""
            <div class='card'>
                <h3>Best Economy</h3>
                <div class='card-value'>{top_econ['player']}</div>
                <div class='card-delta'>{top_econ['economy']}</div>
            </div>
            """, unsafe_allow_html=True)



# =====================================================
# 📊 POINTS TABLE PAGE
# =====================================================
elif page == "Points Table":

    st.title("📊 NPL Points Table by Season")

    # Get the unique seasons from your dataset
    seasons = sorted(df_points["season"].unique(), reverse=True)

    # Select season from dropdown
    selected_season = st.selectbox("Select a Season:", seasons)

    # Filter the points table for the selected season
    df_season = df_points[df_points["season"] == selected_season].drop(
        columns=['For', 'Against'], errors='ignore'
    )

    st.subheader(f"🏆 Points Table — Season {selected_season}")

    # Show table or warning if no rows
    if df_season.empty:
        st.warning("⚠️ No results found for this season.")
    else:
        st.dataframe(df_season, use_container_width=True, height=350)




# =====================================================
# 🧑‍🤝‍🧑 Batting RECORDS PAGE
# =====================================================
elif page == "Batting Records":
    st.title("Batting Records")
    options = [
    "Most Runs",
    "Most Hundreds",
    "Most Fifties",
    "Most Sixes",
    "Most Fours",
    "Highest Strike Rate",
    "Best Average",
    "Most Ducks",
    "Highest Score",
    "Most runs from Boundaries"
    ]

    selected_record = st.selectbox("Select a batting record:", options)
    if selected_record == "Most Runs":
        st.subheader("🏏 Most Runs")
        st.dataframe(most_runs.sort_values('runs', ascending=False), use_container_width=True, height=400)
    elif selected_record == "Most Hundreds":
        st.subheader("🏏 Most Hundreds")
        most_hundreds = pd.read_csv("NPL/Batting Records/most_hundreds.csv")
        st.dataframe(most_hundreds.sort_values('hundreds_scored', ascending=False), use_container_width=True, height=400)
    elif selected_record == "Most Fifties":
        st.subheader("🏏 Most Fifties")
        most_fifties = pd.read_csv("NPL/Batting Records/most_fifties.csv")
        st.dataframe(most_fifties.sort_values('fifties_scored', ascending=False), use_container_width=True, height=400)
    elif selected_record == "Most Sixes":
        st.subheader("🏏 Most Sixes")
        most_sixes = pd.read_csv("NPL/Batting Records/most_sixes.csv")
        st.dataframe(most_sixes.sort_values('boundary_sixes', ascending=False), use_container_width=True, height=400)
    elif selected_record == "Most Fours":
        st.subheader("🏏 Most Fours")
        most_fours = pd.read_csv("NPL/Batting Records/most_runs.csv")
        st.dataframe(most_fours.sort_values('boundary_fours', ascending=False), use_container_width=True, height=400)

    elif selected_record == "Highest Strike Rate":
        st.subheader("🏏 Highest Strike Rate")
        st.dataframe(best_striker.sort_values('strike_rate', ascending=False), use_container_width=True, height=400)
    elif selected_record == "Best Average":
        st.subheader("🏏 Best Average")
        best_average = pd.read_csv("NPL/Batting Records/highest_averages.csv")
        best_average['batting_average'] = pd.to_numeric(best_average['batting_average'], errors='coerce')
        st.dataframe(best_average.sort_values('batting_average', ascending=False), use_container_width=True, height=400)
    elif selected_record == "Most Ducks":
        st.subheader("🏏 Most Ducks")
        most_ducks = pd.read_csv("NPL/Batting Records/most_ducks.csv")
        most_ducks['ducks_scored'] = pd.to_numeric(most_ducks['ducks_scored'], errors='coerce')
        st.dataframe(most_ducks.sort_values('ducks_scored', ascending=False), use_container_width=True, height=400)
    elif selected_record == "Highest Score":
        st.subheader("🏏 Highest Score")
        highest_score = pd.read_csv("NPL/Batting Records/high_scores.csv")
        highest_score['runs_scored'] = pd.to_numeric(highest_score['runs_scored'], errors='coerce')
        st.dataframe(highest_score.sort_values('runs_scored', ascending=False), use_container_width=True, height=400)
    elif selected_record == "Most runs from Boundaries":
        st.subheader("🏏 Most runs from Boundaries in a Innings")
        runs_from_boundaries = pd.read_csv("NPL/Batting Records/most_runs_from_fours_and_sixes_innings.csv")
        runs_from_boundaries['runs_from_boundaries'] = pd.to_numeric(runs_from_boundaries['runs_from_fours_and_sixes'], errors='coerce')
        st.dataframe(runs_from_boundaries.sort_values('runs_from_boundaries', ascending=False), use_container_width=True, height=400)


# =====================================================
# 🏏 TEAM RECORDS PAGE
# =====================================================
elif page == "Bowling Records":
    st.title("Bowling Records")
    options = [
        "Most Wickets",
        "Best Economy Rate",
        "Best Bowling Average",
        "Most Maidens",
        "Most 4-Wicket Hauls",
        "Most 5-Wicket Hauls",
        "Best Bowling figure in a Match"
    ]
    selected_record = st.selectbox("Select a bowling record:", options)
    if selected_record == "Most Wickets":
        st.subheader("🏏 Most Wickets")
        st.dataframe(most_wickets.sort_values('wicket', ascending=False), use_container_width=True, height=400)
    
    elif selected_record == "Best Economy Rate":
        st.subheader("🏏 Best Economy Rate")
        st.dataframe(best_economy.sort_values('economy_rate', ascending=True), use_container_width=True, height=400)
    
    elif selected_record == "Best Bowling Average":
        st.header("🏏 Best Bowling Average")
        best_average = pd.read_csv("NPL/Bowling Records/best_averages.csv")
        best_average['bowling_average'] = pd.to_numeric(best_average['bowling_average'], errors='coerce')
        st.dataframe(best_average.sort_values('bowling_average', ascending=True), use_container_width=True, height=400)
    
    elif selected_record == "Most Maidens":
        st.subheader("🏏 Most Maidens")
        most_maidens = pd.read_csv("NPL/Bowling Records/most_wickets.csv")
        # check column exists
        if 'maidens_earned' not in most_maidens.columns:
            st.warning("⚠️ No results found for this record.")
        else:
            # replace '-' with NA then convert to numeric
            most_maidens['maidens_earned'] = pd.to_numeric(most_maidens['maidens_earned'].replace('-', pd.NA), errors='coerce')
            # if all values are missing, show warning
            if most_maidens['maidens_earned'].dropna().empty:
                st.warning("⚠️ No results found for this record.")
            else:
                st.dataframe(
                    most_maidens.loc[:, ["player", "maidens_earned"]]
                    .sort_values("maidens_earned", ascending=False),
                    use_container_width=True,
                    height=400
                )

    elif selected_record == "Most 4-Wicket Hauls":
        st.subheader("🏏 Most 4-Wicket Hauls")
        most_4_wickets = pd.read_csv("NPL/Bowling Records/most_four_wickets_innings.csv")
        most_4_wickets['four_wickets'] = pd.to_numeric(most_4_wickets['four_wickets'], errors='coerce')
        st.dataframe(most_4_wickets.loc[:, ['player', 'four_wickets']].sort_values('four_wickets', ascending=False), use_container_width=True, height=400)
    
    elif selected_record == "Most 5-Wicket Hauls":
        st.subheader("🏏 Most 5-Wicket Hauls")
        most_5_wickets = pd.read_csv("NPL/Bowling Records/most_five_wickets_innings.csv")
        most_5_wickets['five_wickets'] = pd.to_numeric(most_5_wickets['five_wickets'], errors='coerce')
        st.dataframe(
            most_5_wickets.loc[:, ['player', 'five_wickets']].sort_values('five_wickets', ascending=False),
            use_container_width=True,
            height=400
        )

    elif selected_record == "Best Bowling figure in a Match":
        st.subheader("🏏 Best Bowling in a Match")
        best_bowling = pd.read_csv("NPL/Bowling Records/best_bowling_figures_match.csv")
        st.dataframe(
            best_bowling,
            use_container_width=True,
            height=400
        )


elif page == "Player Records":


    # Page config
    st.set_page_config(page_title="Player Profile", layout="wide")

    # Load dataset
    @st.cache_data
    def load_data():
        return pd.read_csv("NPL/player_dataset.csv")

    df = load_data()

    st.title("🏏 Player Records")

    # -------------------
    # Searchable Player Input
    # -------------------
    

    # Text input filter
    player_data = st.selectbox("Select a Player:", options=[""] + sorted(df["player"].unique()))
    # Filter list for selectbox suggestions
    filtered_players = [p for p in df["player"].unique() if player_data.lower() in p.lower()]

  
        


    
    player_data = df[df["player"] == filtered_players[0]].squeeze()
    st.write("### Player Stats:")
       # Stat tables
    batting_cols = [
        'bat_span', 'bat_matches_played', 'bat_innings_batted', 'bat_not_out',
        'bat_runs', 'bat_highest_inns_score', 'bat_batting_average', 'bat_balls_faced',
        'bat_strike_rate', 'bat_hundreds_scored', 'bat_fifties_scored',
        'bat_ducks_scored', 'bat_boundary_fours', 'bat_boundary_sixes'
    ]

    bowling_cols = [
        'bowl_span', 'bowl_matches_played', 'bowl_innings_bowled', 'bowl_balls',
        'bowl_overs', 'bowl_maidens_earned', 'bowl_conceded', 'bowl_wicket',
        'bowl_best_innings_bowling', 'bowl_bowling_average', 'bowl_economy_rate',
        'bowl_strike_rate', 'bowl_four_wickets', 'bowl_five_wickets'
    ]

    # Batting table (transpose to convert columns → rows)
    batting_table = player_data[batting_cols].T.reset_index()
    batting_table.columns = ["Statistic", "Value"]

    # Bowling table
    bowling_table = player_data[bowling_cols].T.reset_index()
    bowling_table.columns = ["Statistic", "Value"]

    # Convert to string to fix Arrow issue
    batting_table["Value"] = batting_table["Value"].astype(str)
    bowling_table["Value"] = bowling_table["Value"].astype(str)

    # Table CSS styling
    st.markdown("""
    <style>
    table {
        background-color: black !important;
        color: white !important;
    }
    thead th, tbody td {
        background-color: #111 !important;
        color: white !important;
    }
    table, th, td {
        border: 1px solid white !important;
    }
    </style>
    """, unsafe_allow_html=True)


    # Show tables side by side
    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🏏 Batting Records")
        st.table(batting_table)

    with col2:
        st.subheader("🎯 Bowling Records")
        st.table(bowling_table)


   




