https_status = 704;

match https_status :
    case 200:
        print('Success');
    case 400 | 404:
        print('Bad Request');
    case _ :
        print('Im a default case')