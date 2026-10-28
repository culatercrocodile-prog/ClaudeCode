from datetime import datetime


def format_datetime(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    print(format_datetime(datetime.now()))
