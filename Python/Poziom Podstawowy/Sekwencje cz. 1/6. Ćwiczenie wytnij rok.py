def get_year( date ):
    if date[:3] == "199":
        return date[:4]
    else:
        return date[4:]
