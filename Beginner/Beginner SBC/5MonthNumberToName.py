#5 Convert month number to month name | Airbnb

lst_dates = ['01-01-2020','21-03-2022','11-06-2023','12-12-2020']


def sort_list_with_numerical_values(l):
  month_dict={'01':'Jan', '02':'Feb', '03':'Mar', '04':'Apr', '05':'May', '06':'Jun', 
  '07':'Jul', '08':'Aug', '09':'Sep', '10':'Oct', '11':'Nov', '12':'Dec'}
  l1=[]
  for i in l:
    month_number=i.split("-")
    month_name=month_dict[month_number[1]]
    l1.append(month_number[0]+'-'+month_name+'-'+month_number[2])
  return l1
 
print(sort_list_with_numerical_values(lst_dates))


