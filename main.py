import pandas as pd

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

    except ValueError:
        print("숫자를 입력하세요")

main()