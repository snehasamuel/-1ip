mm=int(input("enter the maximum mark"))
eng=int(input("enter the mark of english"))
acc=int(input("enter the mark of accountancy"))
bs=int(input("enter the mark of business studies"))
eco=int(input("enter the mark of economics"))
ip=int(input("enter the mark of ip"))
tot=eng+acc+bs+eco+ip
t_mm=mm*5
per=(tot/t_mm)*100
print("average is:",per,"%")
if per>=91 and per<=100:
      gr='A1'
elif per>=81 and per<=90:
      gr='A2'
elif per>=71 and per<=80:
      gr='B1'

