names=["rares","stefan","vanesa","argentina","paul"]
hobby=["crosetat","pictat","pescuit","tenis","inot"]
food=["quacamole","pizza","salata","prajeli","piure"]

for nume,hobbies,foods in zip(names,hobby,food):
    print(f"Lui {nume} ii p[lace {hobbies} si toata ziua mananca {foods}")


text="imi e foame"

text_it=iter(text)
print(*text_it)
