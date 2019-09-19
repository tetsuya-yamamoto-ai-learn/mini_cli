"""割り勘アプリ

金額と人数を受け取り、割り勘結果を出力するアプリ

1500 円　3人　⇒　1人当たり500円です。端数は0円です。
500 円　3人　⇒　1人当たり166円です。端数は2円です。

"""


def main():
    # 入力
    number_of_people = int(input("人数を入力してください。"))
    amount = int(input("料金総額を入力してください。"))

    # 計算
    payment, remainder = divmod(amount, number_of_people)
    # payment = amount // number_of_people  # 一人当たりの値段の計算
    # remainder = amount % number_of_people  # 端数の計算

    # 出力
    print(f"一人当たり{payment}円です。端数は{remainder}円です。")  # 先頭にfを入れると、fstring（f記法）を使用できる。（python3.6から）


if __name__ == '__main__':
    main()
