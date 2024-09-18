import pandas as pd
from sklearn.datasets import fetch_california_housing


def task():
    # Загрузка данных
    df: pd.DataFrame = fetch_california_housing(as_frame=True).frame

    # 8. Использовать метод info()
    print(df.info)

    # 9. Узнать, есть ли пропущенные значения
    print("\nКоличество пропущенных значений по каждому столбцу:")
    print(df.isna().sum())

    # 10. Вывести записи, где средний возраст домов в районе более 50 лет и население более 2500 человек
    filtered_df = df.loc[(df["HouseAge"] > 50) & (df["Population"] > 2500)]
    print(
        "\nЗаписи, где средний возраст домов в районе более 50 лет и население более 2500 человек:"
    )
    print(filtered_df)

    # 11. Узнать максимальное и минимальное значения медианной стоимости дома
    median_house_value = df["MedHouseVal"]
    print("\nМаксимальное значение медианной стоимости дома:", median_house_value.max())
    print("Минимальное значение медианной стоимости дома:", median_house_value.min())

    # 12. Используя метод apply(), вывести на экран название признака и его среднее значение
    mean_values = df.apply(lambda x: x.mean())
    print("\nСредние значения признаков:")
    print(mean_values)


if __name__ == "__main__":
    task()
