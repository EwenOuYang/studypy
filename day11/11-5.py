def main():
    try:
        with open('ball.png','rb') as f1:
            data = f1.read()
            print(type(data))
        with open('ball2.png','wb') as f2:
            f2.write(data)
    except FileNotFoundError:
        print("指定的文件不存在")
    except IOError as e:
        print("读写文件时出现错误")
    print('程序执行结束.')

if __name__ == '__main__':
    main()
