print("perfil")
print("anime_list")
print("manga_list")
print("browse")
print("forum") 
opção = input("Onde voce quer ir? ") 

if opção == "perfil": 
    perfil = input("Vocë está no seu perfil") 
    print(perfil) 
elif opção == "anime_list": 
    anime_list = input("O que quer assistir hoje?") 
    print(anime_list) 
elif opção == "manga_list": 
    manga_list = input("O que quer ler hoje?") 
    print(manga_list) 
elif opção == "browse":
    browse = input("Onde quer navegar hoje?") 
    print(browse) 
elif opção == "forum": 
    forum = input("Voce está no forum") 
    print(forum) 
else:
    print("comando inválido") 
