import os

root_path = "./vup"
out_path = "./doc"
for root,dirs,files in os.walk(root_path):
    for dir in dirs:
        dir_path = root_path + "/" + dir
        files = os.listdir(dir_path)
        begin = files[0].find("【")
        end = files[0].find("】")
        contents = []
        for file in files:
            with open(dir_path + "/" + file, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith('####') and line[4] != '#':
                        continue
                    if line.startswith('<blockquote>'):
                        continue
                    contents.append(line)
        with open(out_path + "/" + files[0][begin+1:end] + ".txt", "w", encoding="utf-8") as o:
            o.writelines(contents)