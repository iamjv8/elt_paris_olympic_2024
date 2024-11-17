import pandas as pd

# import db


# Read the CSV file
athletes_df = pd.read_csv("./csv/athletes.csv")
events_df = pd.read_csv("./csv/events.csv")
medals_df = pd.read_csv("./csv/medals.csv")

# Data frame to load in SQL tables.
final_athletes_df = athletes_df[
    [
        "code",
        "name",
        "name_short",
        "gender",
        "country_code",
        "country",
        "height",
        "weight",
        "disciplines",
        "events",
        "birth_date",
    ]
]

final_events_df = events_df[["event", "tag", "sport", "sport_code"]]

final_medals_df = medals_df[
    [
        "medal_type",
        "medal_code",
        "medal_date",
        "name",
        "gender",
        "discipline",
        "event",
        "event_type",
        "code",
        "country_code",
        "country",
    ]
]


print(final_athletes_df)