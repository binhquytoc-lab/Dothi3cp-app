# Bước 1: Import thư viện
import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
# Bước 2: Tiêu đề website
st.title('Ứng dụng phân tích giá cổ phiếu Việt Nam')
st.write('Biểu đồ giá đóng cửa của 3 cổ phiếu: VCB, FPT, HPG')
# Bước 3: Chọn danh sách cổ phiếu
stocks = ['VCB.VN', 'FPT.VN', 'HPG.VN']
# Bước 4: Tải dữ liệu
data = yf.download(
    stocks,
    start='2022-01-01'
)
# Bước 5: Lấy giá đóng cửa
close_prices = data['Close']
# Bước 6: Vẽ biểu đồ
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
# Hiển thị biểu đồ trên web
st.pyplot(fig)
# Bước 7: Hiển thị giá đóng cửa mới nhất
st.subheader('Giá đóng cửa mới nhất')
for stock in stocks:
    latest_price = close_prices[stock].dropna().iloc[-1]
    st.write(
        f'{stock}: {latest_price:.2f} VND'
    )
