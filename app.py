# app.py

# Bước 1: Import thư viện
import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Bước 2: Tiêu đề website
st.title('Vẽ biểu đồ giá đóng cửa của 3 cổ phiếu tại Việt Nam')

st.write('Nhập tên 3 mã cổ phiếu và ngày bắt đầu muốn vẽ biểu đồ giá đóng cửa')

# Bước 3: Ô nhập mã cổ phiếu
stock1 = st.text_input('Nhập mã cổ phiếu thứ 1', 'VCB.VN')
stock2 = st.text_input('Nhập mã cổ phiếu thứ 2', 'FPT.VN')
stock3 = st.text_input('Nhập mã cổ phiếu thứ 3', 'HPG.VN')

# Bước 4: Ô nhập ngày bắt đầu
start_date = st.date_input(
    'Chọn ngày bắt đầu',
    pd.to_datetime('2008-01-01')
)

# Bước 5: Nút button
if st.button('Vẽ biểu đồ'):

    # Danh sách cổ phiếu
    stocks = [stock1, stock2, stock3]

    # Tải dữ liệu
    data = yf.download(
        stocks,
        start=start_date
    )

    # Lấy giá đóng cửa
    close_prices = data['Close']

    # Vẽ biểu đồ
    fig, ax = plt.subplots(figsize=(12, 6))

    for stock in stocks:

        ax.plot(
            close_prices.index,
            close_prices[stock],
            label=stock
        )

    ax.set_title('Biểu đồ giá đóng cửa')
    ax.set_xlabel('Ngày')
    ax.set_ylabel('Giá đóng cửa')

    ax.legend()

    ax.grid(True)

    # Hiển thị biểu đồ
    st.pyplot(fig)

    # Hiển thị giá mới nhất
    st.subheader('Giá đóng cửa ngày giao dịch gần nhất')

    for stock in stocks:

        latest_price = close_prices[stock].dropna().iloc[-1]

        st.write(
            f'{stock}: {latest_price:.0f} đồng/cổ phiếu'
        )
