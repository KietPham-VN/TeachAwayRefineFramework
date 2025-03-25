import streamlit as st

# Thiết lập cấu hình trang Streamlit
st.set_page_config(
    page_title="Giới thiệu về Framework Refine: Một Giải pháp Hiệu Quả cho Ứng dụng Quản lý",
    page_icon="./assets/icons/favicon.ico",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Nội dung chính của trang
st.write(
    """
    <style>
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
    .img-container {
        margin-bottom: 20px;
    }
    h1 {
        font-size: 80px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar
with st.sidebar:
    st.header("Nội dung bài viết")
    st.markdown(
    """
    <div class="toc">
        <p>1. Giới thiệu</p>
        <p>2. Các kiến thức, khái niệm cơ bản</p>
        <p>3. Nội dung chuyên sâu</p>
        <p>4. Kiến thức mở rộng</p>
        <p>5. Liên hệ thực tế</p>
        <p>6. Demo</p>
        <p>7. Kết luận</p>
        <p>8. Tài liệu tham khảo:</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "<h2 style='color: #FFC81B;'>F-Code [Techaway 2025]</h2>",
        unsafe_allow_html=True,
    )
    st.markdown("#### **F-Code authors:**")
    st.write("""
        - *Phạm Hoàng Tuấn - SE200947*
        - *Võ Đức Trí - SE204214*
    """)

    st.markdown(
    """
# Giới thiệu về Framework Refine: Một Giải pháp Hiệu Quả cho Ứng dụng Quản lý

![Ảnh minh họa](https://github.com/KietPham-VN/TeachAwayRefineFramework/blob/main/assets/images/1.png?raw=true)



## 1. Giới thiệu

Trong thời đại số hóa, nhu cầu xây dựng các ứng dụng quản lý dữ liệu ngày càng tăng. Các framework hiện có như React Admin hay Ant Design Pro cung cấp giải pháp mạnh mẽ, nhưng đôi khi đòi hỏi sự tùy chỉnh cao và tốn nhiều công sức. Thay vào đó, Refine, một framework phát triển trên nền tảng React, ra đời nhằm cung cấp một giải pháp linh hoạt, giúp tăng tốc quá trình phát triển ứng dụng CRUD (Create, Read, Update, Delete) mà không cần viết code quá nhiều.

Bài viết này sẽ giới thiệu về Refine, từ các khái niệm cơ bản đến nội dung chuyên sâu, giúp lập trình viên hiểu rõ hơn về framework này và cách ứng dụng vào thực tế.

![Ảnh minh họa](https://github.com/KietPham-VN/TeachAwayRefineFramework/blob/main/assets/images/2.png?raw=true)

## 2. Các kiến thức, khái niệm cơ bản

### 2.1. Refine là gì?

Refine là một framework mã nguồn mở dựa trên React, hỗ trợ TypeScript, giúp xây dựng nhanh chóng các ứng dụng quản lý dữ liệu (hay nặng về CRUD). Nó tích hợp với nhiều thư viện phổ biến như Ant Design, Material UI, React Query, GraphQL…

### 2.2. Các đặc điểm chính

- **Kiến trúc linh hoạt:** Hỗ trợ nhiều thư viện UI và backend API khác nhau.
- **Tích hợp sẵn nhiều tính năng:** Authentication, Authorization, Notification, Internationalization, v.v.
- **Mô hình dữ liệu linh hoạt:** Hỗ trợ các nguồn dữ liệu khác nhau như REST API, GraphQL, Firebase, Strapi.
- **Tối ưu hóa hiệu suất:** Sử dụng React Query để quản lý trạng thái dữ liệu hiệu quả.

![Ảnh minh họa](https://github.com/KietPham-VN/TeachAwayRefineFramework/blob/main/assets/images/3.png?raw=true)


## 3. Nội dung chuyên sâu

### 3.1. Cấu trúc của một dự án Refine

Một dự án Refine điển hình gồm các thành phần chính:

- **resources/:** Chứa các tài nguyên của ứng dụng (user, post, category,...).
- **pages/:** Các trang giao diện ứng dụng.
- **components/:** Các thành phần UI tái sử dụng.
- **providers/:** Các bộ điều phối dữ liệu như authProvider, dataProvider.

### 3.2. Cách sử dụng Refine

*Cài đặt Refine*
![Ảnh minh họa](https://github.com/KietPham-VN/TeachAwayRefineFramework/blob/main/assets/images/4.png?raw=true)

Khi cài đặt ứng dụng sẽ có hỏi là thêm ví dụ minh họa, trong trường hợp bạn xác nhận “Yes” thì mọi thứ đã được cài sẵn và công việc của bạn chỉ là ngồi đọc source code và tinh chỉnh sao cho hợp lý.

Trong trường hợp bạn lỡ tay hoặc vô tình nhấn  “No” thì dưới đây là cách để cài đặt cho dự án:

*Tích hợp thư viện và tùy chỉnh router*

![Ảnh minh họa](https://github.com/KietPham-VN/TeachAwayRefineFramework/blob/main/assets/images/5.png?raw=true)

### 3.3. Xây dựng CRUD với Refine

Refine hỗ trợ nhanh chóng việc tạo các trang CRUD. 

Ví dụ, để tạo trang danh sách sản phẩm:
![Ảnh minh họa](https://github.com/KietPham-VN/TeachAwayRefineFramework/blob/main/assets/images/6.png?raw=true)


## 4. Kiến thức mở rộng

Ngoài CRUD cơ bản, Refine còn hỗ trợ:

- **Authentication và Authorization:** Dùng authProvider.
- **Realtime Data:** Kết hợp với Firebase hoặc Supabase.
- **Tùy chỉnh UI:** Sử dụng Ant Design hoặc Material UI.
- **Refine AI:** Hỗ trợ tự động hóa và tối ưu hóa quá trình quản lý dữ liệu bằng AI, giúp gợi ý và dự đoán dữ liệu thông minh hơn.

## 5. Liên hệ thực tế

Refine là một lựa chọn lý tưởng cho các ứng dụng quản lý như:

- Hệ thống quản lý khách hàng (CRM).
- Ứng dụng quản lý kho hàng, sản phẩm, nhân sự.
- Dashboard hiển thị dữ liệu theo thời gian thực (Ví dụ: DevOps)
- Ứng dụng thương mại điện tử.

## 6. Demo

Bạn có thể xem thử dự án mẫu trên [Refine.dev](https://refine.dev/) hoặc tạo một ứng dụng CRUD đơn giản theo hướng dẫn ở phần trên.

![Ảnh minh họa](https://github.com/KietPham-VN/TeachAwayRefineFramework/blob/main/assets/images/7.png?raw=true)


## 7. Kết luận

Refine là một framework mạnh mẽ giúp tăng tốc phát triển ứng dụng CRUD với React. Với sự linh hoạt trong cấu trúc và tích hợp sẵn nhiều tính năng, Refine giúp lập trình viên tiết kiệm thời gian mà vẫn đảm bảo hiệu suất và khả năng mở rộng. Nếu bạn đang tìm kiếm một giải pháp tối ưu cho các ứng dụng quản lý dữ liệu, Refine là một lựa chọn đáng cân nhắc.

## 8. Tài liệu tham khảo:

1. Refine Documentation: [Overview | Refine](https://refine.dev/docs)
2. GitHub Repository: [GitHub - refinedev/refine: A React Framework for building internal tools, admin panels, dashboards & B2B apps with unmatched flexibility.](https://github.com/refinedev/refine)

""",
    unsafe_allow_html=True,
)
