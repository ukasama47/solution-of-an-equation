import sys

def discriminate(a, b, c):
    discriminant = b**2 - 4*a*c
    return discriminant

def main():
    print("2次方程式 ax^2 + bx + c = 0 の解がどのようになるか判別します。\n")

    # 係数の受け取り
    try:
        a = float(input("aの値を入力してください: "))
        b = float(input("bの値を入力してください: "))
        c = float(input("cの値を入力してください: "))
    except ValueError:
        print("無効な入力です。数値を入力してください。")
        sys.exit(1)

    # 判別式を計算
    discriminant = discriminate(a, b, c)

    print("\n判別式 b^2 - 4ac =", discriminant)

    # 解の性質を判別して結果を表示
    if discriminant > 0:
        print("2実数解")
    elif discriminant == 0:
        print("重解")
    else:
        print("虚数解")

# プログラムを実行
main()

        result = check_pass_fail(score)
        print(f"{i}: {score}点 {result}")

# プログラムを実行
main()
