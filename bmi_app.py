"""
身長(cm),体重(kg)を受け取りBMIを小数第2位で出力するアプリ
"""
def main():
    height_cm = float(input('身長(cm)は？ > '))
    weight_kg = float(input('体重(kg)は？> '))
    # height_cm = 180
    # weight_kg = 76
    # 出力 24.6

    #変数のインライン化
    bmi = round(weight_kg / ((height_cm/100) ** 2), 2)
    print(bmi)

if __name__ == '__main__':
    main()