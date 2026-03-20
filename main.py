import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    df = pd.read_csv("data/cost_data.csv")
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.month
    return df

def summarize_by_department(df):
    department_summary = (
        df.groupby("department")["amount"]
        .sum()
        .sort_values(ascending=False)
    )
    return department_summary

def summarize_by_month(df):
    monthly_summary = (
        df.groupby("month")["amount"]
        .sum()
    )
    return monthly_summary

def summarize_by_category(df):
    category_summary = (
        df.groupby("category")["amount"]
        .sum()
        .sort_values(ascending=False)
        .head(3)        
    )
    return category_summary

def plot_category_top3(category_data, month):
    plt.figure(figsize=(8, 5))
    category_data.plot(kind="bar")
    plt.title(f"Month {month} Category TOP 3 Bar Chart")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(f"result/{month}_category_top3.png")
    plt.show()


def main():
    df = load_data()
    
    try:
        month = int(input("몇 월을 보시겠습니까?"))

        if month < 1 or month > 12:
            print("1~12 사이의 월을 입력하세요.")
        else:
            monthly_df = df[df["month"] == month]
            if monthly_df.empty:
                print("데이터 없음")
            else:
                monthly_data = summarize_by_department(monthly_df)
                category_data = summarize_by_category(monthly_df)
                top_category = category_data.index[0]
                top_value = category_data.iloc[0]

                print("=== 데이터 미리보기 ===")
                print(df.head())
                print()

                print("=== 부서별 총비용 ===")
                print(summarize_by_department(df))
                print()

                print("=== 월별 총비용 ===")
                print(summarize_by_month(df))
                print()

                print(f"=== {month}월의 부서별 총비용 ===")
                print(monthly_data)
                print()

                print(f"=== {month}월의 Category TOP 3 ===")
                print(category_data)

                #Graph
                plot_category_top3(category_data, month)
                print(f"{month}월에는 {top_category} category의 비용이 가장 높았습니다({top_value})")

    except ValueError:
        print("숫자를 입력하세요")

main()