#open("test.txt","w") #w biraz tehlikeli içi dolu dosya varsa uçabilir.
file = open("test.txt","w",encoding='utf8')
file.write("Ali veli kırkdokuz elli\nhasa hüseyin\nhaçan bahri\nyagmur ege\nonsel aydin\n")
file.close()