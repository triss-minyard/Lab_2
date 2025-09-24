url = input("Введите URL: ")
cnt_replace= url.count("--")
upd_url = url.replace("--", "-")
print("Новый URl: ", upd_url,"Количество замен: ",cnt_replace)