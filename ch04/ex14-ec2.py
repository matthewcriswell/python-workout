
weather_dict = {
'230130': 30,
'230129': 73,
'230128': 60,
'230127': 56,
'230126': 58,
'230125': 56,
'230124': 53,
'230123': 60,
'230122': 62,
'230121': 63
}

available_dates = set(weather_dict.keys())
while True:
    user_input = input("Enter a date YYMMDD: ").strip()
    if user_input in available_dates:
        print("Temp on that day: ", weather_dict[user_input])
        day_before = str(int(user_input) - 1)
        day_after = str(int(user_input) + 1)
        if day_before in available_dates:
            print("Day before:", weather_dict[day_before])
        if day_after in available_dates:
            print("Day after: ", weather_dict[day_after])
    else:
        print(f"{user_input} unavailable")
    break
