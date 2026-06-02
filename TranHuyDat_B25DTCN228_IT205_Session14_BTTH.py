grade_book = [
    {"id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
    {"id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)}
]

def display_grades(book):
    if not book:
        print("Danh sạch hiện đang trống")
        return
    
    print("\n--- BẢNG ĐIỂM HỌC SINH ---")
    print(f"{'Mã SV':<8} | {'Tên Học Sinh':<20} | {'Toán':<8} | {'Anh':<8} | {'ĐTB':<8}")
    print("-" * 70)

    for student in book:
        math_score, english_score = student['info']
        avg_score = (math_score + english_score) / 2
        
        print(
            f"{student['id']:<8} | "
            f"{student['name']:<20} | "
            f"{math_score:<8.1f} | "
            f"{english_score:<8.1f} | "
            f"{avg_score:<8.2f}"
        )

    print("-" * 70)

def add_student(book):
    while True:
        student_id = input("Nhập mã học sinh mới: ").strip().upper()

        if not student_id:
            print("Mã sinh viên không được để trống")

        if all(student['id'] != student_id for student in book):
            break
        else:
            print("Mã sinh viên đã tồn tại! Yêu cầu chọn mã khác")
    
    student_name = input('Nhập tên học sinh: ').strip().title()
    math_score = float(input("Nhập điểm Toán: "))
    english_score = float(input("Nhập điểm Anh: "))

    book.append({
        "id": student_id,
        "name": student_name,
        "info": (math_score, english_score)
    })

def update_scores(book):
    while True:
        student_id = input("Nhập mã học sinh cần cập nhập: ").strip().upper()

        if not student_id:
            print("Mã sinh viên không được để trống")
        else:
            break
    
    for student in book:
        if student['id'] == student_id:
            new_math= float(input("Nhập điểm Toán: "))
            new_english = float(input("Nhập điểm Anh: "))

            student['info'] = (new_math,new_english)

            print(f"Thành công: Đã cập nhật điểm cho học sinh {student_id}!")
            return
    else:
        print("Không tìm thấy mã sinh viên")

def delete_student(book):
    while True:
        student_id = input("Nhập mã học sinh cần cập nhập: ").strip().upper()

        if not student_id:
            print("Mã sinh viên không được để trống")
        else:
            break
    
    for student in book:
        if student['id'] == student_id:
            book.remove(student)
            print("Thành công: Đã xóa hồ sơ học sinh SV02 khỏi hệ thống!")
            return
    else:
        print("Không tìm thấy sinh viên")



while True:
    choice = input("""\n=== HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ===
1. Xem bảng điểm học sinh
2. Thêm hồ sơ học sinh mới
3. Cập nhật điểm số
4. Xóa hồ sơ học sinh
5. Thoát chương trình
================================
Chọn chức năng (1-5): """)

    match choice:
        case '1':
            display_grades(grade_book)

        case '2':
            add_student(grade_book)
        
        case '3':
            update_scores(grade_book)
        
        case '4':
            delete_student(grade_book)
        
        case '5':
            print("Thoát chương trình")
            break