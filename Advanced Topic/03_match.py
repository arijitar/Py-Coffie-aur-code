# Match Case is similar to Switch case in C language

# It is introducd in pythin 3.10


def http_status(status):
    match status:
        case 200:
            return "OK"
        case 400:
            return "Not found"
        case "500":
            return "Unknown status"
    
#Usage
print(http_status(200))
print(http_status(404))
print(http_status(500))
print(http_status(403))