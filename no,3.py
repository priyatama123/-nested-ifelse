e_date=int(input("enter e_date"))
e_month=int(input("enter e_month"))
e_year=int(input("enter e_year"))
r_date=int(input("enter r_date"))
r_month=int(input("enter r_month"))
r_year=int(input("enter r_year"))
if e_month==r_month and e_year==r_year:
    if r_date<=e_date:
        print("no fine")
    elif r_date>e_date:
        n_d_l=r_date-e_date  
        fine=15*n_d_l
        print(fine)
elif r_date>e_date:
    if r_month>e_month:
        n_d_l=r_date-e_date
        n_m_l=(r_month-e_month)*30
        n_l=n_m_l-n_d_l
        fine=500*n_l
        print("n_m_l=",n_l)
        print("fine=",fine)
    else:
        print("fine charge")
elif r_month==r_month and r_date==e_date:
    if r_year>e_year:
      fixed_fine=10000
      print(fixed_fine)
    else:
        print("no fixed fine")
else:
    print("none")        