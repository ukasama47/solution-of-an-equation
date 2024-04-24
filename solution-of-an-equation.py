
def calculate_average(scores):
    total = sum(scores)
    average = total / len(scores)
    return average

def check_pass_fail(score):
    if score >= 60:
        return "合格"
    else:
        return "不合格"

def main():
    # 学生の点数
    scores = [55,34,65,43,78,98,65,44,54,66]

    # 学生の点数の入力を求める場合は下記の先頭の#をすべて外し、上記の”#学生の点数”を消してください
    #scores = []
    #for i in range(1, 11):
     #   score = int(input(f"{i}番目の学生の点数を入力してください: "))
     #   scores.append(score)

    # 最高点・最低点・平均点を計算
    maximum = max(scores)
    minimum = min(scores)
    average = calculate_average(scores)

    # 最高点・最低点・平均点を表示
    print("最高点:", maximum)
    print("最低点:", minimum)
    print("平均点:", format(average, ".2f"))

    # 合否を表示
    print("\n合否")
    for i, score in enumerate(scores, start=1):
        result = check_pass_fail(score)
        print(f"{i}: {score}点 {result}")

# プログラムを実行
main()
