def main():
    try:
        a = int(input("Enter a number please : "))
        print(a)
        return


    except Exception as e:
        print(e)    
        return

    finally:
        print("I am here , inside the finally block")   # finally ka use function me hoga , agr ye finally nhi hota to return ho jaega , ye statement print nhi hoga - so ham keh skte hai ki " Finally chalega hi chalega , chahe function return hi kyu na kr raha ho "

main()       