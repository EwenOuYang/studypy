filename = ['a.txt', 'b.txt', 'c.txt']
fs_list = []
for fs_file in filename:
    fs_list.append(open(fs_file, 'w', encoding='utf-8'))
for fs in fs_list:
    print(fs)