from tasks.extract_data import extract, get_athlete_df
from tasks.db import get_sql_conn


def load_data():
    conn = get_sql_conn().connect()
    data = extract()
    # print(get_athlete_df().shape)
    get_athlete_df().to_sql(name="athletes", con=conn, index=False, if_exists="append")
    # data["final_events_df"].to_sql(name="events", con=conn, if_exists="replace")
    # data["final_medals_df"].to_sql(name="medals", con=conn, if_exists="replace")
