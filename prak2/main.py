with open('dns_addr', 'r') as f1, open('hosts', 'r') as f2:
	dns_lines = f1.readlines()		
	dns_l = [line for line in dns_lines if line.strip() and line.strip() != "-"]
	hosts_lines = f2.readlines()
	hosts_l = [line for line in hosts_lines if line.strip() and line.strip() != "-" and line.strip() != "#"]
	dns_set = set(dns_l)
	hosts_set = set(hosts_l)
	common_lines = dns_set.intersection(hosts_set)

print(f"Общее количество строк в файле с dns: {len(dns_l)}")
print(f"Количество строк, которые есть в обоих файлах: {len(common_lines)}")
print(f"Процент нежелательного трафика: {round(len(common_lines) / len(dns_l) * 100, 2)}%")
