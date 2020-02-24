input_str = input()
articles, impact_factor = input_str.split(" ")
print(int(articles) * (int(impact_factor) - 1) + 1)
