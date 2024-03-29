def main():
    f = None
    try:
        f = open('123.txt','r',encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print("文件未找到")
    except LookupError:
        print("指定了未知的编码")
    except UnicodeDecodeError:
        print('读取文件时解码错误')
    finally:
        if f:
            f.close()

if __name__ == "__main__":
    main()