import os

def search_files(query, start_path='.'):
    """
    搜索文件和文件夹，返回匹配的文件和文件夹列表
    """
    matched_files = []
    matched_dirs = []  # 新增一个列表用于存储匹配的文件夹

    # 将用户查询字符串拆分为子字符串列表
    query_parts = query.split()

    # 递归地搜索文件和文件夹
    for root, dirs, files in os.walk(start_path):
        # 检查我们是否超过了10层的深度
        depth = root[len(start_path):].count(os.path.sep)
        if depth > 10:
            # 跳过当前目录及其子目录
            del dirs[:]
            continue

        for dir in dirs:  # 新增一个循环用于匹配文件夹名称
            if all(part in dir for part in query_parts):
                matched_dirs.append((dir, root))  # 如果匹配，则添加到 matched_dirs 列表

        for file in files:
            # 检查每个查询部分是否都在文件名中
            if all(part in file for part in query_parts):
                matched_files.append((file, root))

    return matched_files, matched_dirs  # 返回匹配的文件和文件夹列表

def main():
    while True:
        query = input("请输入你要搜索的文件或文件夹名称（输入'exit'退出程序）: ")
        if query.lower() == 'exit':
            break
        
        matched_files, matched_dirs = search_files(query)  # 获取匹配的文件和文件夹列表

        if matched_files or matched_dirs:
            if matched_files:
                print("找到以下匹配的文件:")
                for filename, path in matched_files:
                    print(f"文件名: {filename}, 路径: {path}")
                    
            if matched_dirs:  # 如果找到匹配的文件夹，输出文件夹名称和路径
                print("找到以下匹配的文件夹:")
                for dirname, path in matched_dirs:
                    print(f"文件夹名: {dirname}, 路径: {path}")
        else:
            print("没有找到匹配的文件或文件夹.")
        
        input("按任意键继续...")

if __name__ == '__main__':
    main()
