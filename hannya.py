import random

print("般若心経を覚えよう！")
print("●：カネ")
print("▲：カネ押さえ")
print("■：木魚")

# 問題と選択肢を定義
question = "一：「摩訶般若波羅蜜多心経」の次は？"
choices = ["●■観自在菩薩", "色不異空空不異色", "無苦集滅道無智亦無得", "依般若波羅蜜多●故"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "二：「●■観自在菩薩」の次は？"
choices = ["行深般若波羅密多時", "無色無受想行識", "亦無老死尽", "故得阿耨多羅三藐三菩提"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "三：「行深般若波羅密多時」の次は？"
choices = ["照見●五蘊皆空", "乃至無老死", "心無圭礙無圭礙故無有恐怖", "能除一切苦"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "四：「照見●五蘊皆空」の次は？"
choices = ["度一切苦厄", "無色声香味触法", "依般若波羅蜜多●", "能除一切苦真実不虚"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "五：「度一切苦厄」の次は？"
choices = ["舎利子", "色不異空空不異色", "乃至無老死", "故得阿耨多羅三藐三菩提"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "六：「舎利子」の次は？"
choices = ["色不異空空不異色", "亦無老死尽", "故知般若波羅蜜多", "●羯諦羯諦波羅羯諦波羅僧羯諦"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "七：「色不異空空不異色」の次は？"
choices = ["色即是空空即是色", "是故空中", "亦無老死尽", "依般若波羅蜜多●"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "八：「色即是空空即是色」の次は？"
choices = ["受想行識亦復如是", "乃至無老死", "菩提薩垂", "依般若波羅蜜多●"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")
            
            
# 問題と選択肢を定義
question = "九：「受想行識亦復如是」の次は？"
choices = ["舎利子", "是諸法空相", "度一切苦厄", "以無所得故"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "十：「舎利子」の次は？"
choices = ["是諸法空相", "是故空中", "無苦集滅道無智亦無得", "照見●五蘊皆空"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "十一：「是諸法空相」の次は？"
choices = ["不生不滅不垢不浄不増不減", "無眼界乃至無意識界", "●■観自在菩薩", "舎利子"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "十二：「不生不滅不垢不浄不増不減」の次は？"
choices = ["是故空中", "即説呪曰", "度一切苦厄", "是諸法空相"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "十三：「是故空中」の次は？"
choices = ["無色無受想行識", "無眼耳鼻舌身意", "無色声香味触法", "無眼界乃至無意識界"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "十四：「無色無受想行識」の次は？"
choices = ["無眼耳鼻舌身意", "無無明亦無無明尽", "無苦集滅道無智亦無得", "依般若波羅蜜多●故"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "十五：「無眼耳鼻舌身意」の次は？"
choices = ["無色声香味触法", "無眼界乃至無意識界", "菩提薩垂", "故説般若波羅蜜多呪"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "十六：「無色声香味触法」の次は？"
choices = ["無眼界乃至無意識界", "亦無老死尽", "心無圭礙無圭礙故無有恐怖", "故知般若波羅蜜多"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "十七：「無眼界乃至無意識界」の次は？"
choices = ["無無明亦無無明尽", "無苦集滅道無智亦無得", "依般若波羅蜜多●", "即説呪曰"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "十八：「無無明亦無無明尽」の次は？"
choices = ["乃至無老死", "亦無老死尽", "依般若波羅蜜多●故", "故知般若波羅蜜多"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "十九：「乃至無老死」の次は？"
choices = ["亦無老死尽", "以無所得故", "故得阿耨多羅三藐三菩提", "●羯諦羯諦波羅羯諦波羅僧羯諦"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "二十：「亦無老死尽」の次は？"
choices = ["無苦集滅道無智亦無得", "色不異空空不異色", "是諸法空相", "無色無受想行識"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "二十一：「無苦集滅道無智亦無得」の次は？"
choices = ["以無所得故", "心無圭礙無圭礙故無有恐怖", "是大神呪是大明呪是無上呪是無等等呪", "即説呪曰"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "二十二：「以無所得故」の次は？"
choices = ["菩提薩垂", "故説般若波羅蜜多呪", "依般若波羅蜜多●", "依般若波羅蜜多●故"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "二十三：「菩提薩垂」の次は？"
choices = ["依般若波羅蜜多●故", "究竟涅槃三世諸仏", "能除一切苦真実不虚", "菩提薩婆訶般若心経■▲"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "二十四：「依般若波羅蜜多●故」の次は？"
choices = ["心無圭礙無圭礙故無有恐怖", "遠離一切顛倒夢想", "故得阿耨多羅三藐三菩提", "是大神呪是大明呪是無上呪是無等等呪"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "二十五：「心無圭礙無圭礙故無有恐怖」の次は？"
choices = ["遠離一切顛倒夢想", "究竟涅槃三世諸仏", "故説般若波羅蜜多呪", "是故空中"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")
            
            
# 問題と選択肢を定義
question = "二十六：「遠離一切顛倒夢想」の次は？"
choices = ["究竟涅槃三世諸仏", "舎利子", "不生不滅不垢不浄不増不減", "無色無受想行識"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "二十七：「究竟涅槃三世諸仏」の次は？"
choices = ["依般若波羅蜜多●", "菩提薩婆訶般若心経■▲", "無眼耳鼻舌身意", "乃至無老死"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "二十八：「依般若波羅蜜多●」の次は？"
choices = ["故得阿耨多羅三藐三菩提", "遠離一切顛倒夢想", "無色無受想行識", "色不異空空不異色"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "二十九：「故得阿耨多羅三藐三菩提」の次は？"
choices = ["故知般若波羅蜜多", "故説般若波羅蜜多呪", "行深般若波羅密多時", "色不異空空不異色"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "三十：「故知般若波羅蜜多」の次は？"
choices = ["是大神呪是大明呪是無上呪是無等等呪", "能除一切苦真実不虚", "菩提薩垂", "無色声香味触法"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "三十一：「是大神呪是大明呪是無上呪是無等等呪」の次は？"
choices = ["能除一切苦真実不虚", "故説般若波羅蜜多呪", "乃至無老死", "●■観自在菩薩"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "三十二：「能除一切苦真実不虚」の次は？"
choices = ["故説般若波羅蜜多呪", "乃至無老死", "依般若波羅蜜多●故", "行深般若波羅密多時"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "三十三：「故説般若波羅蜜多呪」の次は？"
choices = ["即説呪曰", "故知般若波羅蜜多", "心無圭礙無圭礙故無有恐怖", "無苦集滅道無智亦無得"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "三十四：「即説呪曰」の次は？"
choices = ["●羯諦羯諦波羅羯諦波羅僧羯諦", "究竟涅槃三世諸仏", "無眼耳鼻舌身意", "不生不滅不垢不浄不増不減"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")


# 問題と選択肢を定義
question = "三十五：「●羯諦羯諦波羅羯諦波羅僧羯諦」の次は？"
choices = ["菩提薩婆訶般若心経■▲", "遠離一切顛倒夢想", "舎利子", "照見●五蘊皆空"]

# 正解の選択肢を決定
answer = choices[0]

# 選択肢をシャッフル
random.shuffle(choices)

# 問題と選択肢を表示
print(question)
for i in range(len(choices)):
    print(f"{i+1}. {choices[i]}")

# ユーザーの回答を受け取る
while True:
    user_answer = int(input("回答を選択してください（1-4）: "))
    if 1 <= user_answer <= 4:
        break
    else:
        print("1から4の数字を入力してください。")

# 回答が正しいかどうかをチェックして結果を表示
if choices[user_answer-1] == answer:
    print("正解です！")
else:
    print("不正解です。もう一度挑戦してください。")
    while True:
        user_answer = int(input("回答を選択してください（1-4）: "))
        if 1 <= user_answer <= 4:
            break
        else:
            print("1から4の数字を入力してください。")
    if choices[user_answer-1] == answer:
        print("正解です！")
    else:
        print("不正解です。もう一度挑戦してください。")
        while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
        else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。もう一度挑戦してください。")
            while True:
                user_answer = int(input("回答を選択してください（1-4）: "))
                if 1 <= user_answer <= 4:
                    break
            else:
                print("1から4の数字を入力してください。")
        if choices[user_answer-1] == answer:
            print("正解です！")
        else:
            print("不正解です。")

print("おつかれさまでした！これで宗教のテストは満点ですね！")
