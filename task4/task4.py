gross_salary = basic_salary + hra + da
net_salary = gross_salary - pf

print("\nEmployee Name:", name)
print("Basic Salary: Rs.", round(basic_salary, 2))
print("HRA: Rs.", round(hra, 2))
print("DA: Rs.", round(da, 2))
print("Gross Salary: Rs.", round(gross_salary, 2))
print("PF Deduction: Rs.", round(pf, 2))
print("Net Salary: Rs.", round(net_salary, 2))
