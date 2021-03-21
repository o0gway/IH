from urllib.parse import urlparse, ParseResult


def parse(query: str) -> dict:
    item = urlparse(query)
    result = {}
    if item[4] != "":
        data = item[4]
        datalist = data.split("&")

        for i in range(len(datalist)):
            if datalist[i] != "":
                element = str(datalist[i]).split("=")
                result[element[0]] = element[1]
        return result
    else:
        return result


def parse_cookie(query: str) -> dict:
    pass


if __name__ == '__main__':
    # parse
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}

    # parse_cookie
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
