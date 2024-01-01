import csv
# tính thuế 
def tinh_tien_thue(doanh_thu):
    if doanh_thu > 50000000:
        return doanh_thu*0.1
    else:
        return doanh_thu*0.05
    
# Tạo cửa hàng mới
def tao_cua_hang():
    ma_cua_hang=input("Nhập mã cửa hàng :")
    ten_cua_hang=input("Nhập tên cửa hàng :")
    von_dau_tu=float(input("Nhập vốn đầu tư :"))
    doanh_thu=float(input("NHập doanh thu :"))
    tien_thue=tinh_tien_thue(doanh_thu)
    return [ma_cua_hang,ten_cua_hang,von_dau_tu,doanh_thu,tien_thue]

# mở file
def mo_file():
    try:
        with open('ds_cua_hang.csv', mode='r', encoding='utf-8') as file:
            print("Đã mở file 'ds_cua_hang.csv'")
            reader = csv.reader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []
    
# Lưu file
def luu_file(ds_cua_hang):
    with open('ds_cua_hang.csv','w',encoding='utf-8',newline='') as file:
        writer=csv.writer(file)
        writer.writerows(ds_cua_hang)

# In ra danh sách cửa hàng 
def in_danh_sach(ds_cua_hang):
    print("Danh sách cửa hàng là ")
    for row in ds_cua_hang:
        print(row)

# xắp xếp doanh thu theo thứ tự giảm dần 
def sap_xep_theo_doanh_thu(ds_cua_hang):
    ds_cua_hang.sort(key=lambda x: x[3],reverse=True)

# Tìm cửa hàng theo mã cửa hàng 
def tim_cua_hang_theo_ma(ds_cua_hang,ma_cua_hang):
    for cua_hang in ds_cua_hang:
        if cua_hang[0] == ma_cua_hang :
            return cua_hang
    return None

# Tìm cửa hàng và xóa cửa hàng theo mã 
def xoa_cua_hang_theo_ma(ds_cua_hang,ma_cua_hang):
    for cua_hang in ds_cua_hang:
        if cua_hang[0] == ma_cua_hang:
            ds_cua_hang.remove(cua_hang)
            print(f"Của hàng có mã cửa hàng {ma_cua_hang} đã bị xóa ")
            return
    print("Không tìm thấy mã cửa hàng")

# Thống kê doanh thu 
def thong_ke_doanh_thu(ds_cua_hang,doanh_thu):
    for cua_hang in ds_cua_hang:
        tong_doanh_thu =sum(float(cua_hang[3]))
        print("Tổng doanh thu tất cả cửa hàng là :",tong_doanh_thu)


# Lọc cửa hàng theo vốn đầu tư
def loc_theo_von(ds_cua_hang,von_dau_tu):
    for cua_hang in ds_cua_hang:
        if cua_hang[3] == von_dau_tu:
            return cua_hang
        return None
    
# TÌm cửa hàng có doanh thu cao nhất 
def max_doanh_thu(ds_cua_hang):
    print("Cửa hàng có doanh thu lớn nhất là :")
    print(ds_cua_hang[1])

# TẠo menu 
def menu():
    ds_cua_hang=mo_file()
    while True:
        print("1.Mở file và In danh sách cửa hàng ")
        print("2.Thêm thông tin cửa hàng ( Tự động tính tiền thuế )")
        print("3.Lưu thông tin vào file ")
        print("4.Xắp xếp cửa hàng theo thứ tự giảm dần doanh thu ")
        print("5.Tìm của hàng băng mã cửa hàng ")
        print("6.Xóa cửa hàng bằng mã cửa hàng ")
        print("7.Thoát chương trình ")
        print("8.Thống kê doanh thu ")
        print("9.lọc cửa hàng theo vốn đầu tư ")
        print("10.In ra cửa hàng có doanh thu lớn nhất ")
        chon_so=input("Nhập lựa chọn của bạn :")
        if chon_so == "1" :
            in_danh_sach(ds_cua_hang)
        elif chon_so == "2" :
            cua_hang_moi=tao_cua_hang()
            ds_cua_hang.append(cua_hang_moi)
        elif chon_so == "3" :
            luu_file(ds_cua_hang)
            print("thông tin cửa hàng đã được lưu ")
        elif chon_so =="4" :
            sap_xep_theo_doanh_thu(ds_cua_hang)
            print("Cửa hàng đã được xắp xếp giảm dần theo doanh thu ")
        elif chon_so =="5" :
            ma_tim_kiem = input("Nhập mã của hàng cần tìm :")
            ket_qua_tim_kiem=tim_cua_hang_theo_ma(ds_cua_hang,ma_tim_kiem)
            print("Kết quả tìm kiếm ")
            print(ket_qua_tim_kiem)
        elif chon_so == "6" :
            ma_xoa_cua_hang = input("Nhập mã của hàng cần tìm :")
            xoa_cua_hang_theo_ma(ds_cua_hang,ma_xoa_cua_hang)
            print("Cửa hàng có mã {ma_xoa_cua_hang} đã bị xóa")
        elif chon_so == "7" :
            break
        elif chon_so == '8' :
            thong_ke_doanh_thu(ds_cua_hang)
        elif chon_so == "9" :
            loc_von=float(input("Nhập vốn đầu tư cần lọc "))
            ds_cua_hang_loc=loc_theo_von(ds_cua_hang,loc_von)
            print("Cửa hàng cần tìm là :",ds_cua_hang_loc)
        elif chon_so == "10" :
            sap_xep_theo_doanh_thu(ds_cua_hang)
            max_doanh_thu(ds_cua_hang)
        else:
            print("Lựa chọn không hợp lệ mời nhập lại ")



menu()




    



    