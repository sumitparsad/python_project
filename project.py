while True:
    n=int(input("Enter choice \n1 for URL Shortner \n2 for URL Expander \n3 for exit\n"))
    if n==1:
        import pyshorteners
        original = input("Enter the URL to shorten: ")
        
        type_bitly = pyshorteners.Shortener(api_key='9318df9e5a40822f9fe61058b06dfcfa663d3032')
        shortened = type_bitly.bitly.short(original)
        print(shortened)
    
    elif n==2:
        import pyshorteners
        shortened = input("Enter the URL to expand: ")
        
        type_bitly = pyshorteners.Shortener(api_key='9318df9e5a40822f9fe61058b06dfcfa663d3032')
        original = type_bitly.bitly.expand(shortened)
        print(original)
        
    elif n==3:
        
        break
        
    else:
        print("Invalid Input")