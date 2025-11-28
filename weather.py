from data import WEATHER_DATA

def get_weather(city: str) -> str:
    city = city.lower()
    return WEATHER_DATA.get(city, "抱歉，暂无该城市的天气数据。")
