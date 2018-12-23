# Nakreslete pomoci zelvy ctverec, rovnostranny trojuhelnik,
# prazdnou tabulku 10x10 bunek, domecek jednim tahem
# a neco hezkeho na zaver. :)

# Na zacatku programu je potreba importovat
# knihovnu s prikazy zelvi grafiky:
import turtle

# Potom vytvorime zelvu, ktera bude kreslit:
t = turtle.Turtle()
r = turtle.Turtle()

# Zelvu ovladame pomoci prikazu:
#   t.forward(pocet_pixelu)
#   t.back(pocet_pixelu)
#   t.left(uhel_ve_stupnich)
#   t.right(uhel_ve_stupnich)

# Pripadne muzeme pouzit pokrocilejsi prikazy:
t.speed(0)
r.speed(1)
t.penup()
t.goto(200, -100)
t.pendown()
t.color('red', 'yellow')
r.color('blue', 'black')

t.left(121) #zajimave uhly napriklad: 91, 179, 121, 161, 169
t.forward(300)
t.left(121) #zajimave uhly napriklad: 91, 179, 121, 161, 169
t.forward(300)
# Prikazy muzeme samozrejme opakovat v cyklu,
# ktery jsme se naucili minulou hodinu:
for i in range(1, 1000):
    t.left(121) #zajimave uhly napriklad: 91, 179, 121, 161, 169
    t.forward(300)
    r.left(121) #zajimave uhly napriklad: 91, 179, 121, 161, 169
    r.forward(300)
