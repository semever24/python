try:
    f = open("sample.txt","a")
    try:
        f.write("\nTry & Except example2")
    except:
        print("Something went wrong")
except:
    print("Something went wrong")
else:
    print("Works perfect")
finally:
    f.close()