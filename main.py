from weather import get_weather

if __name__ == "__main__":
    print("🌤  简易天气查询 CLI")
    city = input("请输入城市名称（如 beijing, shanghai）: ")
    result = get_weather(city)
    print("查询结果：", result)
