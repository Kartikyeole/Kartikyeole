for x in range(int(input())):
                A,B,C,D,E = map(int,input().split(" "))
                if A + B + C <= D:
                                a = "yes"
                elif A <= E:
                                a = "yes"
                elif B <= E:
                                a = "yes"
                elif C <= E:
                                a = "yes"
                print(a)
                a = "no"
