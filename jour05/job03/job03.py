def triangle():
    hauteur = int(input("Hauteur du triangle : "))
    for i in range(hauteur -1):
        print(" " * (hauteur -i -1) + "/" + " " * (2*i) + "\\")
    print("/" + "__" * (hauteur -1) + "\\")

triangle()

